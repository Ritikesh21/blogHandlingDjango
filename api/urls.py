from django.urls import path, include
from .views import BlogListAll, BlogList, BlogDetail, UserList, UserDetail, UserRegistration
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path('blogs/', BlogList.as_view(), name='blog'),
    path('home/', BlogListAll.as_view()),
    path('blogs/<int:pk>/', BlogDetail.as_view()),
    path('users/', UserList.as_view()),
    path('users/register/', UserRegistration.as_view()),
    path('users/<int:pk>/', UserDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
urlpatterns += [
    path('api-auth/', include('rest_framework.urls')),
]