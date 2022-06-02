from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter

from next_user.apis import EntityViewSet

router = DefaultRouter()
router.register('websites', EntityViewSet, basename='websites')

urlpatterns = [
    path('admin/', admin.site.urls),
]

urlpatterns = [
    path(r'nextuser-rest-api/api/', include(router.urls))
] + urlpatterns
