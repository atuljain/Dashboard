from django.shortcuts import render, render_to_response, redirect
from django.template import RequestContext
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.utils.crypto import get_random_string
from django.contrib import messages
from django.core.urlresolvers import reverse

from profiles.models import Profile

from accounts.forms import LoginForm


def profiles_list(request):
    profiles_list = Profile.objects.all()
    return render_to_response("profiles/profiles_list.html",{
        "profiles_list": profiles_list,
        "current": "profiles_list"
    }, context_instance=RequestContext(request))
