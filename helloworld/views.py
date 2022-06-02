from django.http import HttpResponse

def index(request):
    return HttpResponse("webhook8 Hello, world!")
