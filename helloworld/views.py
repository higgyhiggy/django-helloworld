from django.http import HttpResponse

def index(request):
    return HttpResponse("webhook5 Hello, world!")
