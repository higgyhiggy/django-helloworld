from django.http import HttpResponse

def index(request):
    return HttpResponse("webhook12 Hello, world!")
