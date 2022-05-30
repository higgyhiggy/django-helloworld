from django.http import HttpResponse

def index(request):
    return HttpResponse("webhook1 Hello, world!")
