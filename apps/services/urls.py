from django.urls import path, include
from rest_framework import routers
from apps.services import views

router = routers.SimpleRouter()
router.register('', views.ServicesView)

urlpatterns = router.urls
