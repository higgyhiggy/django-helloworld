from django.http import HttpResponse

def index(request):
    return HttpResponse("webhook7 Hello, world!")
