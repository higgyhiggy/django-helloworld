from django.http import HttpResponse

def index(request):
    return HttpResponse("webhook26 Hello, world!")
