from django.urls import path
from .views import RegisterView, LoginView

urlpatterns = [
    # Ro'yxatdan o'tish
    path('api/v1/auth/register/', RegisterView.as_view(), name='register'),

    # Kirish
    path('api/v1/auth/login/', LoginView.as_view(), name='login'),
]
