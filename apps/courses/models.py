from django.db import models

class Course(models.Model):
    """
    Represents a course in the EduTrack system.
    """
    title = models.CharField(max_length=200)
    description = models.TextField()
    credits = models.PositiveIntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    students = models.ManyToManyField('students.Student', through='enrollments.Enrollment', related_name='courses_enrolled')

    def __str__(self):
        """Returns the course title."""
        return self.title
