from django.shortcuts import render,redirect,get_object_or_404 
from django.contrib.auth.models import User,auth
from django.contrib import messages


def logout(request):
    auth.logout(request)
    return redirect("/")


def login(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        user=auth.authenticate(username=username,password=password)
        if user is not None and username=='admin':
            auth.login(request,user)
            return redirect("admin")
        elif user is not None:
            auth.login(request,user)
            return redirect("student_login")
        else:
            messages.info(request,'invalid credentials')
            return redirect("/")

    else:
        return render(request,'login.html')


def register(request):

    if request.method=='POST':
        e_name=request.POST['e_name']
        e_email=request.POST['e_email']
        com_name=request.POST['com_name']
        branch_name=request.POST['branch_name']
        com_loc=request.POST['com_loc']
        dep_name=request.POST['dep_name']
        dep_loc=request.POST['dep_loc']
        if Employee.objects.filter(e_email=e_email).exists():
            messages.info(request,'email taken')
            return redirect('register')
        else:
            user=Employee.objects.create(e_name=e_name,e_email=e_email,com_name=com_name,branch_name=branch_name,com_loc=com_loc,dep_name=dep_name,dep_loc=dep_loc)
            user.save()
            print("user created")
            return redirect("admin")
        return redirect('/')
    
    
    else:
        return render(request,'register.html')
    
def admin(request):
    query_results = User.objects.all()
    return render(request,"admin.html",{'query_results':query_results})
  
def MyView(request):
    query_results = User.objects.all()
    return render(request,"admin.html",{'query_results':query_results})

def delete(request, pk):
    User.objects.filter(id=pk).delete()
    MyView(request)
    return redirect('admin')

def register_stud(request):
    if request.method=='POST':
        first_name=request.POST['first_name']
        username=request.POST['username']
        password=request.POST['password']
        email=request.POST['email']
        if User.objects.filter(email=email).exists():
            messages.info(request,'email taken')
            return redirect('register_stud')
        else:
            user=User.objects.create_user(first_name=first_name,username=username,password=password,email=email)
            user.save()
            print("user created")
            return redirect("/")    
    else:
        return render(request,'register_stud.html')
    

def student_login(request):
    query_results = User.objects.all()
    return render(request,"student_login.html",{'query_results':query_results})
  
def index(request):
    return render(request,'index.html')


