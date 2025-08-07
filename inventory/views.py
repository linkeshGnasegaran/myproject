from django.shortcuts import render, redirect
from .forms import SignUpForm, LoginForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

def home(request):
    return render(request, 'inventory/home.html')  # Point to actual template

def signup_view(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.user_type = form.cleaned_data['role']
            user.save()
            return redirect('login')  # Redirect to login after signup
    else:
        form = SignUpForm()
    return render(request, 'inventory/signup.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            # Optional: redirect based on role
            if user.user_type == 'admin':
                return redirect('admin_dashboard')
            elif user.user_type == 'manager':
                return redirect('manager_dashboard')
            elif user.user_type == 'cashier':
                return redirect('cashier_dashboard')
            else:
                return redirect('home')  # Default fallback
    else:
        form = LoginForm()
    return render(request, 'inventory/login.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('login')

# ✅ Add these dashboard views below:
@login_required
def admin_dashboard(request):
    return render(request, 'inventory/admin_dashboard.html')

@login_required
def manager_dashboard(request):
    return render(request, 'inventory/manager_dashboard.html')

@login_required
def cashier_dashboard(request):
    return render(request, 'inventory/cashier_dashboard.html')
