from django.urls import path

from destinationapp import views

urlpatterns = [

    path('', views.destination, name='destination'),
]
