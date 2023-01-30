import os
from django.db import models
from django.conf import settings
from django.contrib.auth.models import User
from rword.models import SentenceList

class Board(models.Model):
    title = models.CharField(max_length=64, verbose_name='글 제목')
    contents = models.TextField(verbose_name='글 내용')
    writer = models.ForeignKey(User, verbose_name='작성자', on_delete=models.CASCADE)
    sentence = models.ForeignKey(SentenceList, models.DO_NOTHING, max_length=64, verbose_name='문장', default="")
    write_dttm = models.DateTimeField(auto_now_add=True, verbose_name='글 작성일')

    board_name = models.CharField(max_length=32, default='Public', verbose_name='게시판 종류')
    update_dttm = models.DateTimeField(auto_now=True, verbose_name='최종 수정일')
    hits = models.PositiveIntegerField(default=0, verbose_name='조회수')

    image = models.ImageField(blank=True, null=True, default='Images/favicon.png', verbose_name='썸네일 이미지', upload_to = "Images/") 
    file = models.FileField(blank=True, null=True, verbose_name='첨부 파일', upload_to = "Files")

    like_users = models.ManyToManyField(settings.AUTH_USER_MODEL, blank=True, related_name='like_borads')

    def __str__(self):
        return self.title
    
    class Meta:
        db_table = 'board'
        verbose_name = '게시판'
        verbose_name_plural = '게시판'

    @property
    def total_likes(self):
        return self.like_users.count() #like_users 컬럼의 값의 갯수를 센다

    def delete(self, *args, **kargs):
        super(Board, self).delete(*args, **kargs)
        if self.image:
            if self.image != 'Images/favicon.png':
                os.remove(os.path.join(settings.MEDIA_ROOT, self.image.path))
        if self.file:  
            os.remove(os.path.join(settings.MEDIA_ROOT, self.file.path))


class BoardLikeUsers(models.Model):
    id = models.BigAutoField(primary_key=True)
    board = models.ForeignKey(Board, models.DO_NOTHING)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'board_like_users'
        unique_together = (('board', 'user'),)

class Comment(models.Model):
    board = models.ForeignKey(Board, on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    content = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.content