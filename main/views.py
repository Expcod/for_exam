from django.shortcuts import render,redirect
from django.http import HttpResponse
from . import models

def index(request):

    service = models.Services.objects.all()
    contact = models.Contact.objects.all()
    technicians = models.Technicians.objects.all()
    comments = models.Comments.objects.all()

    context ={
        'service':service,
        'contact':contact,
        'technicians':technicians,
        'comments':comments            
    }
    return render(request,'index.html',context)

def contact(request):
    if request.method == 'POST':
        models.Contact.objects.create(
            name = request.POST['name'],
            email = request.POST['email'],
            phone = request.POST['phone'],
            message = request.POST['message']
        )
        return redirect('index')
    return render(request,'contact.html')

def about(request):
    return render(request,'about.html')

def service(request):
    return render(request,'service.html')
 