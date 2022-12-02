from .views import home, register, update, delete, profile
from django.urls import path

urlpatterns = [
    path('registration/', register, name='register'),
    path('home/', home, name='home'),
    path('update/<str:id>/', update, name='update'),
    path('delete/<str:id>/', delete, name='delete'),
    path('profile/<str:id>/', profile, name='profile')
]