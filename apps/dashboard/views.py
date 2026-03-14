from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
import datetime
from apps.students.models import Student
from apps.courses.models import Course
from apps.enrollments.models import Enrollment
from apps.attendance.models import Attendance

class DashboardView(LoginRequiredMixin, TemplateView):
    """View class for the main application dashboard."""
    template_name = 'dashboard/index.html'

    def get_context_data(self, **kwargs):
        """Retrieves summary statistics for the dashboard context."""
        context = super().get_context_data(**kwargs)
        context['total_students'] = Student.objects.count()
        context['total_courses'] = Course.objects.count()
        context['total_enrollments'] = Enrollment.objects.count()
        context['today_attendance'] = Attendance.objects.filter(
            date=datetime.date.today()
        ).count()
        return context
