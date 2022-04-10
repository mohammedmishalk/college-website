from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib.auth.decorators import login_required
from sitemanager.models import Gallery

from users.models import notifications

def home(request):
    return render(request,'home/index.html')

def gallery(request):
    if request.method == 'POST':
        data = Gallery(user = request.user,
        Photo = request.FILES['photo'],
        disc = request.POST['disc'])
        if request.user.last_name == 'admin':
            data.accepted = True
        data.save()
    waiting = Gallery.objects.filter(user = request.user)
    photos = Gallery.objects.all().order_by('-created')
    return render(request,'home/gallery.html',{'data':photos,"waiting":waiting})

def admission(request):
    return render(request,'admission/admissin_login.html')

def admUserData(request):
    return render(request,'admission/admission.html')
def admUserLogin(request):
    return render(request,'admission/login-form.html')



def userLogin(request):
    if request.method == "POST":
        user = auth.authenticate(
            username=request.POST['username'], 
            password=request.POST['password'])
        if user is not None:
            auth.login(request,user)
            return redirect("/user/")
        else:
            msg = 'invalid username or password'
            return HttpResponse(msg)
    return render(request,'login-form.html')

@login_required(login_url='/user/login/')
def dashboard(request):
    if request.user.last_name == 'teacher':
        return render(request,'teacher-dashboard.html')
    elif request.user.last_name == 'student':
        return render(request,'student-dashboard.html')
    return render(request,'dashboard.html')

def userLogout(request):
    auth.logout(request)
    return redirect('/')


def sendNotification(request):
    user = request.user
    if request.method == 'POST':
        if user.last_name == "teacher" or user.last_name == "admin":
            notifications(
                user = user,
                header = request.POST['title'],
                content = request.POST['message'],
                link = request.POST['ref']
            ).save()
    data = notifications.objects.all().order_by('-created')
    return render(request,'create-notifications.html',{'data':data})

def leaveRequest(request):
    return render(request,'leave-request.html')

def inBox(request):
    return render(request,"leave-accept.html")