from django.shortcuts import render, HttpResponse, redirect
# importing User Class
from django.contrib.auth.models import User

from django.contrib.auth import authenticate, login, logout, get_user_model

from django.contrib import messages

# Create your views here.
def myAccount(request):
    return HttpResponse('done')

# Sign Up Method
def handleSignUp(request):
    if request.method == 'POST':

        # Get User Credentials
        usr_fname = request.POST['u_fname']
        usr_lname = request.POST['u_lname']
        usr_email = request.POST['u_email']
        usr_username = request.POST['u_username']
        usr_password = request.POST['u_pass']
        usr_conf_pass = request.POST['c_pass']

        # Validation Checks here

        if len(usr_username) > 20:
            messages.error(request, 'Username must contain 20 characters only! Please try again.')
            return redirect('HomePage')
        
        if usr_password != usr_conf_pass:
            messages.error(request, "Your passwords don't match! Please try again.")
            return redirect('HomePage')
        
        # Create a new user
        tpc_new_usr = User.objects.create_user(usr_username, usr_email, usr_password)
        tpc_new_usr.first_name = usr_fname
        tpc_new_usr.last_name = usr_lname
        tpc_new_usr.save()
        messages.success(request,'Thanks '+usr_fname+' for creating an account on ThePunchCoders')
        return redirect('HomePage')


    else:
        return render(request, 'account/signup.html')

def handleSignin(request):
    if request.method == 'POST':
        # Get User Credentials
        
        log_usr_username = request.POST['log_username']
        log_usr_pass = request.POST['log_pass']
        
        user = authenticate(username=log_usr_username, password=log_usr_pass)

        if user is not None:
            login(request, user)
            messages.success(request,'Successfully logged in as '+log_usr_username)
            return redirect('HomePage')
        else:
            messages.error(request,'Invalid Credentials! Please try again.')
            return redirect('SigninPage')

    else:
        return render(request, 'account/signin.html')

def handleLogout(request):
    logout(request)
    messages.success(request,'Successfully logged out')
    return redirect('HomePage')


def userProfile(request, username):
    all_users= get_user_model().objects.all()
    flag=0
    for user in all_users:
        if username == user.username:
            flag=1
            content = {'username': username}
            return render(request, 'account/profile.html', content)

    if flag != 1:
        return render(request, '404.html')