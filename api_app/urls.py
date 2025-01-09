from  django.urls import path

from api_app.controller import Controller
urlpatterns = [
    path('', Controller.get, name='index'),
]