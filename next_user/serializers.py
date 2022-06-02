from rest_framework import serializers

from .models import Entity


class EntitySerializer(serializers.ModelSerializer):

    class Meta:
        model = Entity
        fields = '__all__'


class EntityRetrieveSerializer(serializers.ModelSerializer):

    class Meta:
        model = Entity
        fields = (
            'name',
        )


class EntityUpdateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Entity
        fields = (
            'name',
            'supportEmail',
        )
