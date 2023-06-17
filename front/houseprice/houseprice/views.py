from django.http import HttpResponse
from django.shortcuts import render
from team.models import team

def home(request):
    teamdata = team.objects.all()
    data={
        'teamdata':teamdata
    }
    return render(request, "index.html",data)

def about(request):
    return render(request, "about.html")

def service(request):
    return render(request, "service.html")

def feature(request):
    return render(request, "feature.html")
def contact(request):
    return render(request, "contact.html")
def predict(request):
    return render(request, "predict.html")
def teams(request):
    teamdata = team.objects.all()
    data={
        'teamdata':teamdata
    }
    return render(request, "team.html", data)
