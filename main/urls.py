from django.urls import path
from .views import *

urlpatterns = [
    path('', HomePage.as_view(), name='home'),
    path('about-us/', AboutUs.as_view(), name= 'about-us'),
    path('services/', Services.as_view(), name='services'),
    path('media/', Gallery.as_view(), name='media'),
    path('contact-us/', ContactUs, name='contact-us')
   
]
