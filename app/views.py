from django.shortcuts import render,redirect
from app.models import *
from django.http import HttpResponse

# Create your views here.
def IndexVw(request):
    if request.method=="POST":
        first_name=request.POST['fname']
        last_name=request.POST['lname']
        city=request.POST['city']
        email=request.POST['email']
        numer=request.POST['number']
        if Contact.objects.filter(email=email).exists():
            return HttpResponse('You are already registered')
        else:
            Contact.objects.create(first_name=first_name,last_name=last_name,city=city,email=email,number=numer)
            return HttpResponse('You are successfully registered')
    return render(request, 'index.html')


def AboutVw(request):
    return render(request, 'About.html')


def ServiceVw(request):
    return render(request, 'service.html')


def CarsVw(request):
    return render(request, 'cars.html')


def ContactVw(request):
    return render(request, 'Contact.html')


def LoginVw(request):
    if request.method=="POST":
            Registration_email=request.POST['lemail']
            Registration_password=request.POST['lpass']
            if Registration.objects.filter(Registration_email=Registration_email,Registration_password=Registration_password).exists():
               return redirect('../app1/Dash')
            else:
                return HttpResponse('Check Email Password.')
    return render(request, 'login.html')


def RegistrationVw(request):
    if request.method=="POST":
        Registration_First_Name=request.POST['rfname']
        Registration_Last_Name=request.POST['rlname']
        Registration_city=request.POST['rcity']
        Registration_email=request.POST['remail']
        Registration_number=request.POST['rnumber']
        Registration_password=request.POST['rpassword']
        Registration_confirm_password=request.POST['rcpassword']
        if Registration.objects.filter(Registration_email=Registration_email).exists():
            
            return HttpResponse("You Are Already Registered")
        else:
            Registration.objects.create(Registration_First_Name=Registration_First_Name,Registration_Last_Name=Registration_Last_Name,Registration_city=Registration_city,Registration_email=Registration_email,Registration_number=Registration_number,Registration_password=Registration_password,Registration_confirm_password=Registration_confirm_password)
            return HttpResponse("Registration Sucssesfull")
    return render(request, 'registration.html')