from django.db import models
from django.test import TestCase
from apps.students.models import Student
from apps.courses.models import Course
from apps.enrollments.models import Enrollment
from .models import Attendance
import datetime


class AttendanceModelTest(TestCase):
    """Basic unit tests for the Attendance model."""

    def setUp(self):
        """Set up test fixtures: student, course, and enrollment."""
        self.student = Student.objects.create(
            first_name="Alice", last_name="Smith",
            email="alice@example.com", grade_level=10
        )
        self.course = Course.objects.create(
            title="Mathematics 101",
            description="Basic maths",
            credits=3,
        )
        self.enrollment = Enrollment.objects.create(
            student=self.student,
            course=self.course,
            status='ENROLLED',
        )
        self.today = datetime.date.today()

    def test_create_attendance_record(self):
        """Attendance record should be created successfully."""
        att = Attendance.objects.create(
            enrollment=self.enrollment,
            date=self.today,
            status='PRESENT',
        )
        self.assertEqual(att.status, 'PRESENT')
        self.assertEqual(att.enrollment, self.enrollment)

    def test_str_representation(self):
        """__str__ should include student name, course, and status."""
        att = Attendance.objects.create(
            enrollment=self.enrollment,
            date=self.today,
            status='ABSENT',
        )
        self.assertIn('Alice Smith', str(att))
        self.assertIn('Absent', str(att))

    def test_unique_together_constraint(self):
        """Two attendance records for the same enrollment+date should raise IntegrityError."""
        from django.db import IntegrityError
        Attendance.objects.create(
            enrollment=self.enrollment,
            date=self.today,
            status='PRESENT',
        )
        with self.assertRaises(IntegrityError):
            Attendance.objects.create(
                enrollment=self.enrollment,
                date=self.today,
                status='ABSENT',
            )
