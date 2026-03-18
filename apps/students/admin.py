from django.contrib import admin
from .models import Student

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('student_id', 'first_name', 'last_name', 'email', 'grade_level', 'is_active')
    list_filter = ('grade_level', 'is_active')
    search_fields = ('student_id', 'first_name', 'last_name', 'email')
