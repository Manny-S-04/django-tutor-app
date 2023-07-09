from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import ReviewForm, CallBackForm
from .models import Review, CallBack


# Create your views here.


def index_view(request):
    context = {
        "something": "somethings value",
        "listofreviews": ["review1", "review2", "review3"]
    }
    return render(request, "index.html", context)


#######################################################
# REVIEWS
#######################################################
def reviews_view(request):
    reviews = Review.objects.all()
    form = ReviewForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('reviews')  # Redirect back to the reviews page after form submission

    context = {
        'reviews': reviews,
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
        return redirect('callbacks')  # Redirect back to the reviews page after form submission

    context = {
        'callbackdata': callback,
        'form': form,
    }
    return render(request, 'request-a-callback.html', context)


#######################################################
# CallBack
#######################################################

def services_view(request):
    return render(request, 'services.html')


def contactus_view(request):
    return render(request, 'contact-us.html')


def about_view(request):
    return render(request, 'about.html')


def navbar(request):
    return render(request, 'navbar.html')
