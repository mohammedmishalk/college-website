from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib.auth.decorators import login_required
from sitemanager.models import Department, Gallery, Students, Syllabus, Teachers

from users.models import leaveRequest, notifications

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
    return render(request,'gallery.html',{'data':photos,"waiting":waiting})


def sylabus(request):
    try:
        data = Teachers.objects.get(user = request.user) 
    except:
        data = Students.objects.get(user = request.user)
    dep = Department.objects.get(id = data.Department)
    sylabus_obj = Syllabus.objects.get(dprt = dep.id)
    return render(request,'sylabus.html',{"data":sylabus_obj,"course":dep.course})


def timeTable(request):
    return render(request,'time-table.html')

def userLogin(request):
    if request.method == "POST":
        user = auth.authenticate(
            username=request.POST['username'], 
            password=request.POST['password'])
        if user is not None:
            auth.login(request,user)
            if user.is_superuser:
                return redirect('/manager/')
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

def leave_request(request):
    user = request.user
    if request.method == 'POST':
        leaveRequest(
            user = user,
            from_date = request.POST['from'],
            to_date = request.POST['to'],
            reason = request.POST['message']
        ).save()
    data = leaveRequest.objects.filter(user = user)
    return render(request,'leave-request.html',{'data':data})

def inBox(request):
    return render(request,"leave-accept.html")