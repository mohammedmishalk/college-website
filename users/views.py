from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth

from users.models import notifications

# Create your views here.
def userLogin(request):
    if request.method == "POST":
        user = auth.authenticate(
            username=request.POST['username'], 
            password=request.POST['password'])
        if user is not None:
            auth.login(request,user)
            return HttpResponse("authenticatted")
        else:
            msg = 'invalid username or password'
            return HttpResponse(msg)

    return render(request,'login-form.html')

def dashboard(request):
    if request.user.last_name == 'teacher':
        return render(request,'teacher-dashboard.html')
    elif request.user.last_name == 'student':
        return render(request,'student-dashboard.html')
    return render(request,'dashboard.html')

def userLogout(request):
    auth.logout(request)
    return redirect('/user')


def sendNotification(request):
    user = request.user
    if request.method == 'POST':
        if user.last_name == "teacher":
            notifications(
                user = user,
                header = request.POST['title'],
                content = request.POST['message'],
                link = request.POST['ref']
            ).save()
    data = notifications.objects.all().order_by('-created')
    return render(request,'create-notifications.html',{'data':data})