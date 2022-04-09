import random
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.contrib.auth.models import auth,User
from sitemanager.models import Staf, Students, Teachers
from django.contrib.auth.decorators import login_required


@login_required(login_url='/manager/admin_login/')
def dashboard(request):
    if request.user.is_staff:
        teachers = Teachers.objects.all()
        students = Students.objects.all()
        staf = Staf.objects.all()
        context ={'teachers':teachers,'students':students,'staf':staf}
        return render(request,"admin_dashboard.html",context)
    return HttpResponse("You are not a authenticated user")

def admin_login(request):
    if request.method =='POST':
        user = auth.authenticate(
                    username=request.POST['username'], 
                    password=request.POST['password'])
        if user is not None:
            auth.login(request,user)
            return redirect('/manager')
        else:
            return HttpResponse('invalid username or password')
    return render(request,"admin_login.html")

def add_teacher(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        dpt = request.POST['dpt']
        subject = request.POST['subject']
        qualifications = request.POST['qualifications']
        phone = request.POST['phone']
        username = usernameGenerater(name)
        password = name + str(phone[:5])
        print(password)
        user = User.objects.create_user(username=username,first_name = name,last_name ='teacher', password=password,email=email)
        user.save()
        Teachers(
            user = user,
            Department = dpt,
            Subject = subject,
            Qualifications = qualifications,
            Phone_number = phone,
            Photo = request.FILES['image']
        ).save()
    page = 1
    return render(request,"form_add.html",{'page':page})

def add_student(request):
    page = 2
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        dpt = request.POST['dpt']
        dob = request.POST['dob']
        parent = request.POST['parent']
        phone = request.POST['phone']
        contact = request.POST['contact']
        username = usernameGenerater(name)
        password = name + str(phone[:5])
        user = User.objects.create_user(username=username,first_name = name,last_name ='student', password=password,email=email)
        user.save()
        Students(
            user = user,
            Department = dpt,
            DoB = dob,
            Parent_name = parent,
            Phone_number = phone,
            Contact_number =contact,
            Photo = request.FILES['photo']
        ).save()
    return render(request,"form_add.html",{'page':page})

def add_staf(request):
    page = 3
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        dutty = request.POST['dutty']
        phone = request.POST['phone']
        username = usernameGenerater(name)
        password = name + str(phone[:5])
        user = User.objects.create_user(username=username,first_name = name,last_name ='staf', password=password,email=email)
        user.save()
        Staf(
            user = user,
            Dutty = dutty,
            Phone_number = phone,
            Photo = request.FILES['photo']
        ).save()
    return render(request,"form_add.html",{'page':page})


def edit_teacher(request,u_id):
    data = Teachers.objects.get(pk = u_id)
    if request.method == "POST":
        data.Department = request.POST['dpt']
        data.Subject = request.POST['subject']
        data.Qualifications = request.POST['qualifications']
        data.Phone_number = request.POST['phone']
        try:
            data.Photo = request.FILES['image']
        except:
            pass
        data.save()
        data.user.first_name = request.POST['name']
        data.user.email = request.POST['email']
        data.user.save()

        return redirect('/manager')
    page = 1
    return render(request,"form_add.html",{'page':page,'data':data})

def edit_student(request,u_id):
    data = Students.objects.get(pk = u_id)
    if request.method == "POST":
        data.Department = request.POST['dpt']
        data.Parent_name = request.POST['parent']
        data.Contact_number = request.POST['contact']
        data.Phone_number = request.POST['phone']
        try:
            data.Photo = request.FILES['photo']
        except:
            pass
        if request.POST['dob'] != '':
            data.DoB = request.POST['dob']
        data.save()
        data.user.first_name = request.POST['name']
        data.user.email = request.POST['email']
        data.user.save()
        return redirect('/manager')
    page = 2
    return render(request,"form_add.html",{'page':page,'data':data})

def edit_staf(request,u_id):
    data = Staf.objects.get(pk = u_id)
    if request.method == "POST":
        data.Dutty = request.POST['dutty']
        data.Phone_number = request.POST['phone']
        try:
            data.Photo = request.FILES['photo']
        except:
            pass
        data.save()
        data.user.first_name = request.POST['name']
        data.user.email = request.POST['email']
        data.user.save()
        return redirect('/manager')
    page = 3
    return render(request,"form_add.html",{'page':page,'data':data})

def usernameGenerater(name):
    while True:
        username = name + str(random.randint(10,10000))
        if User.objects.filter(username=username).exists():
            continue
        return username
