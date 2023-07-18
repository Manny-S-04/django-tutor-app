import json
from django.core.serializers.json import DjangoJSONEncoder
from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.core import serializers
from .forms import ReviewForm, CallBackForm
from .models import Review, CallBack



# Create your views here.


def index_view(request):
    context = {
    }
    return render(request, "home.html", context)


#######################################################
# REVIEWS
#######################################################
def reviews_view(request):
    reviews = Review.objects.all()
    reviews_ser = serializers.serialize('json', reviews)
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('reviews')
    else:
        form = ReviewForm()
        
    context = {
        'reviews': reviews,
        'reviews_ser' : reviews_ser,
        'form': form,
    }
    return render(request, 'reviews.html', context)



#######################################################
# REVIEWS
#######################################################

#######################################################
# CallBack
#######################################################

def callback_view(request):
    callback = CallBack.objects.all()
    form = CallBackForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('callbacks')

    context = {
        'callbackdata': callback,
        'form': form,
    }
    return render(request, 'callback.html', context)


#######################################################
# CallBack
#######################################################

def contactus_view(request):
    return render(request, 'contact-us.html')


def about_view(request):
    return render(request, 'aboutus.html')


def navbar(request):
    return render(request, 'navbar.html')

def maths_view(request):
    return render(request, 'maths.html')

def physics_view(request):
    return render(request, 'physics.html')

def test_view(request):
    callback = CallBack.objects.all()
    form = ReviewForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('test')

    context = {
        'form': form,
    }
    return render(request, 'test.html', context)