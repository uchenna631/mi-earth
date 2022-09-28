from django.urls import path
from . import views


urlpatterns = [
    path('', views.profile, name='profile'),
    path('add_post/', views.add_post, name='add_post'),
    path('edit_profile/', views.edit_profile, name='edit_profile'),
    path('edit_post/<slug:slug>/', views.edit_post, name='edit_post'),
    path('delete_post/<slug:slug>/', views.delete_post, name='delete'),
]
