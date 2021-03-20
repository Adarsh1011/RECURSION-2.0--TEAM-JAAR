from blog.api import urls as api_url
from django.urls import path, include
from .views import (PostListView, PostDetailView, PostCreateView,PostUpdateView, PostDeleteView, CategoryView,PostListView2,PostDetailView2)
from . import views

urlpatterns = [
    
    path('', views.mainhome, name='main-home'),
    path('blogs/', PostListView.as_view(), name='blog-home'),
    path('post/<int:pk>/', PostDetailView, name='post-detail'),
    path('post/<int:pk>/update', PostUpdateView.as_view(), name='post-update'),
    path('post/new/', PostCreateView.as_view(), name='post-create'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),
    path('about/', views.about, name='blog-about'),
    path('category/<str:cats>/', CategoryView, name='category'),
    # path('donate/', views.DonateView, name='donate'),
    path('dashboard/', views.DashboardView, name='dashboard'),
    path('blogs2/', PostListView2.as_view(), name='blog-home2'),
    path('post2/<int:pk>/', PostDetailView2, name='post-detail2'),
    path('api/', include(api_url)),
]