from django.conf import settings
from django.shortcuts import redirect
from urllib.parse import urlencode
import requests
import json
import datetime
from humanfriendly import format_timespan
from django.http import JsonResponse


def FormErrors(*args):
    '''
    Handles form error that are passed back to AJAX calls
    '''
    message = ''
    for f in args:
        if f.errors:
            message = f.errors.as_text()
    return message


def reCAPTCHAValidation(token):
    '''
    reCAPTCHA validation
    '''
    result = requests.post(
        'https://www.google.com/recaptcha/api/siteverify',
        data={
            'secret': settings.RECAPTCHA_PRIVATE_KEY,
            'response': token
        })
    
    return result.json()