from django.urls import path, include
from rest_framework.routers import DefaultRouter

from api import views
print('here')
router = DefaultRouter()
router.register('categories', views.CategoryViewSet)
# router.register('test', views.test)

urlpatterns = [
    path('', include(router.urls)),
]
