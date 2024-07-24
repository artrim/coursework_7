from django.urls import path
from rest_framework.permissions import AllowAny
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from users.apps import UsersConfig
from users.views import UserCreateAPIView, UserDestroyAPIView, UserUpdateAPIView, UserRetrieveAPIView, UserListAPIView

app_name = UsersConfig.name


urlpatterns = [
    path('register/', UserCreateAPIView.as_view(), name='register'),
    path('token/', TokenObtainPairView.as_view(permission_classes=(AllowAny,)), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(permission_classes=(AllowAny,)), name='token_refresh'),
    path("", UserListAPIView.as_view(), name="users_list"),
    path('<int:pk>/', UserRetrieveAPIView.as_view(), name="user_retrieve"),
    path('update/<int:pk>/', UserUpdateAPIView.as_view(), name="user_update"),
    path('destroy/<int:pk>/', UserDestroyAPIView.as_view(), name="user_destroy"),
]
