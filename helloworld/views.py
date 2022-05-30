from django.http import HttpResponse

def index(request):
    return HttpResponse("webhook6 Hello, world!")
