from django.http import HttpResponse

def index(request):
    return HttpResponse("webhook3 Hello, world!")
