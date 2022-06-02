from django_filters import rest_framework as dj_filters

from .models import Entity


class EntityFilter(dj_filters.FilterSet):

    class Meta:
        model = Entity
        fields = (
            'code',
        )
