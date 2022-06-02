from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework import status

from .models import Entity
from .serializers import (
    EntitySerializer,
    EntityRetrieveSerializer,
    EntityUpdateSerializer,
)
from .permissions import HasApiKey


class EntityViewSet(ModelViewSet):
    model = Entity
    serializer_class = EntitySerializer
    queryset = Entity.objects.all()
    permission_classes = [
        HasApiKey,
    ]

    def get_serializer_class(self):
        if self.action == 'retrieve':
            return EntityRetrieveSerializer
        else:
            return EntitySerializer

    def list(self, request, *args, **kwargs):
        code = request.query_params.get('code')
        if code is None:
            return Response({'error': 'code is required'}, status=status.HTTP_400_BAD_REQUEST)

        if not Entity.objects.filter(code=code).exists():
            return Response(status=status.HTTP_404_NOT_FOUND)

        entities = Entity.objects.filter(
            code=code
        ).values(
            'name',
            'timezone',
        )

        return Response(entities, status=status.HTTP_200_OK)

    def put(self, request, *args, **kwargs):
        code = request.query_params.get('code')
        if code is None:
            return Response({'error': 'code is required'}, status=status.HTTP_400_BAD_REQUEST)
        serializer = EntityUpdateSerializer(data=request.data)
        if not serializer.is_valid():
            return Response({'error': 'invalid payload'}, status=status.HTTP_400_BAD_REQUEST)

        if not Entity.objects.filter(code=code).exists():
            return Response({'error': 'Entity with the code does not exist'}, status=status.HTTP_400_BAD_REQUEST)

        Entity.objects.filter(
            code=code
        ).update(
            name=serializer.validated_data['name'],
            supportEmail=serializer.validated_data['supportEmail'],
        )
        entities = Entity.objects.filter(
            code=code
        ).values(
            'name',
            'supportEmail',
        )
        return Response(entities, status=status.HTTP_200_OK)

    def delete(self, request, *args, **kwargs):
        code = request.query_params.get('code')
        if code is None:
            return Response({'error': 'code is required'}, status=status.HTTP_400_BAD_REQUEST)

        Entity.objects.filter(code=code).delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
