from django.shortcuts import render,redirect
from django.contrib.auth. models import User
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.views.decorators.cache import never_cache



# Create your views here.


# userHome page
@login_required(login_url='login-page')
@never_cache
def userHomePage(request):
    if request.user.is_superuser:
        return redirect('admin-home')
    user_obj= User.objects.get(username= request.user)
    print(user_obj.username)
    context= {'user':user_obj}
    return render(request,'userHome.html',context)



# adminHome page
@login_required(login_url='login-page')
@never_cache
def adminHomePage(request):
    if not request.user.is_superuser:
        return redirect('user-home')
    
    if request.method == 'POST':
        search= request.POST.get('search')
        user_obj= User.objects.filter(username__icontains= search,is_superuser= False)
        if user_obj:
            return render(request,'adminHome.html',{'user':user_obj})
        else:
            messages.error(request,'invalid users')
            return redirect('admin-home')
    else:
        users_obj= User.objects.filter(is_superuser=False)
        context= {'user':users_obj}
        return render(request,'adminHome.html',context)

        
        
    
    


# editing users
@login_required(login_url='login-page')
@never_cache
def edit(request,id):
    print('editttt')
    if not request.user.is_superuser:
        return redirect('user-home')
    try:

        user_obj= User.objects.get(id=id)
    except:
        return redirect('admin-home')
    
    if request.method=='POST':
        email=request.POST.get('email')
        f_name=request.POST.get('f_name')
        l_name=request.POST.get('l_name')
        user_obj.first_name= f_name
        user_obj.last_name= l_name
        user_obj.email= email
        user_obj.save()
        messages.success(request,'User updated successfully')
        return redirect('admin-home')
    return render(request,'edit.html',{'user':user_obj})


# adding users
@login_required(login_url='login-page')
@never_cache
def addUsers(request):
    if not request.user.is_superuser:
        return redirect('user-home')
    if request.method=='POST':
        username=request.POST.get('username1')
        email=request.POST.get('email')
        password1=request.POST.get('password')
        f_name=request.POST.get('f_name')
        l_name=request.POST.get('l_name')
        duplicate_user= User.objects.filter(username= username)
        if duplicate_user:
            messages.error(request,'this user is already taken')
            return redirect('add-users')
        else:
            User.objects.create_user(username=username,email=email,password=password1,first_name=f_name,last_name= l_name)
            messages.success(request,'User created successfully')
            return redirect('admin-home')
    return render(request,'add.html')


# deleting users
@login_required(login_url='login-page')
@never_cache
def deleteUser(request,id):
    print(id,'idddd')
    if not request.user.is_superuser:
        return redirect('user-home')
    User.objects.get(id=id).delete()
    messages.success(request,'user deleted')
    return redirect('admin-home')





def sampleView(request):
    context={'name':'rabeeh','age':22,'place':'kadalundi'}
    # context={'name':'rabeeh'}
    return render(request,'sample_view.html',context)