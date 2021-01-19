
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User, auth
from backend.forms import EmployeeForm  
from backend.models import Employee  

# Create your views here.


def index(request):
    return render(request, 'index.html')

def register(request):
    return render(request,'register.html')
   
def register_submission(request):
    if request.method == "POST":  
        form = EmployeeForm(request.POST)  
        if form.is_valid():  
            try:  
                form.save()  
                return redirect('index')  
            except:  
                pass  
    else:  
        form = EmployeeForm()  
    return render(request,'register.html',{'form':form})


def about(request):

    return render(request,'about.html')   



def contact(request):

    return render(request,'contact.html') 



def mentors(request):

    return render(request,'mentors.html')     
    
    
def login(request):

    return render(request,'login.html')     