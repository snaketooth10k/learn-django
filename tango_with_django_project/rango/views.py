# from django.http import HttpResponse
from django.shortcuts import render
from rango.models import Category, Page
from rango.forms import CategoryForm, PageForm

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


def add_category(request):
    form = CategoryForm

    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
            return index(request)
        else:
            print(form.errors)

    return render(request, 'rango/add-category.xhtml', {'form': form})


def add_page(request, category_slug):

    try:
        category = Category.objects.get(slug=category_slug)
    except Category.DoesNotExist:
        category = None

    form = PageForm()
    if request.method == 'POST':
        form = PageForm(request.POST)
        if form.is_valid():
            if category:
                page = form.save(commit=False)
                page.category = category
                page.views = 0
                page.save()
                return show_category(request, category_slug)
        else:
            print(form.errors)

    context_dict = {'form': form, 'category': category}
    return render(request, 'rango/add-page.xhtml', context_dict)


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
