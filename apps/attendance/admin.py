from django.contrib import admin
from .models import Attendance


@admin.register(Attendance)
class AttendanceAdmin(admin.ModelAdmin):
    """Admin configuration for Attendance records."""
    list_display = ['enrollment', 'date', 'status', 'recorded_at']
    list_filter = ['status', 'date', 'enrollment__course']
    search_fields = [
        'enrollment__student__first_name',
        'enrollment__student__last_name',
        'enrollment__course__title',
    ]
    date_hierarchy = 'date'
    ordering = ['-date']
