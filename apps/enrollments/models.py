from django.db import models
from apps.students.models import Student
from apps.courses.models import Course

class Enrollment(models.Model):
    """
    Represents the enrollment of a student in a course.
    """
    STATUS_CHOICES = [
        ('ENROLLED', 'Enrolled'),
        ('COMPLETED', 'Completed'),
        ('DROPPED', 'Dropped'),
    ]

    student = models.OneToOneField(Student, on_delete=models.CASCADE, related_name='enrollment')
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='enrollments')
    enrollment_date = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='ENROLLED')

    class Meta:
        unique_together = ('student', 'course')
        ordering = ['-enrollment_date']

    def __str__(self):
        """Returns a string representation of the enrollment."""
        return f"{self.student} - {self.course}"
