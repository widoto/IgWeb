from django.urls import path
from . import views
from board import views as view_board
from accounts import views as view_accounts

urlpatterns = [
    path('', views.rwordpage, name='rwordpage'),
    path('rboard/', views.rwordboard, name='rwordboard'),
    path('rboard/detail/<int:pk>', views.rword_detail, name='rword_detail'),
    path('rboard/search/', views.rwordboard_search, name='rwordboard_search'),
    #path('rboard/public/<int:pk>/write/', view_board.board_public_write, name='board_public_write'),
    #path('rboard/science/<int:pk>/write/', view_board.board_science_write, name='board_science_write'),
    #댓글
    path('rword/detail/<int:pk>/comments/', views.sen_comments_create, name='sen_comments_create'),
    path('<int:Sentence_pk>/comments/<int:comment_pk>/delete/', views.sen_comments_delete, name='sen_comments_delete'),
    #좋아요
    path('<int:pk>/likes/', views.likes, name='likes'),
    #로그인
    path('rboard/login/', view_accounts.login, name='login')
]