from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='blog-index'),
    path('detail/<int:pk>/', views.detail, name='blog-details'),
    path('edit/<int:pk>/', views.edit_post, name='edit-blog'),
    path('delete/<int:pk>/', views.delete_post, name='delete_blog'),
]