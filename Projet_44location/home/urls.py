from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

app_name = 'home'

urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('about_us/', views.about_us, name='about_us'),
    path('contact_us/', views.contact_us, name='contact_us'),
    #path('forum/', views.forum, name='forum'),



    #path('javascript_test/', views.javascript_test, name='javascript_test'),
    #path('dom/', views.dom, name='dom'),
    #path('', views.espion, name='espion'),

]