from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView
from .views import register, login, logout

urlpatterns = [
    path('register/', register),
    path('login/', login),
    path('refresh/', TokenRefreshView.as_view()),
    path('logout/', logout),
]
