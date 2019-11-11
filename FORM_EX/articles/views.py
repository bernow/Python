from django.shortcuts import render, redirect, get_object_or_404
from .models import Article
from .forms import ArticleForm

def index(request):
    articles = Article.objects.all()
    return render(request, 'articles/index.html', {'articles':articles})

def create(request):
    if request.method == 'POST':
        form = ArticleForm(request.POST)
        if form.is_valid():
            title = form.cleaned_data.get('title')
            content = form.cleaned_data.get('content')
            article = Article.objects.create(title=title, content=content)
            return redirect('articles:index')
    else:
        form = ArticleForm()
    return render(request, 'articles/new.html',{'form':form})

def detail(request, article_pk):
    article = get_object_or_404(Article, pk=article_pk)
    return render(request, 'articles/detail.html', {'article':article})

def delete(request, article_pk):
    article = get_object_or_404(Article, pk=article_pk)
    if request.method == 'POST':
        article.delete()
        return redirect('articles:index')
    else:
        return redirect('articles:detail', article.pk)

def update(request, article_pk):
    article = get_object_or_404(Article, pk=article_pk)
    if request.method == 'POST':
        form = ArticleForm(request.POST)
        if form.is_valid():
            article.title = form.cleaned_data.get('title')
            article.content = form.cleaned_data.get('content')
            article.save()
            return redirect('articles:detail', article.pk)
    else:
        # ArticleForm 을 초기화(이전에 DB에 저장된 데이터 입력값을 넣어준 상태)
        form = ArticleForm(initial={'title':article.title, 'content':article.content}) # 방법 1
        # form = ArticleForm(initial=article.__dict__) # 딕셔너리 자료형이 되어 저장     # 방법 2
    return render(request, 'articles/new.html', {'form':form})
