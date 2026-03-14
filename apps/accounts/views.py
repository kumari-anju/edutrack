from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic

@login_required
def profile(request):
    """View function for the user profile page."""
    return render(request, 'accounts/profile.html')

class SignUpView(generic.CreateView):
    """View class for user registration."""
    form_class = UserCreationForm
    success_url = reverse_lazy('accounts:login')
    template_name = 'accounts/signup.html'

    def dispatch(self, request, *args, **kwargs):
        """Redirects authenticated users to their profile page."""
        if request.user.is_authenticated:
            return redirect('accounts:profile')
        return super().dispatch(request, *args, **kwargs)
