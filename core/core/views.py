from django.http import HttpResponse

def home(request):
    print("Recibiendo request")
    print("Recibiendo request")
    return HttpResponse("Bienvenido a la API")