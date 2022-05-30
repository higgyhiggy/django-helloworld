from django.http import HttpResponse

def index(request):
    return HttpResponse("webhook4 Hello, world!")
