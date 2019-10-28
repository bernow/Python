from django.shortcuts import render, HttpResponse
import random

def index(request):
    #return HttpResponse('Welcome to Django')
    return render(request, 'index.html')

def hola(request):
    #return HttpResponse('Hello, my name is hong')
    return render(request, 'hola.html')

def dinner(request):
    menus = ['피자','치킨','족발','라면']
    dinner = random.choice(menus)
    return HttpResponse(f'오늘의 저녁메뉴는 {dinner}입니다.')

def lotto(request):
    numbers = range(1,46)
    my_lotto = sorted(random.sample(numbers, 6)) #sorted는 오름차순이다.
    return HttpResponse(f'오늘의 로또 추천번호는 {my_lotto}입니다.') 