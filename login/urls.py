from django.urls import path,include
from login import views


app_name = 'login'

urlpatterns = [
    path('', views.user_login, name='user_login'),
    path('logout/',views.user_logout,name='logout')
]