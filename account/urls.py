from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken import views
from .views import AccountViewSet

# create router
router = DefaultRouter()
router.register(r'accounts', AccountViewSet, basename='account')

urlpatterns = [
    path('', include(router.urls)),
    path('auth/', views.obtain_auth_token),
]
