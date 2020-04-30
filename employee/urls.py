from django.urls import path

from employee import views

urlpatterns=[
    path('post-employee/',views.post_employe),
    path('get-employees/',views.get_employees),
    path('select/<str:pk>/',views.select),
    path('search/',views.search_employee)
]