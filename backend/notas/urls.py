from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('create/', views.create_nota, name='create_nota'),
    path('list/', views.notas_list, name='notas_list'),
    path('edit/<int:pk>/', views.edit_nota, name='edit_nota'),
    path('delete/<int:pk>/', views.delete_nota, name='delete_nota'),
    path('profile/<int:pk>/', views.profile, name='profile')
]
