from django.shortcuts import render
from faker import Faker
from .models import Past

def index(request):
    return render(request, 'pasts/index.html')

def past_life(request):
    name = request.POST.get('name')

    # DB에 이름이 있는지 확인
    person = Past.objects.filter(name=name).first()
    # filter를 사용하면 에러메시지가 안뜬다.
    # person = Past.objects.get(name=name)

    # DB에 이미 같은 name이 있으면 기존 name의 past_job을 가져오기,(레코드가 있으면 None이 아니니깐 True일 것입니다.)
    if person:
        past_job = person.past_job
    else:
        faker = Faker('ko-KR')
        past_job = faker.job()
        person = Past(name=name, past_job=past_job)
        person.save()
    return render(request, 'pasts/past_life.html', {'person':person})
