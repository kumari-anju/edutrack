from django.apps import AppConfig


class AttendanceConfig(AppConfig):
    """App configuration for the attendance tracking module."""
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'apps.attendance'
    label = 'attendance'
