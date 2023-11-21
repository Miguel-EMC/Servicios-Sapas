from django.urls import path, include
from rest_framework import routers
from apps.spas import views

router = routers.SimpleRouter()
router.register('', views.SpasView)

urlpatterns = router.urls
