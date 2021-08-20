




from django.urls import path
from django.urls.conf import include
from rest_framework.routers import DefaultRouter

from . import views

router = DefaultRouter()
router.register('hello-viewset', views.HelloViewSet, basename='hello-viewset')
router.register('user-profiles', views.UserProfilesViewSet, basename='user-profiles')

urlpatterns = [
    path('apiview', views.HelloApiView.as_view(), name='apiview'),
    path('login/', views.UserLoginApiView.as_view(), name='login'),
    path('', include(router.urls)),
]
