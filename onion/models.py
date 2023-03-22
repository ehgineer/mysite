from django.db import models

# Create your models here.

# 1. 회원 테이블
# 속성 : 아이디, 패스워드, 이름, 전화 번호, 지역
class User(models.Model):
    user_id = models.CharField(max_length=255, unique=True)
    user_pw = models.CharField(max_length=255)
    user_name = models.CharField(max_length=255)
    user_phone = models.CharField(max_length=255)
    user_area = models.CharField(max_length=255)   

# 2. 판매 글 쓰기 테이블
# 속성 : 아이디, 지역, 글 제목, 글 내용, 일시, 사진
class Sale(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    sale_title = models.CharField(max_length=255)
    sale_content = models.TextField()
    date = models.DateTimeField(null=True)
    image = models.ImageField(upload_to="")

# 3. 답변 글 쓰기 테이블
# 속성 : 아이디, 판매글의 질문 제목, 답변 내용, 일시, 
class Answer(models.Model):
    sale_title = models.ForeignKey(Sale, on_delete=models.CASCADE)
    answer_content = models.TextField()
    date = models.DateTimeField(null=True)
    