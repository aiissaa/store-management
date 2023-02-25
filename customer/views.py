from django.shortcuts import render
from django.views.generic import FormView
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

from .forms import SignUpForm


class SignUpView(FormView):
    template_name = 'customer/signup.html'
    form_class = SignUpForm
    success_url = '/'

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return super().form_valid(form)
