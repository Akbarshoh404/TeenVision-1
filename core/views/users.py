from rest_framework import viewsets
from django.contrib.auth import get_user_model
from core.serializers import CustomUserSerializer
from core.permissions import IsAdminOrSuperuser
from rest_framework.permissions import IsAuthenticated

User = get_user_model()


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = CustomUserSerializer
    permission_classes = [IsAuthenticated, IsAdminOrSuperuser]
