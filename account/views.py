from .form import CustomUserCreationForm
from django.shortcuts import render
from django.views.generic import CreateView
from django.urls import reverse_lazy

# Create your views here.
class SignUpViews(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'