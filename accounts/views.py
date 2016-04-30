from django.shortcuts import render, render_to_response, redirect
from django.template import RequestContext
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.utils.crypto import get_random_string
from django.contrib import messages
from django.core.urlresolvers import reverse

from accounts.forms import LoginForm



def login_user(request):
    """
        Function is used for login the registered user in the Peekhi.
    """

    if request.user.is_authenticated():
        return redirect(reverse('profiles_list'))

    if request.method == "POST":
        form = LoginForm(request.POST)

        if form.is_valid():
            user_obj = User.objects.get(email=form.cleaned_data['email'])
            user = authenticate(username=user_obj.username, password=form.cleaned_data['password'])

            if user:

                if user.is_active:
                    login(request, user)

                    return redirect(request.GET.get('next') or reverse('profiles_list'))

                messages.add_message(request, messages.ERROR, "Please check your email and verify the email address to log on to 64 bit Consultants.")

                return redirect(reverse('login_user'))

            error_message = "Email Id and password did't match."

            return render_to_response("accounts/login_user.html",{
                "form": form,
                "error_message": error_message,
                "current": "login",
                "next": request.POST.get('next', '')
            }, context_instance=RequestContext(request))

        return render_to_response("accounts/login_user.html",{
            "form": form,
            "current": "login",
            "next": request.POST.get('next', '')
        }, context_instance=RequestContext(request))
    else:
        form = LoginForm()

        return render_to_response("accounts/login_user.html", {
            "form": form,
            "current": "login",
            "next": request.GET.get('next', '')
        }, context_instance=RequestContext(request))


def logout_user(request):
    """
        Function is used to logout the user from the Peekhi.
    """

    logout(request)
    return redirect(reverse('login_user'))
