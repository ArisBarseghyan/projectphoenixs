from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_page, name='home'),
    path('models/', views.supercars, name='models'),
    path('details/<int:pk>/', views.car_detail, name='detail'),
    path('login/', views.login_view, name='login'),
    path('sing_in/', views.registration_view, name='sing_in'),
    path('logout/', views.logout_view, name='logout'),
    path('cars/', views.cars, name='cars'),
    path('car/<int:pk>/', views.car_detail, name='car_detail'),
    path('add/', views.add_car, name='add'),
    path('order/', views.order_view, name='order'),
    path('manufacturers/', views.company_view, name='Manufacturers'),
    path('com_details/<int:pk>/', views.company_detail, name='com_detail'),
]
