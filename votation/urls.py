from django.urls import path, include
from . import views
urlpatterns = [
    path('', views.login, name="login"),
    path('vote', views.vote, name="vote"),
    path('realTime', views.realTime, name="realTime"),
    path('logout', views.logout, name="logout"),
    path('requestUpdate', views.requestUpdate, name="requestUpate"),
    path('saveVote', views.saveVote, name="vote"),
    path('registerUser', views.registerUser, name="registerUser")
]
