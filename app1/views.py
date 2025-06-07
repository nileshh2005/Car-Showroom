from django.shortcuts import render,redirect
from app.models import *

# Create your views here.
def DashVw(request):
    return render(request,'Dash.html')

def CntVw(request):
    cnt_data = Contact.objects.filter(status=True)
    return render(request, 'Cnt.html',{'cnt_data':cnt_data})

def Cnt_dltVw(request,id):
    cnt_data = Contact.objects.filter(id=id).update(status=False)
    return redirect('/app1/Cnt')

def Cnt_updtVw(request,id):
   cnt_data = Contact.objects.filter(id=id)
   if request.method == 'POST':
      first_name=request.POST['fname']
      last_name=request.POST['lname']
      city=request.POST['city']
      email=request.POST['email']
      numer=request.POST['number']
      Contact.objects.filter(id=id).update(first_name=first_name,last_name=last_name,city=city,email=email,number=numer)
      return redirect('/app1/Cnt')
   return render(request,'Cnt_updt.html',{'cnt_data':cnt_data})
