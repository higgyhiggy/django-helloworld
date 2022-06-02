from django.http import HttpResponse

def index(request):
    return HttpResponse("webhook16 Hello, world!")
