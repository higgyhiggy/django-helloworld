from django.http import HttpResponse

def index(request):
    return HttpResponse("webhook23 Hello, world!")
