from django.shortcuts import render
from django import forms
import requests

class cityForm(forms.Form):
    city = forms.CharField(label="",widget=forms.TextInput(attrs={
        'class':'form-control rounded',
        'placeholder':'City',
    }))

# https://mdbootstrap.com/docs/standard/extended/weather/#section-2
# https://www.weatherapi.com/docs/
def index(request):
    if request.method == "POST":
        form = cityForm(request.POST)
        if form.is_valid():
            city = form.cleaned_data["city"]
            key = "9450f7e9c3eb48aa81911555221006"
            URL = "https://api.weatherapi.com/v1/current.json?key="+ key +"&q=" + city
            x = requests.get(URL)
            data = x.json()
            print(data['location'])
            return render(request,'realtime/index.html',{
                "data":data,
                "form":cityForm()
            })

    return render(request,'realtime/index.html',{
        "data":None,
        "form":cityForm()
    })