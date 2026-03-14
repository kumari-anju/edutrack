from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Student

class StudentListView(LoginRequiredMixin, ListView):
    """View class to list all registered students."""
    model = Student
    template_name = 'students/student_list.html'
    context_object_name = 'students'

class StudentDetailView(LoginRequiredMixin, DetailView):
    """View class to show details for a specific student."""
    model = Student
    template_name = 'students/student_detail.html'

class StudentCreateView(LoginRequiredMixin, CreateView):
    """View class to register a new student."""
    model = Student
    template_name = 'students/student_form.html'
    fields = ['first_name', 'last_name', 'email', 'grade_level', 'is_active']
    success_url = reverse_lazy('students:list')

class StudentUpdateView(LoginRequiredMixin, UpdateView):
    """View class to update student information."""
    model = Student
    template_name = 'students/student_form.html'
    fields = ['first_name', 'last_name', 'email', 'grade_level', 'is_active']
    success_url = reverse_lazy('students:list')

class StudentDeleteView(LoginRequiredMixin, DeleteView):
    """View class to delete a student record."""
    model = Student
    template_name = 'students/student_confirm_delete.html'
    success_url = reverse_lazy('students:list')
