from django.shortcuts import render
import requests

# Create your views here.

def home(request):

    city = request.POST.get('city', 'mumbai')
    print('CITY = ',city)

    if city == "":
        city = "delhi"
    

    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid=f75089673c70a8474b839d4e06ef575d"
    data = requests.get(url).json()
    

    payload = {

        'city' : data['name'],
        'weather':data['weather'][0]['main'],
        'icon':data['weather'][0]['icon'],
        'kelvin_temperature':data['main']['temp'],
        'celcius_temperature':int(data['main']['temp'] - 273),
        'pressure':data['main']['pressure'],
        'humidity':data['main']['humidity'],
        'description':data['weather'][0]['description'],
    }
   
    contex = {'data':payload}
    print(contex)
    return render(request,'home/home.html',contex)



def error_404_view(request,exception):
    return render(request,'home/404.html')

def handler500(request):
    return render(request,'home/base.html')

