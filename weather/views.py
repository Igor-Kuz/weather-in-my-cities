
import requests
from django.shortcuts import render, redirect
from .models import City
from .forms import CityForm


def index(request):
	url = 'http://api.openweathermap.org/data/2.5/weather?q={}&units=metric&lang=ru&APPID=53cc655a14666b4965050fe2d13ccc9d'

	err_msg = ''
	message = ''  # создаем переменную сообщения которое увидит пользователь
	message_class = ''  # содержит css класс цвет соообщения

	if request.method == 'POST':
		form = CityForm(request.POST)
		if form.is_valid():
			new_city = form.cleaned_data['name']
			existing_city_count = City.objects.filter(name=new_city).count()
			# проверяем на то что при ввoде что город существует
			if existing_city_count == 0:
				r = requests.get(url.format(new_city)).json()
				# print(r)# смотрим в ответ API & var 'cod' при отсутствии выдает 404, при наличии 200
				if r['cod'] == 200: 
					form.save()
				else:  # сообщение об ощибке при некорректном ввoде города с проверкой  API
					err_msg = 'Такого города не существует'
			else:
				err_msg = f'Город {new_city} уже был введен ранее'  # избежать повторного ввода существующего города

		#  если ошибка существует вывести сообщение об ошибке
		if err_msg:
			message = err_msg
			message_class = 'is-danger'
		else:
			message = 'Город успешно добавлен'
			message_class = 'is-success'

	form = CityForm()
	cities = City.objects.all()
	weather_data = []
	for city in cities:
		r = requests.get(url.format(city)).json()
		city_weather = {
			'city': city.name,
			'country_code': r['sys']['country'],
			'temperature': r['main']['temp'],
			'feels_like': r['main']['feels_like'],
			'description': r['weather'][0]['description'],
			'humidity': r['main']['humidity'],
			'pressure': r['main']['pressure'],
			'icon': r['weather'][0]['icon'],
			'main': r['weather'][0]['main'],
			'coord': r['coord']['lon'],
			'coordy': r['coord']['lat'],
			'wind': r['wind']['speed'],
			'direction': r['wind']['deg'],
			'visibility': r['visibility'],
			'clouds': r['clouds']['all'],
			}
		
		weather_data.append(city_weather)

	context = {
		'weather_data': weather_data,
		'form': form,
		'message': message,
		'message_class': message_class,
	}

	return render(request, 'weather/weather.html', context)


def delete_city(request, city_name):
	City.objects.get(name=city_name).delete()

	return redirect('home')