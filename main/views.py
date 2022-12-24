from django.shortcuts import render
from django.views.generic import ListView
# Create your views here.
from .models import Samthafs
from django.core.mail import send_mail
from django.conf import settings


class HomePage(ListView):
    model = Samthafs
    template_name = 'home.html'

class AboutUs(ListView):
    model = Samthafs
    template_name = 'main/aboutus.html'

class Services(ListView):
    model = Samthafs
    template_name = 'main/services.html'
class Gallery(ListView):
    model = Samthafs
    template_name = 'main/gallery.html'


def ContactUs(request):
    if request.method == "POST":
        sender_name = request.POST['name']
        sender_email = request.POST['email']
        subject = request.POST['subject']
        phone_number = request.POST['phone']
        message = request.POST['message']

        send_mail(
            'Email From Website',
            f'From: {sender_name}! \n , Email:{sender_email} \n  Phone Number: {phone_number} \n Subject: {subject} \n Message: \n \n {message}',
            sender_email,
            ['samthafsprojects@gmail.com']
        )
        

        return render(request, 'main/contactus.html', {'Subject': subject })
    else:
        return render(request, 'main/contactus.html', {})
