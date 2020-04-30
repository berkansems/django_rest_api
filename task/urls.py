from django.urls import path

from task import views

urlpatterns =[
    path('hello-world/',views.hello_world),
    path("hello/",views.hello),
    path("calculator/",views.calculator),
    path("newcalculator/",views.newcalculator)

]