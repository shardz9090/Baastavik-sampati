from django.http import HttpResponse
from django.shortcuts import render
from team.models import team
from django.views.decorators.csrf import csrf_exempt
from django.conf import settings
import joblib
import pandas as pd
import os
from django.conf import settings
from sklearn.preprocessing import OneHotEncoder
import numpy as np
from sklearn.preprocessing import LabelEncoder

dataset = pd.read_csv("houseprice/latlong.csv")

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


@csrf_exempt
def predict(request):
    address_values = sorted(dataset['Address'].unique())
    context = {'address_values': address_values}
    return render(request, "predict.html", context)
    
    # if request.method == 'POST':
    #     # Load the trained model
    #     model_path = os.path.join(settings.BASE_DIR, 'houseprice/random_forest.joblib')
    #     model = joblib.load(model_path)
        
    #     # Get the form data
    #     land = float(request.POST.get('land'))
    #     floors = float(request.POST.get('floor'))
    #     road = int(request.POST.get('road'))
    #     bedrooms = int(request.POST.get('bed'))
    #     bathrooms = int(request.POST.get('bath'))
    #     facing = request.POST.get('face')
    #     address = request.POST.get('address')
        
    #     # Prepare the features for prediction
    #     features = pd.DataFrame([[floors, bathrooms, bedrooms, land, road, facing, address]],
    #                             columns=['Floor', 'Bathroom', 'Bedroom', 'Land', 'Road', 'Face', 'Address'])
        
    #     # Load the encoded features used during model training
    #     X_encoded = pd.read_csv('houseprice/latlong.csv')
        
    #     # Convert categorical variable 'Address' to numerical using one-hot encoding
    #     X_encoded = pd.get_dummies(X_encoded, columns=['Address'])
        
    #     # Ensure all required columns are present in X_encoded
    #     required_columns = ['Floor', 'Bathroom', 'Bedroom', 'Land', 'Road', 'Face']
    #     for column in required_columns:
    #         if column not in X_encoded.columns:
    #             X_encoded[column] = 0
        
    #     # Label encode the 'Face' column
    #     label_encoder = LabelEncoder()
    #     X_encoded['Face'] = label_encoder.fit_transform(X_encoded['Face'])
        
    #     # Add the missing address columns to X_encoded
    #     encoded_address_columns = pd.get_dummies(X_encoded['Address'])
    #     missing_address_columns = set(features['Address']) - set(encoded_address_columns.columns)
    #     for column in missing_address_columns:
    #         encoded_address_columns[column] = 0
    #     X_encoded = pd.concat([X_encoded, encoded_address_columns], axis=1)
        
    #     # Ensure the order of columns in X_encoded matches the order during training
    #     X_encoded = X_encoded[features.columns]
        
    #     # Make the prediction
    #     price = model.predict(features)
        
    #     return render(request, 'predict.html', {'price': price})

    # return render(request, 'predict.html')
