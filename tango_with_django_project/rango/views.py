# from django.http import HttpResponse
from django.shortcuts import render
from rango.models import Category, Page

# Create your views here.


def index(request):
    category_list = Category.objects.order_by("-likes")[:5]
    context_dict = {'categories': category_list}
    return render(request, 'rango/index.xhtml', context=context_dict)


def about(request):
    context_dict = {'author': 'William Reynolds'}
    return render(request, 'rango/about.xhtml', context=context_dict)

def show_category(request, category_url):

