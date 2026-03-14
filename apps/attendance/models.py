from django.db import models


class Attendance(models.Model):
    """
    Records a student's attendance for a course session on a given date.
    One record per enrolled student per course per day (enforced via unique_together).
    """
    STATUS_CHOICES = [
        ('PRESENT', 'Present'),
        ('ABSENT', 'Absent'),
        ('LATE', 'Late'),
    ]

    enrollment = models.ForeignKey(
        'enrollments.Enrollment',
        on_delete=models.CASCADE,
        related_name='attendance_records',
        help_text="The enrollment this attendance record is tied to."
    )
    date = models.DateField(
        help_text="The date of the course session."
    )
    status = models.CharField(
        max_length=10,
        choices=STATUS_CHOICES,
        default='PRESENT',
        help_text="Attendance status for this session."
    )
    notes = models.TextField(
        blank=True,
        help_text="Optional notes (e.g. reason for absence)."
    )
    recorded_at = models.DateTimeField(
        auto_now_add=True,
        help_text="Timestamp when the record was created."
    )

    class Meta:
        unique_together = ('enrollment', 'date')
        ordering = ['-date']

    def __str__(self):
        """Returns a human-readable summary of the attendance record."""
        return f"{self.enrollment.student} — {self.enrollment.course} on {self.date}: {self.get_status_display()}"
