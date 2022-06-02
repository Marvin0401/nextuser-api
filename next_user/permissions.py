from django.conf import settings
from rest_framework.permissions import BasePermission


class HasApiKey(BasePermission):

    def has_permission(self, request, view):
        if request.headers.get('Authorization') != settings.API_KEY:
            return False

        return True
