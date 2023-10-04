from django.shortcuts import render
from django.http import HttpResponse
from app.models import Category, Page
from app.forms import CategoryForm, PageForm
from django.shortcuts import redirect, reverse


# Create your views here.


def index(request):
    return render(request, 'app/index.html')


def about(request):
    return render(request, 'app/about.html')


def contact(request):
    return render(request, 'app/contact.html')


def services(request):
    return render(request, 'app/services.html')

