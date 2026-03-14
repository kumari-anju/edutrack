from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Course

class CourseListView(LoginRequiredMixin, ListView):
    """View class to list all available courses."""
    model = Course
    template_name = 'courses/course_list.html'
    context_object_name = 'courses'

class CourseCreateView(LoginRequiredMixin, CreateView):
    """View class to create a new course."""
    model = Course
    template_name = 'courses/course_form.html'
    fields = ['title', 'description', 'credits']
    success_url = reverse_lazy('courses:course_list')

class CourseUpdateView(LoginRequiredMixin, UpdateView):
    """View class to update an existing course."""
    model = Course
    template_name = 'courses/course_form.html'
    fields = ['title', 'description', 'credits']
    success_url = reverse_lazy('courses:course_list')

class CourseDeleteView(LoginRequiredMixin, DeleteView):
    """View class to delete a course."""
    model = Course
    template_name = 'courses/course_confirm_delete.html'
    success_url = reverse_lazy('courses:course_list')
