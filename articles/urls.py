from django.urls import path
from . import views
# articles/___
urlpatterns = [
    path('create/', views.create),
    path('new/', views.new),
    path('index/', views.index),
]
