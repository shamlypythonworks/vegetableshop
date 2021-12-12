
from django.urls import path
from . import views
urlpatterns=[
    path('appointment/', views.appointment, name='appointment'),
    path('register/',views.register,name='registerdet'),
    path('login/',views.login,name='login'),
    path('logout/',views.logout,name='logout')
]