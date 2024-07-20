from django.urls import path
from django.contrib import admin
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('admin/', admin.site.urls),
    path('about/', views.about,name='about'),
    path('login/', views.login, name='login'),
    path('register/', views.register, name='register'),
    path('footer/', views.footer, name='footer'),
    path('browse/',views.browse, name= 'browse'),
    path('recommend_books/',views.recommend_books, name = 'recommend_books'),
    path('genre_select/',views.genre, name = 'genre')

]