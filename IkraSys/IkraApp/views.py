from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
# Create your views here.
from django.views import generic
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .forms import StudentsForm
from django.contrib.auth import authenticate, login, logout


def form(request):
    if request.method == 'POST':
        form = StudentsForm(request.POST, request.FILES)
        if form.is_valid():
            Students = form.save(commit=False)
            Students.save()
            return redirect('login')

    else:
        form = StudentsForm()
    return render(request, 'form.html', {'form': form })




def login_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user.is_active:
            login(request, user)
            return redirect('/form')
        else:
            messages.warning(
                request, 'هناك خطأ في اسم المستخدم أو كلمة المرور.')

    return render(request, 'login.html', {
        'title': 'تسجيل الدخول',
    })


def logout_user(request):
    logout(request)
    return render(request, 'logout.html', {
        'title': 'تسجيل الخروج'
    })

