from django.urls import path
from Home import views

urlpatterns = [
    path('', views.index, name='home'),
    path('login/', views.login_page, name='login'),
    path('main/', views.main, name='main'),
    path('signup/', views.signup, name='signup'),
    path('<str:conversion_type>/', views.conversion_page, name='conversion'),
]
