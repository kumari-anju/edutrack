from django import forms
from .models import Attendance
from apps.enrollments.models import Enrollment


class AttendanceForm(forms.ModelForm):
    """Form for recording a single attendance entry."""

    class Meta:
        model = Attendance
        fields = ['enrollment', 'date', 'status', 'notes']
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'status': forms.Select(attrs={'class': 'form-select'}),
            'notes': forms.Textarea(attrs={'class': 'form-control', 'rows': 2}),
            'enrollment': forms.Select(attrs={'class': 'form-select'}),
        }

    def __init__(self, *args, course=None, **kwargs):
        """Optionally filter enrollments to a specific course."""
        super().__init__(*args, **kwargs)
        if course:
            self.fields['enrollment'].queryset = Enrollment.objects.filter(
                course=course, status='ENROLLED'
            ).select_related('student', 'course')
        else:
            self.fields['enrollment'].queryset = Enrollment.objects.filter(
                status='ENROLLED'
            ).select_related('student', 'course')


class BulkAttendanceForm(forms.Form):
    """
    Form for selecting a course and date before bulk-marking attendance.
    The actual per-student status rows are rendered as dynamic formset rows in the template.
    """
    date = forms.DateField(
        widget=forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
        label="Session Date",
    )
    course = forms.ModelChoiceField(
        queryset=None,
        widget=forms.Select(attrs={'class': 'form-select'}),
        label="Course",
    )

    def __init__(self, *args, **kwargs):
        from apps.courses.models import Course
        super().__init__(*args, **kwargs)
        self.fields['course'].queryset = Course.objects.all()
