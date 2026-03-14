from django.urls import path
from . import views

app_name = 'attendance'

urlpatterns = [
    # Mark attendance (bulk) for a course session
    path('mark/', views.AttendanceMarkView.as_view(), name='mark'),
    # Daily attendance report: ?course=<pk>&date=<YYYY-MM-DD>
    path('daily/', views.AttendanceDailyReportView.as_view(), name='daily_report'),
    # Monthly attendance report: ?course=<pk>&month=<YYYY-MM>
    path('monthly/', views.AttendanceMonthlyReportView.as_view(), name='monthly_report'),
    # Student specific attendance visual report: ?student=<pk>
    path('student/', views.StudentAttendanceReportView.as_view(), name='student_report'),
]
