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
$ code . #코드 실행
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




## [D06] 191029

1. static파일을 사용할려면 html소스에 {% load static %} 를 써줘야함.
2. {{% extends 'utilities/base,html' %}} -> base.html을 가져와서 사용하겠다



## [D07] 191030

### DataBase

1. 데이터베이스는 체계화된 데이터의 집합이다.
2. RDBMS(관계혀데이터베이스 관리 시스템)
   - 관계형 기반으로하는 데이터베이스 관리시스템
     - 오라클
     - 마이SQL
     - SQLite
3. 스키마(scheme)
   - 데이터베이스에서 자료의 구조, 표현방법, 관계등을 정의한 구조
     - PK = ID : 각 행의  고유값으로 Primary Key로 불린다. 반드시 설정해야하며 데이터베이스 관리 및    관계 설정시 주요하게 활용
4. SQL
   - 관계형 데이터베이스 관리시스템(RDBMS)의 데이터를 관리하기 위한 프로그래밍 언어



#### ORM(Object-relational mapping)

1. 객체와 관계와의 설정

   - 장점 
     - 재사용 및 유지보수의 편리성이 증가한다
     - 객체 지향적인 코드로 인해 더 직관적이고 비즈니스 로직에 더 집중할 수 있게 도와준다
     - DBMS에 대한 종속성이 줄어든다
   - 단점 
     - 완벽한 ORM 으로만 서비스를 구현하기가 어렵다
     - 프로시저가 많은 시스템에선 ORM의 객체 지향적인 장점을 활용하기 어렵다
     - 프로시저란? -> 특정 작업을 수행 하는, 이름이 있는 PL/SQL BLOCK 이다

2. migrations

   - 관련 명령어

   ````bash
   $ python manage.py makemigrations # migration 파일 생성
   $ python manage.py migrate # migration 적용(DB에 반영하기)
   ````



3. shell

   - shell로 모델 조작하기

     ```bash
     $ python manage.py shell # shell 실행
     >>> from articles(만든app이름).models import Article # shell과 연결 후 작성
     >>> Article.objects.all() # 모든 데이터를 확인(QuerySet으로 확인)
     ```

   - 데이터 import방법

     ```bash
     # 방법 1
     >>> article = Article()
     >>> article.title = 'first'
     >>> article.content = 'django'
     >>> article.save()
     
     # 방법 2
     >>> article = Article(title='second', content='edition')
     >>> article
     >>> article.save()
     
     # 방법 3 (save 할 필요가 없다.)
     >>> Article.objects.create(title='third', content='eye')
     
     # 세부내용 확인
     def __str__(self):
           return f'{self.id}번 글 - {self.title} : {self.content}' 작성해주고 
     >>> Article.objects.all()해주면 됨
     
     # 마지막 세이브한거에 대하여 값 확인
     >>> article.id # 마지막 저장한 id값이 나온다.
     >>> article.title # 마지막 저장한 title값
     ```

   - 데이터 특정값 확인하기

     ````bash
     # filter - title이 'first'인 데이터를 보여준다.
     >>> Article.objects.filter(title='first')
     # title이 'first'인 데이터중에서 첫번째 데이터를 보여준다.
     >>> Article.objects.filter(title='first').first()
     # get - pk가 1인 값을 보여준다.
     >>> Article.objects.get(pk=1)
     # get활용(특정값 수정)
     >>> article = Article.objects.get(pk=4)
     >>> article.title = '4th'
     >>> article.save() # 저장하면 pk가 4인 데이터의 title을 4th로 바꿔준다.
     ````

   - 유효성 검사

     ````bash
     $ 클래스변수명(article).full_clean()
     ````

   - 활용

     ```bash
     # 역순으로 뽑기
     >>> articles = Article.objects.order_by('-pk')
     >>> article #확인
     
     # 2번째 3번째 뽑아내기
     >>> articles = Article.objects.all()[1:3]
     >>> articles #확인
     
     # title에 'fir'이 들어가있는거 뽑아내기
     >>> articles = Article.objects.filter(title__contains='fir')
     >>> articles #확인
     
     # title에 f가 들어가 있는거 뽑기
     >>> articles = Article.objects.filter(title__startswith='f')
     >>> articles #확인
     ```

   - 지우기(delete)

     ```bash
     >>> article = Article.objects.get(pk=5)
     >>> article.delete()
     ```

