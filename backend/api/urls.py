from django.urls import path

from . import views
from rest_framework_simplejwt.views import (
    TokenRefreshView,
)

urlpatterns = [
    path("", views.getRoutes),
    path('token/', views.MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('register/', views.RegisterView.as_view(), name='auth_register'),
    path('test/', views.testEndPoint, name='test'),
    path("notes/", views.getNotes),
    path("note/create/", views.createNote),
    path("note/<str:pk>/update/", views.updateNote),
    path("note/<str:pk>/delete/", views.deleteNote),
    path("note/<str:pk>/", views.getNote),
]
