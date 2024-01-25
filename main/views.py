from django.shortcuts import render,redirect
from django.http import HttpResponse
from . import models

def index(request):

    services = models.Services.objects.all()
    contact = models.Contact.objects.all()
    technicians = models.Technicians.objects.all()
    comments = models.Comments.objects.all()
    booking = models.Booking.objects.all()

    if request.method == 'POST':
        models.Booking.objects.create(
            name = request.POST['name'],
            email = request.POST['email'],
            select = request.POST['select'],
            message = request.POST['message'],
            date = request.POST['date']
        )
        return redirect('index')
    
    context ={
        'services':services,
        'contact':contact,
        'technicians':technicians,
        'comments':comments,            
        'booking':booking            
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
    services = models.Services.objects.all()
    context ={
        'services':services
    }
    
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        select = request.POST['select']
        message = request.POST['message']
        date = request.POST['date']
        models.Booking.objects.create(
        name = name,
        email = email,
        select = select,
        message = message,
        date = date
        )
        
        
        return redirect('index')
    return render(request,'service.html',context)