4. 관리자 지정하기

   ```bash
   $ python manage.py createsuperuser #쓰고 아이디 지정하고 이메일은 안써도됨 비밀번호 치고 y
   ```

5. 관리자 설정

   - admin.py 파일을 생성한다.

   - 사이트 구조를 바꿀려면 아래 클래스 선언한다

     ````bash
     class ArticleAdmin(admin.ModelAdmin):
         list_display = ('pk', 'title', 'content', 'created_at', 'updated_at')
     
     admin.site.register(Article, ArticleAdmin)
     ````

6.  django-extensions(from import를 안해줘도됨)

````bash
# install해준다.
$ pip install django-extensions 
# settings에서 'django_extensions'를 INSTALLED_APPS에 추가해준다
# shell_plus로 가동
$ python manage.py shell_plus
````



## [D08] 191031

### HTTP

1. 기본 속성
   - Stateless : 상태정보가 저장되지 않음. 즉, 요청 사이에는 연결고리가 없음
   - Connectless : 서버에 요청을 하고 응답을 한 이후에 연결은 끊어짐
2. 응답 코드
   - 200 : 정상적으로 수행됨
   - 300 : 서버가 클라이언트를 다른 주소로 보냄
   - 400 : 서버가 요청을 받지 못하였음
   - 401 : 미승인(비인증)
   - 403 : 접근할 권리가 없음
3. Method
   - GET
   - POST
   - PUT/PATCH





## [D09] 191104

### 댓글 기능 

1. models.py(Comment클래스 추가)

   ````bash
   class Comment(models.Model):
       content = models.CharField(max_length=300) #댓글
       created_at = models.DateTimeField(auto_now_add=True) #댓글 생성 날짜
       article = models.ForeignKey(Article, on_delete=models.CASCADE)
       #article클래스 외래키 설정(연결시키는거)
   ````

2.  admin.py

   ```bash
   class CommentAdmin(admin.ModelAdmin):
       list_display = ('id','content','created_at','article_id')
   ```

3. shell

   ```bash
   # article을 pk에 맞게 불러온다
   article = Article.objects.get(pk=2)
   
   # comment를 만들어준다
   comment=Comment()
   
   # comment의 값을 넣어준다
   comment.content='first comment' -> 방법1
   comment = Comment(article=article, content='second comment') -> 방법2
   
   # comment에 article을 연결
   comment.article=article
   
   # comment의 맞는 article글 찾는 방법
   comment.article
   
   # article의 comment불러오기(comment는 여러개이므로 전체를 불러와야함)
   article.comment_set.all()
   ```

   

## [D10] 191105

1. 이미지 파일 넣기

```bash
# 이미지처리
$ pip install pillow

파일을 보낼려고 할 때 form태그에 enctype을 해줘야한다.
Ex) enctype="multipart/form-data"

# PIL, Pillow를 좀 더 쓰기 쉽도록 도와주는 라이브러리
$ pip install pilkit

# django를 안써주면 일반imagekit랑 2개가 install되서 충돌난다
$ pip install django-imagekit

```



## [D11] 191106

### FORM

1. 설정방법

   - 사용하는 app안에 forms.py 파일 생성

     ````bash
     from django import forms
     # class로 설정해준다.
     class ArticleForm(forms.Form):
         title = forms.CharField(max_length=100)
         content = forms.CharField()
     ````

