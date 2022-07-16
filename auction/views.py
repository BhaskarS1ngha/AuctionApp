from django.shortcuts import render, redirect
from .models import Auction, user
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from django.core.paginator import Paginator


def homepage(request):
    page_number = request.GET.get("page",1)
    per_page = 10
    auctions = Auction.objects.filter(isActive=True)
    paginator = Paginator(auctions,per_page)
    page = paginator.get_page(page_number)
    page.page_range = paginator.get_elided_page_range(page_number, on_each_side=1,on_ends=2)

    return render(request,template_name='auction/index.html', context={"Auctions": page})


def admin(request):
    if request.user.is_superuser:
        page_number = request.GET.get("page", 1)
        per_page = 10
        auctions = Auction.objects.filter()
        paginator = Paginator(auctions, per_page)
        page = paginator.get_page(page_number)
        page.page_range = paginator.get_elided_page_range(page_number, on_each_side=1, on_ends=2)
        return render(request, template_name='auction/adminPage.html', context={"Auctions": page})
    else:
        messages.error(request,"You need to be logged in")
        return redirect("auction:login")


def getUsers(request):
    return render(request, template_name='auction/show_users.html', context={"Users": user.objects.all()})


def logout_request(request):
    logout(request)
    messages.info(request, "Logged out successfully!")
    return redirect("auction:homepage")


def login_request(request):
    if request.method == 'POST':
        form = AuthenticationForm(request=request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.info(request, f"You are now logged in as {username}")
                return redirect('auction:homepage')
            else:
                messages.error(request, "Invalid username or password.")
        else:
            messages.error(request, "Invalid username or password.")
    form = AuthenticationForm()
    return render(request=request,
                  template_name="auction/login.html",
                  context={"form": form})
