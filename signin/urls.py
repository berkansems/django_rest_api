from django.urls import path

from signin import views

urlpatterns=[
    path('new/',views.create_user),
    path('profile/',views.profile)
]