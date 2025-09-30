from django.http import HttpResponse

def hello_world(request):
    return HttpResponse("Hello,This is Django First Project!")  
