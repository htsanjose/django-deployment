from django.shortcuts import render
from baseapp.forms import UserForm, UserProfileInfoForm

from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
#from django.core.urlresolvers import reverse
from django.urls import reverse
from django.contrib.auth.decorators import login_required

# Create your views here.
def index(request):
    return render(request, 'baseapp/index.html')

@login_required
def special(request):
    return render(request,'baseapp/index.html')

@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))

def register(request):
    registered = False
    if request.method == "POST":
        user_form = UserForm(data=request.POST)
        profile_form = UserProfileInfoForm(data=request.POST)

        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            user.set_password(user.password) # hash password and save
            user.save()

            profile = profile_form.save(commit=False) # not save yet to avoid collision
            profile.user = user

            if 'profile_pic' in request.FILES:
                profile.profile_pic = request.FILES['profile_pic']

            profile.save()
            registered = True

        else:
            print(user_form.errors, profile_form.errors)

    else:
        user_form = UserForm()
        profile_form = UserProfileInfoForm()

    return render(request, 'baseapp/registration.html', context=
                            {'user_form':user_form,
                             'profile_form':profile_form,
                             'registered': registered})

def user_login(request):

    if request.method == 'POST':
        username = request.POST.get('uname') # uname from login.html
        password = request.POST.get('pwd') # pwd from logn.html

        user = authenticate(username=username, password=password)

        if user:
            if user.is_active:
                login(request,user)
                return HttpResponseRedirect(reverse('index'))
            else:
                return HttpResponse("Account not active")
        else:
            print("Someone tried to login and failed!")
            print("Username: {} and password: {}".format(username,password))
            return HttpResponse("Invalid login details!")
    else:
        return render(request,'baseapp/login.html')
