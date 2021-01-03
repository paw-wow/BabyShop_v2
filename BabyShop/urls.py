from django.urls import path
from .views import index, edit, delete

urlpatterns = [
    path('edit/<int:pk>/', edit, name='edit'),
    path('delete/<int:pk>/', delete, name='delete'),

    path('', index, name='index')
]
