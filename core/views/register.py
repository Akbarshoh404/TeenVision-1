from rest_framework.generics import UpdateAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework import status, generics
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.parsers import MultiPartParser, FormParser


from core.serializers import UserRegisterSerializer, UserLoginSerializer, UserProfileUpdateSerializer


class RegisterView(generics.GenericAPIView):
    serializer_class = UserRegisterSerializer
    parser_classes = [MultiPartParser, FormParser]

    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            refresh = RefreshToken.for_user(user)
            return Response({
                'refresh': str(refresh),
                'access': str(refresh.access_token),
                'message': "Ro'yxatdan o'tish muvaffaqiyatli yakunlandi",
                'user': {
                    'id': user.id,
                    'full_name': user.get_full_name(),
                    'email': user.email
                }
            }, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class LoginView(generics.GenericAPIView):
    serializer_class = UserLoginSerializer
    parser_classes = [MultiPartParser, FormParser]

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)  # Validationlrni ishga tushuradi

        user = serializer.validated_data['user']  # validate ichida user qaytgan

        # JWT token yaratamiz
        refresh = RefreshToken.for_user(user)
        access_token = refresh.access_token

        return Response({
            "refresh": str(refresh),
            "access": str(access_token),
            "message": "Kirish muvaffaqiyatli amalga oshirildi",
            "user": {
                "id": user.id,
                "full_name": user.get_full_name(),
                "email": user.email
            }
        }, status=status.HTTP_200_OK)


class UserProfileUpdateView(UpdateAPIView):
    serializer_class = UserProfileUpdateSerializer
    permission_classes = [IsAuthenticated]
    parser_classes = [MultiPartParser, FormParser]

    def get_object(self):
        return self.request.user
