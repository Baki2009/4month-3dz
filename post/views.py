from django.shortcuts import render
from datetime import datetime

# Create your views here.

def time(request):
    current_time = datetime.now().strftime("%H:%M:%S")
    return render(request, 'time.html', {'current_time': current_time})

def portfolio(request):
    # Здесь вы можете добавить логику для отображения портфолио
    # Например, получение списка проектов из базы данных и передача их в шаблон
    projects = []  # Замените этот список реальными данными
    return render(request, 'portfolio.html', {'projects': projects})

