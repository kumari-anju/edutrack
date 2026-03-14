from django.db import models


class Student(models.Model):
    """
    Represents a student in the EduTrack system.
    """
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    enrollment_date = models.DateField(auto_now_add=True)
    grade_level = models.IntegerField(default=1)
    is_active = models.BooleanField(default=True)
    courses = models.ManyToManyField('courses.Course', through='enrollments.Enrollment', related_name='students_enrolled')

    def __str__(self):
        """Returns the full name of the student."""
        return f"{self.first_name} {self.last_name}"

    class Meta:
        ordering = ['-enrollment_date']
