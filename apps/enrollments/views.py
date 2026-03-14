from django.shortcuts import render, redirect
from django.views.generic import ListView, CreateView
from django.urls import reverse_lazy
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Enrollment
from .forms import EnrollmentForm

class EnrollmentListView(LoginRequiredMixin, ListView):
    """View class to list all student enrollments."""
    model = Enrollment
    template_name = 'enrollments/enrollment_list.html'
    context_object_name = 'enrollments'

class EnrollmentCreateView(LoginRequiredMixin, CreateView):
    """View class to create a new enrollment."""
    model = Enrollment
    form_class = EnrollmentForm
    template_name = 'enrollments/enrollment_form.html'
    success_url = reverse_lazy('enrollments:list')

    def form_valid(self, form):
        """Displays a success message upon valid form submission."""
        messages.success(self.request, "Student enrolled successfully!")
        return super().form_valid(form)
