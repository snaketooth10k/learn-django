from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.


def index(request):
    context_dict = {'bold_message': 'Here is a message from the view!'}
    return render(request, 'rango/index.xhtml', context=context_dict)


def about(request):
    return HttpResponse('Rango says here is the about page. <a href="/rango/">Go back</a>')
