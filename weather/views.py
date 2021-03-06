
import requests
from django.shortcuts import render, redirect
from .models import City
from .forms import CityForm

def index(request):
	url = 'http://api.openweathermap.org/data/2.5/weather?q={}&units=metric&APPID=53cc655a14666b4965050fe2d13ccc9d'
	
	err_msg = ''#
	message = ''# создаем переменную сообщения которое увидит пользователь
	message_class = ''# содержит css класс цвет соообщения

	if request.method == 'POST':
		form = CityForm(request.POST)

		if form.is_valid():
			new_city = form.cleaned_data['name']
			existing_city_count = City.objects.filter(name=new_city).count()#проверяем на при ввoде что город существует

			if existing_city_count == 0:
				r = requests.get(url.format(new_city)).json() #сообщение об ощибке при некорректном ввoде города с проверкой  API
				#print(r)# смотрим в ответ API & var 'cod' при отсутствии выдает 404, при наличии 200
				if r['cod'] == 200: 
					form.save()
				else:
					err_msg = 'Такого городане существует'	
						
			else:
				err_msg = 'Город уже введен ранее'# избежать повторного ввода существующего города

		#если ошибка существует надо вывести сообщение об ошибке
		if err_msg:
			message =err_msg
			message_class = 'is-danger'
		else:
			message = 'Город успешно добавлен' #иначе сообщение о том что город добавлен	
			message_class = 'is-sucess'

	#  print(err_msg)

	form = CityForm()

	cities = City.objects.all()

	weather_data = []

	for city in cities:

		r = requests.get(url.format(city)).json() 
		
		city_weather = {
			'city' : city.name,
			'temperature' : r['main']['temp'],
			'description' : r['weather'][0]['description'],
			'icon' : r['weather'][0]['icon'],
		}	
		
		weather_data.append(city_weather)

		

	context = {'weather_data' : weather_data, 
	'form' : form,
	'message' : message,
	'message_class' : message_class
	}

	return render(request, 'weather/weather.html', context)

#функция для даления города
def delete_city(request, city_name):
	City.objects.get(name=city_name).delete()

	return redirect('home')	#завязываем на  urls.py & weather html