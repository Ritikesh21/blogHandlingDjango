from django.urls import path
from .views import Home, AuthorRegistration, BlogCreate, BlogDetail, BlogUpdate, BlogDelete, CustomLoginView, AuthorBlog
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('', Home.as_view(), name='home'),
    path('profile/', AuthorBlog.as_view(), name='profile'),
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(next_page='home'), name='logout'),
    path('register/', AuthorRegistration.as_view(), name='register'),
    path('create/', BlogCreate.as_view(), name='create'),
    path('update/<int:pk>/', BlogUpdate.as_view(), name='update'),
    path('delete/<int:pk>/', BlogDelete.as_view(), name='delete'),
    path('detail/<int:pk>/', BlogDetail.as_view(), name='detail')
]