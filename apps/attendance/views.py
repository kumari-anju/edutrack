import datetime
import json
from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView
from django.contrib import messages
from django.db import IntegrityError
from django.db.models import Count, Q

from apps.courses.models import Course
from apps.enrollments.models import Enrollment
from .models import Attendance
from .forms import BulkAttendanceForm


class AttendanceMarkView(LoginRequiredMixin, View):
    """
    GET:  Renders a bulk mark-attendance form.  
          Query params: course=<pk> and date=<YYYY-MM-DD> to pre-fill.
    POST: Saves one attendance row per enrolled student for the given course+date.
          Existing records for the same (enrollment, date) are updated rather than
          re-created, so the view is safely idempotent.
    """
    template_name = 'attendance/mark.html'

    def _get_context(self, courses, course=None, date=None, enrollments=None, existing=None):
        """Build shared template context."""
        return {
            'courses': courses,
            'selected_course': course,
            'selected_date': date,
            'enrollments': enrollments or [],
            'existing': existing or {},
            'status_choices': Attendance.STATUS_CHOICES,
        }

    def get(self, request):
        """Display the mark-attendance page."""
        courses = Course.objects.all()
        course_pk = request.GET.get('course')
        date_str = request.GET.get('date') or datetime.date.today().isoformat()

        try:
            selected_date = datetime.date.fromisoformat(date_str)
        except ValueError:
            selected_date = datetime.date.today()

        selected_course = None
        enrollments = []
        existing = {}

        if course_pk:
            selected_course = get_object_or_404(Course, pk=course_pk)
            enrollments = (
                Enrollment.objects
                .filter(course=selected_course, status='ENROLLED')
                .select_related('student')
            )
            # Pre-load existing attendance records for this course+date
            existing = {
                att.enrollment_id: att
                for att in Attendance.objects.filter(
                    enrollment__course=selected_course,
                    date=selected_date,
                )
            }

        return render(request, self.template_name, self._get_context(
            courses, selected_course, selected_date, enrollments, existing
        ))

    def post(self, request):
        """Save/update attendance for all enrolled students in the selected course+date."""
        course_pk = request.POST.get('course')
        date_str = request.POST.get('date')

        try:
            selected_date = datetime.date.fromisoformat(date_str)
        except (ValueError, TypeError):
            messages.error(request, "Invalid date.")
            return redirect('attendance:mark')

        selected_course = get_object_or_404(Course, pk=course_pk)
        enrollments = Enrollment.objects.filter(course=selected_course, status='ENROLLED')

        saved_count = 0
        for enrollment in enrollments:
            status = request.POST.get(f'status_{enrollment.pk}', 'ABSENT')
            notes = request.POST.get(f'notes_{enrollment.pk}', '')
            # Update or create so the view is safely idempotent
            Attendance.objects.update_or_create(
                enrollment=enrollment,
                date=selected_date,
                defaults={'status': status, 'notes': notes},
            )
            saved_count += 1

        messages.success(
            request,
            f"Attendance saved for {saved_count} student(s) on {selected_date.strftime('%B %d, %Y')}."
        )
        return redirect(
            f"{request.path}?course={course_pk}&date={selected_date.isoformat()}"
        )


class AttendanceDailyReportView(LoginRequiredMixin, TemplateView):
    """
    Daily attendance report for a given course and date.
    Query params: course=<pk> and date=<YYYY-MM-DD>
    """
    template_name = 'attendance/daily_report.html'

    def get_context_data(self, **kwargs):
        """Builds report context from query params."""
        context = super().get_context_data(**kwargs)
        courses = Course.objects.all()
        course_pk = self.request.GET.get('course')
        date_str = self.request.GET.get('date') or datetime.date.today().isoformat()

        try:
            selected_date = datetime.date.fromisoformat(date_str)
        except ValueError:
            selected_date = datetime.date.today()

        selected_course = None
        records = []
        summary = {}

        if course_pk:
            selected_course = get_object_or_404(Course, pk=course_pk)
            records = (
                Attendance.objects
                .filter(enrollment__course=selected_course, date=selected_date)
                .select_related('enrollment__student', 'enrollment__course')
            )
            # Quick summary counts
            summary = {
                'present': records.filter(status='PRESENT').count(),
                'absent': records.filter(status='ABSENT').count(),
                'late': records.filter(status='LATE').count(),
                'total': records.count(),
            }

        context.update({
            'courses': courses,
            'selected_course': selected_course,
            'selected_date': selected_date,
            'records': records,
            'summary': summary,
        })
        return context


class AttendanceMonthlyReportView(LoginRequiredMixin, TemplateView):
    """
    Monthly attendance report for a given course and calendar month.
    Query params: course=<pk> and month=<YYYY-MM>
    """
    template_name = 'attendance/monthly_report.html'

    def get_context_data(self, **kwargs):
        """Aggregates per-student attendance counts for the selected month."""
        context = super().get_context_data(**kwargs)
        courses = Course.objects.all()
        course_pk = self.request.GET.get('course')
        month_str = self.request.GET.get('month') or datetime.date.today().strftime('%Y-%m')

        try:
            year, month = map(int, month_str.split('-'))
            selected_month_start = datetime.date(year, month, 1)
        except (ValueError, TypeError):
            selected_month_start = datetime.date.today().replace(day=1)
            year = selected_month_start.year
            month = selected_month_start.month

        selected_course = None
        student_stats = []

        if course_pk:
            selected_course = get_object_or_404(Course, pk=course_pk)
            enrollments = (
                Enrollment.objects
                .filter(course=selected_course, status='ENROLLED')
                .select_related('student')
            )

            for enrollment in enrollments:
                records = Attendance.objects.filter(
                    enrollment=enrollment,
                    date__year=year,
                    date__month=month,
                )
                present = records.filter(status='PRESENT').count()
                absent  = records.filter(status='ABSENT').count()
                late    = records.filter(status='LATE').count()
                total   = records.count()
                pct = round((present / total * 100), 1) if total > 0 else None
                student_stats.append({
                    'student': enrollment.student,
                    'present': present,
                    'absent': absent,
                    'late': late,
                    'total': total,
                    'attendance_pct': pct,
                })

        context.update({
            'courses': courses,
            'selected_course': selected_course,
            'selected_month': selected_month_start,
            'month_str': f"{year:04d}-{month:02d}",
            'student_stats': student_stats,
        })
        return context


