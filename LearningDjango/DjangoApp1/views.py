from django.shortcuts import render
from datetime import datetime

# Create your views here.
from django.shortcuts import render
from django.http import HttpResponse

# defines web pages here
def index(request):
    # create variable now and set it to the current time
    now = datetime.now()

    # render helper provides a simplified interface for working with page templates.
    return render(
        request,
        "DjangoApp1/index.html",  # Relative path from the 'templates' folder to the template file
        # "index.html", # Use this code for VS 2017 15.7 and earlier
        {
            'title' : "Hello Django",
            'message' : "Hello Django!",
            'content' : " on " + now.strftime("%A, %d %B, %Y at %X")
        }
    )

def about(request):
    return render(
        request,
        "DjangoApp1/about.html",
        {
            'title' : "About HelloDjangoApp",
            'content' : "Example app page for Django."
        }
    )