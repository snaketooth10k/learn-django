from django.http import HttpResponse

# Create your views here.


def index(request):
    return HttpResponse('Hey there partner! Welcome to Rango.')
