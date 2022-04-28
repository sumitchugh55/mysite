from django.shortcuts import render,HttpResponse
from datetime import datetime
from polls.models import Contact

# Create your views here.
def index(request):
    return render(request,'index.html')
    
    #return HttpResponse("this is homepage.")

def about(request):
    return render(request,'About.html')
    
    # return HttpResponse("this is about page.")

def services(request):
    return render(request,'Services.html')
    # return HttpResponse("this is services page.")

def contact(request):
    if request.method =="POST":
        name=request.POST.get('name')
        email=request.POST.get('email')
        phone=request.POST.get('phone')
        desc=request.POST.get('desc')
        contact= Contact(name=name,email=email,phone=phone,desc=desc,date=datetime.today())
        contact.save()
    
    return render(request,'contact.html')
    # return HttpResponse("this is contact page.")