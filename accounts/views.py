from django.shortcuts import render, redirect
from django.contrib.auth import login as auth_login, logout as auth_logout, update_session_auth_hash
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, PasswordChangeForm
from django.views.decorators.http import require_http_methods
from django.contrib.auth.decorators import login_required
from . import forms 


# Create your views here.
#user login function
def login(request):
    if request.method == "POST":
        form=AuthenticationForm(data=request.POST)
        if form.is_valid():
            auth_login(request, form.get_user())
            next_path = request.GET.get("next") or "articles:articles"
            return redirect("articles")
    else:
        form = AuthenticationForm()
    context={"form":form}
    return render(request, "accounts/login.html", context)

# user logout function
@require_http_methods(["POST"])
def logout(request):
    if request.user.is_authenticated:
        auth_logout(request)
    return redirect("articles")

# adding user
def signup(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user=form.save()
            auth_login(request, user)
            return redirect("articles:articles")
    else:
        form = UserCreationForm()
    context = {"form": form}
    return render(request, "accounts/signup.html", context)

# removing user
@require_http_methods(["POST"])
def delete(request):
    if request.user.is_authenticated:
        request.user.delete()
        auth_logout(request)
    return redirect("articles:articles")

# editing user info
@require_http_methods(["GET", "POST"])
def update(request):
    if request.method == "POST":
        form = forms.CustomUserChangeForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect("accounts:mypage")
    else:
        form = forms.CustomUserChangeForm(instance=request.user)
    context = {"form": form}
    return render(request, "accounts/update.html", context)

# render mypage
def mypage(request):
    if request.user.is_authenticated:
        context={
            'my':request.user.my_articles.all(),
            'liked':request.user.liked_articles.all()
        }
        return render(request, "accounts/mypage.html",context)
    
    return redirect("accounts:login")

# change password
@login_required
@require_http_methods(["GET", "POST"])
def change_password(request):
    if request.method == "POST":
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
            return redirect("accounts:mypage")
    else:
        form = PasswordChangeForm(request.user)
    context = {"form": form}
    return render(request, "accounts/change_password.html", context)
