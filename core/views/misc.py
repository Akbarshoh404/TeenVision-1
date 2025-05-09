from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.permissions import IsAdminUser, IsAuthenticatedOrReadOnly
from rest_framework.response import Response

from core.models import Major
from core.serializers import MajorSerializer, ProgramSerializer


class MajorViewSet(viewsets.ModelViewSet):
    queryset = Major.objects.all()
    serializer_class = MajorSerializer
    permission_classes = [IsAdminUser | IsAuthenticatedOrReadOnly]

    @action(detail=True, methods=['get'])
    def programs(self, request, pk=None):
        major = self.get_object()
        programs = major.program_set.all()  # Joriy Majorga tegishli barcha programlar
        serializer = ProgramSerializer(programs, many=True, context={'request': request})
        return Response(serializer.data)
