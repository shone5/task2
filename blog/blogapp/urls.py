from django.urls import path
from blogapp import views
from blogapp import views

urlpatterns = [
    path('home_page/', views.home_page, name='home_page'),
    path('', views.register_page, name='register_page'),
    path('login_page/', views.login_page, name='login_page'),
    path('register', views.register, name='register'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('reply_comment/', views.reply_comment, name='reply_comment'),
    path('create_post/', views.create_post, name='create_post'),

]
