from django.shortcuts import render
from django.http import HttpResponse



# Create your views here.
def index(request):
    return HttpResponse("Hello User!!!")

# def greet(request, name):
#     return HttpResponse(f"Hello, {name.capitalize()}")

def greet (request, name):
    return HttpResponse(f"Hello, {name}")

def greet_html(request, name):
    return render(request, 'greet.html', {
        'name': name.capitalize()
    })

def index_page(request):
    return render(request, 'index.html')