from django.shortcuts import render,redirect
from django.contrib.auth. models import User,auth
from django.contrib import messages
from django.views.decorators.cache import never_cache



# Create your views here.

@never_cache
def loginPage(request):
    if request.session.session_key:
        if request.user.is_staff:
            return redirect('admin-home')
        else:
            return redirect('user-home')
    print(request.session.session_key)
    if request.method == 'POST':
        name = request.POST.get('username')
        password = request.POST.get('password')
        user= auth.authenticate(username=name,password= password)
        if user :
            if user.is_staff:
                auth.login(request,user)
                return redirect('admin-home')
            else:
                auth.login(request,user)
                return redirect('user-home')
        else:
            messages.error(request,'invalid user')
            return redirect('login-page')
    return render(request,'login.html')

@never_cache
def registerPage(request):
    if request.session.session_key:
        if request.user.is_staff:
            return redirect('admin-home')
        else:
            return redirect('user-home')
    if request.method=='POST':
        name=request.POST.get('username')
        email=request.POST.get('email')
        password=request.POST.get('password')
        password2=request.POST.get('password2')
        f_name=request.POST.get('f_name')
        l_name=request.POST.get('l_name')
        username_obj= User.objects.filter(username= name)
        if password == password2:
            if username_obj:
                messages.error(request,'this user is already taken')
                return redirect('register-page')
            else:
                myuser= User.objects.create_user(username=name,email=email,password=password,first_name= f_name,last_name= l_name)
                myuser.save()
                messages.success(request,'successfully')
                return redirect('login-page')
        else:
            messages.error(request, 'Passwords do not match')
            return redirect('register-page')
    return render(request,'register.html')



def logout(request):
    auth.logout(request)
    return redirect('login-page')