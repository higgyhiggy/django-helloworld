from django.http import HttpResponse

def index(request):
    return HttpResponse("webhook9 Hello, world!")
