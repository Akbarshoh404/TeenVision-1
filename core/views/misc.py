from rest_framework import viewsets
from rest_framework.permissions import IsAdminUser
from core.models import Major
from core.serializers import MajorSerializer


class MajorViewSet(viewsets.ModelViewSet):
    queryset = Major.objects.all()
    serializer_class = MajorSerializer
    permission_classes = [IsAdminUser]