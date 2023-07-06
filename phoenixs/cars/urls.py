from django.urls import path
from cars import views

urlpatterns = [
    path('', views.home_page, name='home'),
    path('models/', views.supercars, name='models'),
    path('details/<int:pk>/', views.car_detail, name='detail'),
    path('login/', views.login_view, name='login'),
    path('sing_in/', views.registration_view, name='sing_in'),
    path('logout/', views.logout_view, name='logout'),
    path('Exclusive_cars/', views.exclusive, name='exclusive'),
    path('car/<int:pk>/', views.car_detail, name='car_detail'),
]
