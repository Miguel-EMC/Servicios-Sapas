from django.urls import path, include
from rest_framework import routers
from apps.categories import views

router = routers.SimpleRouter()
router.register('', views.CategoriesView)

urlpatterns = router.urls
