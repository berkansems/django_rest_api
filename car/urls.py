from django.urls import path

from car import views

urlpatterns= [
    path('personview/',views.personView),
    path('carview/',views.carView)
]