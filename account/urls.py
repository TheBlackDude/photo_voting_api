from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import AccountViewSet

# create router
router = DefaultRouter()
router.register(r'accounts', AccountViewSet, basename='account')

urlpatterns = [
    path('', include(router.urls)),
    path('auth/', include('rest_auth.urls')),
]