class StudentAttendanceReportView(LoginRequiredMixin, TemplateView):
    """
    Student-specific attendance visualization.
    Query params: student=<pk>
    """
    template_name = 'attendance/student_report.html'

    def get_context_data(self, **kwargs):
        """Prepares chart data for daywise, weekly, and monthly attendance."""
        context = super().get_context_data(**kwargs)
        from apps.students.models import Student
        students = Student.objects.filter(is_active=True).order_by('last_name', 'first_name')
        
        student_pk = self.request.GET.get('student')
        selected_student = None
        
        chart_data = {
            'daywise': {},
            'weekly': {},
            'monthly': {}
        }

        if student_pk:
            selected_student = get_object_or_404(Student, pk=student_pk)
            
            # All attendance records for this student
            records = Attendance.objects.filter(enrollment__student=selected_student).order_by('-date')
            
            # --- 1. Daywise Data (Last 14 distinct session dates) ---
            from collections import defaultdict
            daily_agg = defaultdict(lambda: {'PRESENT': 0, 'ABSENT': 0, 'LATE': 0})
            
            # Distinct dates for the last 14 days of attendance
            dates = list(records.values_list('date', flat=True).distinct().order_by('-date')[:14])
            recent_records = records.filter(date__in=dates)
            
            for rec in recent_records:
                daily_agg[rec.date.isoformat()][rec.status] += 1
            
            sorted_dates = sorted(daily_agg.keys())
            chart_data['daywise'] = {
                'labels': [datetime.date.fromisoformat(d).strftime('%b %d') for d in sorted_dates],
                'present': [daily_agg[d]['PRESENT'] for d in sorted_dates],
                'absent': [daily_agg[d]['ABSENT'] for d in sorted_dates],
                'late': [daily_agg[d]['LATE'] for d in sorted_dates],
            }
            
            # --- 2. Weekly Data (Last 12 weeks) ---
            today = datetime.date.today()
            start_of_week = today - datetime.timedelta(days=today.weekday())
            weeks = []
            for i in range(12):
                w_start = start_of_week - datetime.timedelta(weeks=i)
                weeks.append(w_start)
            weeks.reverse()
            
            weekly_agg = {w.isoformat(): {'label': w.strftime('%b %d'), 'PRESENT': 0, 'ABSENT': 0, 'LATE': 0} for w in weeks}
            
            twelve_weeks_ago = weeks[0]
            weekly_records = records.filter(date__gte=twelve_weeks_ago)
            
            for rec in weekly_records:
                rec_week_start = rec.date - datetime.timedelta(days=rec.date.weekday())
                key = rec_week_start.isoformat()
                if key in weekly_agg:
                    weekly_agg[key][rec.status] += 1
            
            sorted_weeks = sorted(weekly_agg.keys())
            chart_data['weekly'] = {
                'labels': [weekly_agg[k]['label'] for k in sorted_weeks],
                'present': [weekly_agg[k]['PRESENT'] for k in sorted_weeks],
                'absent': [weekly_agg[k]['ABSENT'] for k in sorted_weeks],
                'late': [weekly_agg[k]['LATE'] for k in sorted_weeks],
            }

            # --- 3. Monthly Data (Last 6 months) ---
            months = []
            curr_date = today.replace(day=1)
            for _ in range(6):
                months.append((curr_date.year, curr_date.month))
                if curr_date.month == 1:
                    curr_date = curr_date.replace(year=curr_date.year - 1, month=12)
                else:
                    curr_date = curr_date.replace(month=curr_date.month - 1)
            months.reverse()
            
            monthly_agg = {f"{y}-{m:02d}": {'label': datetime.date(y, m, 1).strftime('%b %Y'), 'PRESENT': 0, 'ABSENT': 0, 'LATE': 0} for y, m in months}
            
            six_months_ago = datetime.date(months[0][0], months[0][1], 1)
            monthly_records = records.filter(date__gte=six_months_ago)
            
            for rec in monthly_records:
                key = f"{rec.date.year}-{rec.date.month:02d}"
                if key in monthly_agg:
                    monthly_agg[key][rec.status] += 1
            
            sorted_months = sorted(monthly_agg.keys())
            chart_data['monthly'] = {
                'labels': [monthly_agg[k]['label'] for k in sorted_months],
                'present': [monthly_agg[k]['PRESENT'] for k in sorted_months],
                'absent': [monthly_agg[k]['ABSENT'] for k in sorted_months],
                'late': [monthly_agg[k]['LATE'] for k in sorted_months],
            }
            
        context.update({
            'students': students,
            'selected_student': selected_student,
            'chart_data_json': json.dumps(chart_data)
        })
        return context
