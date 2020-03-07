from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('coolWebsites/', views.coolWebsites, name='coolWebsites'),
    path('signup/', views.signup, name='signup'),
    path('new_user/', views.new_user, name='new_user'),
    path('login/', views.login, name='login')
]
