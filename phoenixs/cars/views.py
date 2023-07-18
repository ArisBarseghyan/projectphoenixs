from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import Car, Comment, Company
from .forms import RegistrationForm, LoginForm, VehicleFilterForm, CommentForm, CarForm, SendForm
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.core.mail import send_mail, EmailMessage
from django.conf import settings


def home_page(request):
    return render(request, 'home/home_page.html')


def add_car(request):
    if request.method == 'POST':
        form = CarForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = CarForm()
    return render(request, 'models/add_car.html', {'car': form})


def supercars(request):
    cars = Car.objects.all()
    return render(request, 'models/supercars.html', {'cars': cars})


def car_detail(request, pk):
    car = get_object_or_404(Car, pk=pk)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.user = request.user
            comment.car = car
            comment.save()
    else:
        form = CommentForm()

    comments = Comment.objects.filter(car=car)

    return render(request, 'models/detail.html', {'car': car, 'comment': form, 'comments': comments})


def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')
    else:
        form = LoginForm()
    return render(request, 'login/login.html', {'form': form})


def registration_view(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = RegistrationForm()
    return render(request, 'login/registration.html', {'form': form})


def logout_view(request):
    logout(request)
    return redirect('home')


def cars(request):
    form = VehicleFilterForm(request.GET)
    vehicles = Car.objects.all()
    if form.is_valid():
        body_type = form.cleaned_data.get('body_type')
        if body_type:
            vehicles = vehicles.filter(body_type=body_type)

    page_count = Paginator(vehicles, 2)
    page_number = request.GET.get('page')

    try:
        page_obj = page_count.get_page(page_number)
    except (PageNotAnInteger, EmptyPage):
        page_obj = page_count.page(5)

    context = {
        'form': form,
        'page_obj': page_obj
    }
    return render(request, 'models/cars.html', context)


def order_view(request):
    form = SendForm(request.GET)
    if form.is_valid():
        send_to = form.cleaned_data.get("user_mail")
        client_name = request.user.username
        message = f'Dear {client_name},\n\nThank you for purchasing a car from Phoenixs Car Salon. We appreciate your business and hope you enjoy your new car!\n\nBest regards,\nThe Phoenixs Team'
        send_mail(subject='Hello from Django', message=message,
                  recipient_list=[send_to],
                  from_email=settings.EMAIL_HOST_USER)
        return redirect('home')
    return render(request, 'models/car_order.html', {'form': form})


def company_view(request):
    company = Company.objects.all()
    return render(request, 'company/company.html', {'company': company})


def company_detail(request, pk):
    company = get_object_or_404(Company, pk=pk)
    return render(request, 'company/detail.html', {'com': company})
