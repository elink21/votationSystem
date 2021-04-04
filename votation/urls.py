from django.urls import path, include
from . import views
urlpatterns = [
    path('', views.login, name="index"),
    path('realTime', views.realTime, name="realTime")
]
