from django.urls import path
from rest_framework.routers import DefaultRouter
from car import views

router=DefaultRouter()
router.register('person',views.PersonViewSet)
router.register('car',views.CarViewSet)

urlpatterns= [
    #path('personview/',views.personView),
    path('carview/',views.carView)
]

urlpatterns += router.urls
