# from django.http import HttpResponse
from django.shortcuts import render
from rango.models import Category, Page

# Create your views here.


def index(request):
    category_list = Category.objects.order_by("-likes")[:5]
    page_list = Page.objects.order_by("-views")[:5]
    context_dict = {
        'categories': category_list,
        'pages': page_list
    }
    return render(request, 'rango/index.xhtml', context=context_dict)


def about(request):
    context_dict = {'author': 'William Reynolds'}
    return render(request, 'rango/about.xhtml', context=context_dict)

def show_category(request, category_slug):
    context_dict = {}
    try:
        category = Category.objects.get(slug=category_slug)
        pages = Page.objects.filter(category=category)
        context_dict['category'] = category
        context_dict['pages'] = pages

    except Category.DoesNotExist:
        context_dict['category'] = None
        context_dict['pages'] = None

    return render(request, 'rango/category.xhtml', context=context_dict)
