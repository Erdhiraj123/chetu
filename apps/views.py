from django.http import HttpResponse
from django.shortcuts import render,HttpResponseRedirect, redirect
from . models import Users1
from apps . forms import *
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import Group




# Create your views here.

def show(request):
    if request.method=='POST':
        fm=StudentRegistration(request.POST)
        if fm.is_valid():
            nm=fm.cleaned_data['name']
            em=fm.cleaned_data['email']
            pp=fm.cleaned_data['password']
            print(request.user)
            reg=Users1(name=nm,email=em,password=pp,author = request.user)
            reg.save()
            fm=StudentRegistration()
    else:
        fm=StudentRegistration()
    if request.user.is_superuser:  # Check if the user is a superuser
        stud = User.objects.all()  # Show all users from the User model
        return render(request,"enroll/admin.html",{'form':fm,'stu':stud})
    if request.user.groups.filter(name='TM').exists():
        
        return render(request,'enroll/abc.html')
    else:
        stud = Users1.objects.filter(author=request.user) 
    return render(request,'enroll/addandshow.html',{'form':fm,'stu':stud})

#This Function will return Update data

def update(request,id):
    if request.method=='POST':
        pi=Users1.objects.get(pk=id)
        fm=StudentRegistration(request.POST, instance=pi)
        if fm.is_valid():
            fm.save()
    else:
        pi=Users1.objects.get(pk=id)
        fm=StudentRegistration(instance=pi)

    return render(request,'enroll/update.html',{'form':fm})

#This Will return Delete data

def deletedate(request,id):
    if request.method=='POST':
        pi=Users1.objects.get(pk=id)
        pi.delete()
        return HttpResponseRedirect('/')
    

# **************************************** User Registration ***********************************

def userregistration(request):
    if not request.user.is_authenticated:
        if request.method=='POST':
            fm=RegistrationForm(request.POST)
            if fm.is_valid():
            
                user=fm.save()
                user = fm.save()
                group = Group.objects.get(name='TR')
                user.groups.add(group)

                return HttpResponse("Registration submit")
            
        else:
            fm=RegistrationForm()
        return render(request,"enroll/registration.html",{'form':fm})

    else:
        return HttpResponseRedirect('details/')
    
# **************************************** FM Registration ***********************************

def flormregistration(request):
    if not request.user.is_authenticated:
        if request.method=='POST':
            fm=RegistrationForm(request.POST)
            if fm.is_valid():
            
                user=fm.save()
                group = Group.objects.get(name='FM')
                user.groups.add(group)

                return HttpResponse("Registration submit")
            
        else:
            fm=RegistrationForm()
        return render(request,"enroll/registration.html",{'form':fm})

    else:
        return render(request,"enroll/fm.html",{'form':fm})
    
# **************************************** TL Registration ***********************************

def teamleadregistration(request):
    if not request.user.is_authenticated:
        if request.method=='POST':
            fm=RegistrationForm(request.POST)
            if fm.is_valid():
            
                user=fm.save()
                group = Group.objects.get(name='TL')
                user.groups.add(group)

                return HttpResponse("Registration submit")
            
        else:
            fm=RegistrationForm()
        return render(request,"enroll/registration.html",{'form':fm})

    else:
        return HttpResponseRedirect('details/')
    
# **************************************** TM Registration ***********************************

def teammregistration(request):
    if not request.user.is_authenticated:
        if request.method=='POST':
            fm=RegistrationForm(request.POST)
            if fm.is_valid():
            
                user=fm.save()
                group = Group.objects.get(name='TM')
                user.groups.add(group)

                return HttpResponse("Registration submit")
            
        else:
            fm=RegistrationForm()
        return render(request,"enroll/registration.html",{'form':fm})

    else:
        return HttpResponseRedirect('details/')
    

# **************************************** Login ***********************************

def user_login(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            form=loginform(request=request, data=request.POST)
            if form.is_valid():
                uname = form.cleaned_data['username']
                upass = form.cleaned_data['password']
                user = authenticate(username=uname,password=upass)
                if user is not None:
                    login(request, user)
                    messages.success(request,'Login Successfull')
                    return redirect(show)
        else:
            form=loginform()
        return render(request,'enroll/login.html',{"form":form})
    else:
        return HttpResponseRedirect('details/')


# def dashboard(request):
#     if request.user.is_authenticated:
#         posts = Users1.objects.all()
#         user = request.user
#         full_name = user.get_full_name()
#         gps = user.groups.all()
#         return render(request,'dashboard.html',{"posts":posts,"fullname":full_name,"groups":gps})
#     else:
#         return redirect(user_login)

# **************************************** Logout ***********************************

def user_logout(request):
    logout(request)
    return HttpResponseRedirect('/login/')



# **************************************** Admin Delete ***********************************


def admindelete(request,id):
    if request.method=='POST':
        pi=User.objects.get(pk=id)
        pi.delete()
        return HttpResponseRedirect('/')
    

# **************************************** Admin Edit ***********************************


def adminupdate(request, id):
    if request.method == 'POST':
        user = User.objects.get(pk=id)
        fm = EditAdminUserProfileForm(request.POST, instance=user)
        if fm.is_valid():
            fm.save()
            messages.success(request,'Login Successfull')
            return redirect(show)
    else:
        user = User.objects.get(pk=id)
        fm = EditAdminUserProfileForm(instance=user)

    return render(request, 'enroll/update.html', {'form': fm})

