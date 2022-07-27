from django.urls import path
from . import views

urlpatterns = [
    path('addMessage/', views.addMessage, name='addMessage')
]