2.  views.py에서 사용

   ```bash
   if request.method == 'POST':
           form = ArticleForm(request.POST) 
       # 사용자가 ArticleForm 으로 보낸 데이터를 받아서 form이라는 인스턴스를 생성
       # form의 type은 ArtilcleForm이라는 클래스의 인스턴스(request.POST는 QueryDict로 담긴다.)
           if form.is_valid(): # form이 유효한지 체크한다
               #form.cleaned_data 데이터를 요청받은대로 처리한다.
               title = form.cleaned_data.get('title')            
               content = form.cleaned_data.get('content')
               article = Article.objects.create(title=title, content=content)
               return redirect('articles:index')
       else:
           form = ArticleForm()
           #상황에 따라 context에 넘어가는 2가지 form
           # 1. GET : 기본 form 으로 넘겨짐
           # 2. POST : 검증에 실패(is_valid -> False)한 form(오류 메시지를 포함)상태로 넘겨준다
       return render(request, 'articles/new.html', {'form':form})
   ```

   

## [D12] 191111

### Model Form

- form 클래스를 상속받은 클래스 (forms.ModelForm)
- form 을 만들 때 model 클래스의 내역 그래도 form을 만든다면(Model Form) forms.py에서 form 필드를 중복해서 정의할 필요가 없다.
- 모델과 관련된 form 이라면 모델 폼을 사용하는 것이 좋다



1. Form 과 Model Form의 차이

   - Form(일반 폼) : 직접 필드 정의, 위젯 설정이 필요
   - Model Form (모델 폼) : 모델과 필드를 지정하면 모델폼이 자동으로 폼 필드를 생성

   ```bash
   # 일반 Form(위젯 설정까지)
    class ArticleForm(forms.Form):
        title = forms.CharField(
            max_length = 100,
            label = '제목',
            widget = forms.TextInput(
                attrs = {
                    'class' : 'my-title',
                    'placeholder' : 'Enter the title',
                }
            )
            )
        content = forms.CharField(
            label = '내용',
            widget = forms.Textarea(
                attrs={
                    'class' : 'my-content',
                   'placeholder' : 'Enter the content',
                    'rows' : 5,
                    'cols' : 50,
                }
            )
            )
            
   # Model Form
   class ArticleForm(forms.ModelForm):
       class Meta:
           model = Article
           fields =['title','content',]
   ```

   

2. ModelForm.save( )

   - Model From 클래스에는 .save( ) 메소드가 구현되어 있음

     ```bash
     # 사용예시
     def create(request):
         if request.method == 'POST':
             form = ArticleForm(request.POST) 
             if form.is_valid():
             #POST로 넘어온 값들을 form.save로 바로 저장한다.
             	article = form.save()
             	return redirect('articles:index')
         else:
             form = ArticleForm()
         return render(request, 'articles/form.html', {'form':form})
     ```

     

3.  ModelForm을 활용한 Model Instance 수정

   - 수정 대상이 되는 model instance를 Model Form 인스턴스 생성시에 instance 인자로서 지정한다.

   ```bash
   def update(request, article_pk):
       article = get_object_or_404(Article, pk=article_pk)
       if request.method == 'POST':
       	# instance=article은 기본적으로 적용되는 form에 값(형식)을 나타낸다.
           form = ArticleForm(request.POST, instance=article)
           if form.is_valid():
               article = form.save()
               # article.title = form.cleaned_data.get('title')
               # article.content = form.cleaned_data.get('content')
               # article.save()
               return redirect('articles:detail', article.pk)
       else:
           # ArticleForm 을 초기화(이전에 DB에 저장된 데이터 입력값을 넣어준 상태)
           form = ArticleForm(instance=article)
           # form = ArticleForm(initial='title':article.title,'content':article.content}) 
           # 방법 1
           # form = ArticleForm(initial=article.__dict__) # 딕셔너리 자료형이 되어 저장     # 방법 2
       return render(request, 'articles/form.html', {'form':form, 'article':article})
   ```

   