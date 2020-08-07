from django.urls import path, include
from rest_framework.authtoken import views
from rest_framework.routers import DefaultRouter

from api import views as apiView

app_name = 'api'

router = DefaultRouter()
router.register('categories', apiView.CategoryViewSet)
router.register('tags', apiView.TagViewSet)
router.register('payment', apiView.PaymentViewSet)
router.register('transactions', apiView.TransactionViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('token/', views.obtain_auth_token)
]
