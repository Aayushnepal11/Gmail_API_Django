from django.urls import path
from . import views

app_name = 'spam_checker'
urlpatterns = [
    path('', views.index, name="home"),
    path('spam/', views.spam, name="spam"),
    path('draft', views.draft, name="draft"),
]
