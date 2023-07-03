from django.urls import path
from news import views

app_name = 'news'

urlpatterns = [
    path('news/', views.news_view, name='news'),
    path('details/<int:pk>/', views.news_detail, name='detail'),
]
