import os
import joblib
import numpy as np
from django.shortcuts import render

# Load the ML model once when the server starts
model_path = os.path.join(os.path.dirname(__file__), 'model.pkl')
model = joblib.load(model_path)

def index(request):
    return render(request, "home.html")

def predict_price(request):
    prediction = None

    if request.method == "POST":
        try:
            bedrooms = int(request.POST.get("bedrooms"))
            bathrooms = int(request.POST.get("bathrooms"))
            livingarea = int(request.POST.get("livingarea"))
            condition = int(request.POST.get("condition"))
            numberofschool = int(request.POST.get("numberofschool"))

            features = np.array([[bedrooms, bathrooms, livingarea, condition, numberofschool]])
            prediction = model.predict(features)[0]
        except Exception as e:
            prediction = f"Error in prediction: {str(e)}"

    return render(request, "predict.html", {"prediction": prediction})
def about(request):
    return render(request, "about.html")
