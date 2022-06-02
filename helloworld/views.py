from django.http import HttpResponse

def index(request):
    return HttpResponse("webhook18 Hello, world!")
