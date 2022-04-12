from django.shortcuts import render

from sitemanager.models import Gallery

# Create your views here.
def home(request):
    return render(request,'home/home.html')

def gallery(request):
    photos = Gallery.objects.all().order_by('-created')
    return render(request,'home/gallery.html',{'data':photos})

def about(request):
    return render(request,'home/about.html')

def messages(request):
    return render(request,'home/messages.html')

def staff(request):
    return render(request,'home/staff.html')

def management(request):
    return render(request,'home/management.html')

def courses(request,name):
    return render(request,f'home/courses/{name}.html')  

def facilitites(request):
    return render(request,'home/facilitites.html')

def contact(request):
    return render(request,'home/contact.html')

def instructions(request):
    return render(request,'home/instructions .html')
def admission(request):
    return render(request,'admission/admissin_login.html')

def admUserData(request):
    return render(request,'admission/admission.html')
def admUserLogin(request):
    return render(request,'admission/login-form.html')