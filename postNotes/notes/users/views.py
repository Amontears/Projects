from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from .forms import RegisterForm, LoginForm, ProfileForm
from .models import Profile

# Регистрация пользователя
def signupuser(request):
    if request.user.is_authenticated:
        return redirect(to='noteapp:main')

    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            # Создание профиля пользователя при регистрации
            Profile.objects.get_or_create(user=user)
            return redirect(to='noteapp:main')
        else:
            messages.error(request, 'Ошибка в данных регистрации')
            return render(request, 'users/signup.html', context={"form": form})

    return render(request, 'users/signup.html', context={"form": RegisterForm()})

# Вход пользователя
def loginuser(request):
    if request.user.is_authenticated:
        # Создание профиля, если его нет
        if not hasattr(request.user, 'profile'):
            Profile.objects.get_or_create(user=request.user)
        return redirect(to='noteapp:main')

    if request.method == 'POST':
        user = authenticate(username=request.POST['username'], password=request.POST['password'])
        if user is None:
            messages.error(request, 'Неверное имя пользователя или пароль')
            return render(request, 'users/login.html', context={"form": LoginForm()})

        login(request, user)
        # Создание профиля, если его нет
        if not hasattr(user, 'profile'):
            Profile.objects.get_or_create(user=user)
        return redirect(to='noteapp:main')

    return render(request, 'users/login.html', context={"form": LoginForm()})

# Выход пользователя
@login_required
def logoutuser(request):
    logout(request)
    return redirect(to='noteapp:main')

# Профиль пользователя
@login_required
def profile(request):
    # Проверка существования профиля пользователя
    user_profile = getattr(request.user, 'profile', None)
    if not user_profile:
        user_profile = Profile.objects.create(user=request.user)

    if request.method == 'POST':
        profile_form = ProfileForm(request.POST, request.FILES, instance=user_profile)
        if profile_form.is_valid():
            profile_form.save()
            messages.success(request, 'Ваш профиль успешно обновлен')
            return redirect(to='users:profile')
    else:
        profile_form = ProfileForm(instance=user_profile)

    return render(request, 'users/profile.html', {'profile_form': profile_form})
