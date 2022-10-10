from django.shortcuts import render, redirect, reverse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth import Login, Logout, authenticate
from django.conf import settings
from django.http import JsonResponse
from django.views.generic.edit import FormView
from django.views.generic.base import TemplateView
from django.utils.decorators import method_decorator

from did_django_google_tutorial.mixins import(
    AjaxFormMixin,
    reCAPTCHAValidation,
    FormErrors,
    RedirectParams,
    )

from .forms import (
    UserForm,
    UserProfileForm,
    AuthForm,
)


class AccountView(TemplateView):
    '''
    Generic FormView with our mixin to display user account page
    '''
    template_name = 'users/account.html'

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)