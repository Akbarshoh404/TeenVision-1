from rest_framework import viewsets, mixins
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.parsers import MultiPartParser, FormParser
from django.contrib.auth import get_user_model

from core.permissions import IsAdminUserOnly, IsSuperAdmin, IsAdminOrReadOnly
from core.models import Major
from core.serializers import MajorSerializer, ProgramSerializer, CustomUserSerializer, AdminSerializer

User = get_user_model()


class UserViewSet(mixins.ListModelMixin,
                  mixins.DestroyModelMixin,
                  viewsets.GenericViewSet):
    queryset = User.objects.filter(is_staff=False, is_superuser=False)
    serializer_class = CustomUserSerializer
    permission_classes = [IsAuthenticated, IsAdminUserOnly]
    parser_classes = [MultiPartParser, FormParser]


class AdminViewSet(viewsets.ModelViewSet):
    queryset = User.objects.filter(is_staff=True)
    serializer_class = AdminSerializer
    permission_classes = [IsAuthenticated, IsSuperAdmin]
    parser_classes = [MultiPartParser, FormParser]

    def perform_create(self, serializer):
        serializer.save(is_staff=True)


class MajorViewSet(viewsets.ModelViewSet):
    queryset = Major.objects.all()
    serializer_class = MajorSerializer
    permission_classes = [IsAdminOrReadOnly]
    parser_classes = [MultiPartParser, FormParser]

    @action(detail=True, methods=['get'])
    def programs(self, request, pk=None):
        major = self.get_object()
        programs = major.program_set.all()  # Joriy Majorga tegishli barcha programlar
        serializer = ProgramSerializer(programs, many=True, context={'request': request})
        return Response(serializer.data)
