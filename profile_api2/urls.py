




from django.urls import path
from django.urls.conf import include
from rest_framework.routers import DefaultRouter

from . import views

router = DefaultRouter()
router.register('hello-viewset', views.HelloViewSet, basename='hello-viewset')

urlpatterns = [
    path('apiview', views.HelloApiView.as_view(), name='apiview'),
    path('', include(router.urls)),
]
