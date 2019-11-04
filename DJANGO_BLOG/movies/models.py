from django.db import models

class Movie(models.Model):
    title = models.CharField(max_length=100) # 영화명
    title_en = models.CharField(max_length=100) # 영화명(영문)
    audience = models.IntegerField() # 누적 관객수
    open_date = models.DateField() # 개봉일
    genre = models.CharField(max_length=100) # 장르
    watch_grade = models.CharField(max_length=100) # 관람등급
    score = models.FloatField() # 평점
    poster_url = models.TextField() # 포스터 이미지 URL
    description = models.TextField() # 영화 소개

    def __str__(self):
        return self.title
