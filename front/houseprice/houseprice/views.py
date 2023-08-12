from django.http import HttpResponse
from django.shortcuts import render, redirect
from team.models import team
from django.views.decorators.csrf import csrf_exempt
from django.conf import settings
import pickle
import pandas as pd
import os
from django.conf import settings
import numpy as np
from sklearn.preprocessing import LabelEncoder,OneHotEncoder
from sklearn.compose import ColumnTransformer

dataset = pd.read_csv("houseprice/sorted_latlong.csv")
model_dataset = pd.read_csv("houseprice/latest1.csv")

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

def info(request):
    return render(request, "information.html")

def contact(request):
    return render(request, "contact.html")


@csrf_exempt
def predict(request):
    pipe = pickle.load(open("houseprice/best_rf_model.pkl", "rb"))
    addresses = sorted(model_dataset['Address'].unique())
    faces = sorted(model_dataset['Face'].unique())   
    context = {'addresses': addresses, 'faces': faces}
    if request.method == 'POST':
        land = float(request.POST.get('land'))
        floor = float(request.POST.get('floor'))
        road = int(request.POST.get('road'))
        bed = int(request.POST.get('bed'))
        bathroom = int(request.POST.get('bath'))
        face = request.POST.get('face')
        address = request.POST.get('address')

        input_data = pd.DataFrame([[floor, bathroom, bed, land, road, address, face]], 
                                  columns=['Floor', 'Bathroom', 'Bedroom', 'Land', 'Road', 'Address', 'Face'])
        pred_price = pipe.predict(input_data)[0]
        prediction_price = "{:.2f}".format(pred_price)
        
        data = {
            'land': land,
            'floor': floor,
            'road': road,
            'bed' : bed,
            'bath' : bathroom,
            'face' : face,
            'address' : address,
            'price' : prediction_price
        }
        return render(request, 'prediction.html', {'data' : data})
    else:
        return render(request, 'predict.html',context)
    
    

