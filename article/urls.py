from django.urls import path
from .views import (ArticleListView,
                    ArticleDetailView,
                    ArticleDeleteView,
                    ArticleUpdateView,
                    ArticleCreateView,
                    )





urlpatterns = [
    path('post/<int:pk>/', ArticleDetailView.as_view(), name='article_detail'),
    path('', ArticleListView.as_view(), name='article_view'),
    path('post/<int:pk>/delete/', ArticleDeleteView.as_view(), name='article_delete'),
    path('post/<int:pk>/edit/', ArticleUpdateView.as_view(), name='article_update'),
    path('post/new', ArticleCreateView.as_view(), name='article_create'),
]