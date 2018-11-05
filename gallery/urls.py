from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ImageViewSet, ImageApiView, VoteApiView

router = DefaultRouter()
router.register(r'images', ImageViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('image/<int:pk>/', ImageApiView.as_view()),
    path('image/vote/<int:pk>/', VoteApiView.as_view()),
]
