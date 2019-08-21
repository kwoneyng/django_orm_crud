from django.db import models

class Article(models.Model):
    # id(pk)는 기본적으로 처음 테이블 생성시 자동으로 만들어 진다.
    # id = models.AutoField(primary_key=True)

    # CharField 에서는 max_length 가 필수 인자다.
    title = models.CharField(max_length=20) # 클래스 변수 (DB의 필드)
    content = models.TextField() # 클래스 변수 (DB의 필드)
    created_at = models.DateTimeField(auto_now_add=True)