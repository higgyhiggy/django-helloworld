from django.http import HttpResponse

def index(request):
    return HttpResponse("webhook10 Hello, world!")
