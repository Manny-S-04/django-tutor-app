"""tutoringWebsite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from tutor.views import index_view, reviews_view, callback_view, services_view , about_view, contactus_view, navbar


urlpatterns = [
    path('', index_view),
    path('admin/', admin.site.urls),
    path('index/', index_view),
    path('reviews/', reviews_view, name='reviews'),
    path('callbacks', callback_view, name='callbacks'),
    path('services/', services_view),
    path('about-us/', about_view, name='about-us'),
    path('aboutus/', about_view),
    path('contact-us/', contactus_view),
    path('contactus/', contactus_view),
    path('navbar/', navbar),
]