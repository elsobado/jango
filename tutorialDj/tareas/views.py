from django.shortcuts import render

tasks= [ "foo", "bar","gonio"]
# Create your views here.
def index(request):
    return render(request, "tareas/index.html", {
        "tareas":tasks
    })