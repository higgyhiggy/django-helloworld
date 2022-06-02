from django.http import HttpResponse

def index(request):
    return HttpResponse("webhook25 Hello, world!")
