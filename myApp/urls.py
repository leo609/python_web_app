from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('sign-up/', views.sign_up, name='sign_up'),
    path('info/', views.info, name='info'),
    path('submit/', views.submit, name='submit')
]