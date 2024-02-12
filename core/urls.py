from rest_framework_simplejwt.views import TokenRefreshView, TokenVerifyView, TokenObtainPairView
from core import views
from django.urls import path



urlpatterns = [
    # Autenticação
    path('token/obtain/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('login', views.LoginView.as_view()),
    # Rota de registro
    path('register', views.RegisterView.as_view()),
    # rotas relacionadas ao otp
    path('2f/generate', views.GenerateOTP.as_view()),
    path('2f/verify', views.VerifyOTP.as_view()),
    path('2f/validate', views.ValidateOTP.as_view()),
    path('2f/disable', views.DisableOTP.as_view()),
    # rota de perfil
    path('user/', views.UserDetailsAPIView.as_view(), name='user-details'),
]
