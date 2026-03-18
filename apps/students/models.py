from django.db import models
from django.core.validators import MinValueValidator

class Student(models.Model):
    """
    Represents a student in the EduTrack system.
    """
    student_id = models.CharField(max_length=20, unique=True, help_text="Unique Identifier for the Student")
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    enrollment_date = models.DateField(auto_now_add=True)
    grade_level = models.IntegerField(default=1, validators=[MinValueValidator(1)])
    is_active = models.BooleanField(default=True)
    courses = models.ManyToManyField('courses.Course', through='enrollments.Enrollment', related_name='students_enrolled')

    def __str__(self):
        """Returns the identifier and full name of the student."""
        return f"[{self.student_id}] {self.first_name} {self.last_name}"

    class Meta:
        ordering = ['-enrollment_date']
