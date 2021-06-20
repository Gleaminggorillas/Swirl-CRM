from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home_page(request):
    context = {
        "name": "Joe",
        "age": 35,
    }
    return render(request, 'second_page.html', context)
