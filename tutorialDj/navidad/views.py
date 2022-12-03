from django.shortcuts import render
import datetime

# Create your views here.
def index(request):
    now = datetime.datetime.now()
    return render(request, "navidad/index.html", 
                  {"navidad":now.month == 12 and now.day ==1 })