# Today I Learned

## [D01] 191021 INTRO
- 해피해킹 소개
- 교육 일정 안내
- Python remind

## [D02] 191022



## [D04] 191024

### 가상환경 설정

```bash 
$ python -m venv venv # 가상환경 파일 만들기
$ source ./venv/Scripts/activate # 가상환경 실행
$ python -m pip install --upgrade pip # (업그레이드)
```

### FLASK 실행

```bash
$ FLASK_APP=(파일이름) flask run
```

### webHook

```bash
$./ngrok http 5000 # webhook url확인 방법 (터미널)

#1. webhook을 통해 telegram에 보낸 요청 안에 있는 메시지를 가져와서 그대로 전송 (소스)
url = f'{base}/bot{token}/setWebhook?url=https://0660d15b.ngrok.io/{token}'
```



## [장고(Django)]

1. django 의 성격

   - 다소 독선적(Opinionated)
   - django 실행

   ````bash
   $ python manage.py runserver
   ````

   

2. for문 활용법

   - {% for 변수 in 변수 %} -> 기본 for문 사용법 (끝에 {% endfor %} 써줘야함)

3. urls.py

   ```bas
   path('match/', views.match) 
   #앞에는 url주소, 뒤에는 views의 값
   ```

   



## [D05] 191028

1. 프로젝트 만드는 법

   ```bash
   $django-admin startproject '이름'
   ```

   

2. app 만드는법

   ```bash
   $django-admin startapp '이름'
   ```

3.  