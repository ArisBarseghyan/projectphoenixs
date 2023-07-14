from .models import Car, Comment
from .forms import RegistrationForm, LoginForm
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from .forms import CommentForm, CarForm


def home_page(request):
    return render(request, 'home/home_page.html')


def add_car(request):
    if request.method == 'POST':
        form = CarForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('models/cars.html')
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
    cars = Car.objects.all()
    return render(request, 'models/cars.html', {'cars': cars})
