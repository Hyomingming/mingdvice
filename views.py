from django.shortcuts import render
from django.utils import timezone
from django.http import HttpResponse
from .models import Post
from pyowm import OWM
import serial

arduino = serial.Serial('COM4', 9600)

def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    n = weather('Seoul')  # weather 함수로 Seoul을 보냄
    y =  HttpResponse(n)
    if (n == 'Haze' or n == 'Clouds'): #yellow
        num = 1
        arduino.write(num)
    elif (n == 'Rain' or n == 'Snow'): #red
        num = 2
        arduino.write(num)
    elif (n == 'Clear'): #green
        num = 3
        arduino.write(num)
    return render(request, 'blog/post_list.html', {'posts': y})


def weather(city): #날씨 함수 (city = Seoul)
    API_key = '9f864162d2fc721e571f596e1b20a36d'
    owm = OWM(API_key)
    obs = owm.weather_at_place(city) #입력한 지역에 관련된 정보가 obs객체를 통해 반환됨
    w = obs.get_weather() #날씨 검색
    y = w.get_status() #간단하게 상태 가져옴 (자세한 상태를 알고 싶은 경우 w.get_detailed_status())
  #  print( '오늘의 날씨는?', y ) #Haze, Clouds, Clear, Rain, Snow
    return y

