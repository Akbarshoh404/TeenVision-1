from rest_framework import generics, status
from rest_framework.response import Response
from django.contrib.auth import get_user_model
from rest_framework_simplejwt.tokens import RefreshToken

from core.serializers import RegisterSerializer, LoginSerializer

User = get_user_model()


class RegisterView(generics.GenericAPIView):
    serializer_class = RegisterSerializer

    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True) # Validationlrni ishga tushuradi
        user = serializer.save() # yangi user yaratiladi
        return Response({
            "message": "Muvaffaqiyatli✅",
            "user": {
                "id": user.id,
                "full_name": f"{user.first_name} {user.last_name}",
                "email": user.email,
                "country": user.country
            }
        }, status=status.HTTP_201_CREATED)


class LoginView(generics.GenericAPIView):
    serializer_class = LoginSerializer

    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)  # Validationlrni ishga tushuradi

        user = serializer.validated_data['user']  # validate ichida user qaytgan

        # JWT token yaratamiz
        refresh = RefreshToken.for_user(user)
        return Response({
            "refresh": str(refresh),
            "access": str(refresh.access_token),
            "message": "Kirish muvaffaqiyatli bajarildi"
        }, status=status.HTTP_200_OK)
