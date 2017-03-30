from django.http import HttpResponse

# Create your views here.


def index(request):
    return HttpResponse('Hey there partner! Welcome to Rango. <a href="about/">About</a>')


def about(request):
    return HttpResponse('Rango says here is the about page. <a href="/rango/">Go back</a>')
