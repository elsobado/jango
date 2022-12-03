from   django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
def index(request):
    return render(request,"hola/index.html")

def potros(request):
    return HttpResponse("Hola, Ceroilo"
                        )
def greet(request,name):
 return HttpResponse(f"Hola,{name.capitalize()}! , Te han puyado el culo ahoyra??")
 return render(request,"hola/greet.html", {
     "name":name.capitalize()
 })
