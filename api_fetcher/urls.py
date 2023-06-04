from django.urls import path
from . import views

app_name = 'spam_checker'
urlpatterns = [
    path('', views.index, name="home"),
    path('inbox', views.inbox, name="inbox"),
    path('spam/', views.spam, name="spam"),
]
