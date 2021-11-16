from django.contrib.auth import decorators
from django.http import HttpResponse
from django.http.response import HttpResponseNotAllowed
from django.shortcuts import redirect
from django.contrib.auth import authenticate, login, logout


def unauthenticated_user(view_func):
        def wrapper_func(request, *args, **kwargs):
            if request.user.is_authenticated:
                return redirect('home')
            else:
                return view_func(request, *args, **kwargs)

        return wrapper_func
            



def allowed_users(allowed_roles = []):
    def decorator(view_func):
        def wrapper_func (request, *args, **kwargs):
            group = None
            if request.user.groups.exists():
                group = request.user.groups.all()[0].name
            if group in allowed_roles:
                return view_func(request, *args, **kwargs)
            else:
                logout(request)
                return HttpResponse('Not allowed')

        return wrapper_func
    return decorator


