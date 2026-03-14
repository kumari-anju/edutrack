from django.urls import path
from . import views

app_name = 'enrollments'

urlpatterns = [
    path('', views.EnrollmentListView.as_view(), name='list'),
    path('add/', views.EnrollmentCreateView.as_view(), name='create'),
]
