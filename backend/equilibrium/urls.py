from django.contrib import admin
from django.conf.urls import include
from django.urls import path
from rest_framework import routers
from users.api.viewsets import UserViewSet


router = routers.DefaultRouter()
router.register(r'users', UserViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls')),
]