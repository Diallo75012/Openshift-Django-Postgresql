from django.urls import path, include
from . import views

app_name = 'users'

urlpatterns = [
    path('', views.report, name='report'),
    path('index', views.index, name='index'),
    path('registerUser', views.registerUser, name='registerUser'),
    path('loginuser', views.loginUser, name='loginuser'),
    path('logoutuser', views.logoutUser, name='logoutuser'),
    path('addinfo', views.addInfo, name='addinfo'),
    path('deleteinfo/<str:pk>', views.deleteInfo, name='deleteinfo'),
    path('updateinfo/<str:pk>', views.updateInfo, name='updateinfo'),
]
