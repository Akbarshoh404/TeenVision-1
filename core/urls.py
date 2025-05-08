from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import RegisterView, LoginView, UserViewSet, ProgramViewSet, MajorViewSet

router = DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'programs', ProgramViewSet)
router.register(r'majors', MajorViewSet)


urlpatterns = [
    path('', include(router.urls)),
    path('api/v1/auth/register/', RegisterView.as_view(), name='register'),     # Ro'yxatdan o'tish
    path('api/v1/auth/login/', LoginView.as_view(), name='login'),     # Kirish
]
