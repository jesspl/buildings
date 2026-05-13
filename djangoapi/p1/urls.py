from django.urls import path, include
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r'calles', views.CallesModelViewSet)
router.register(r'semaforos', views.SemaforosModelViewSet)
router.register(r'manzanas', views.ManzanasModelViewSet)

urlpatterns = [
    path('', include(router.urls)),
]