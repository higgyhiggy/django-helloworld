from django.http import HttpResponse

def index(request):
    return HttpResponse("webhook2 Hello, world!")
