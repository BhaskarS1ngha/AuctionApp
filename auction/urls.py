from django.urls import path
from . import views


app_name = 'auction'

urlpatterns = [
    path("", views.homepage, name="homepage"),
    path("users/", views.getUsers, name="userlist"),
    path('logout', views.logout_request, name='logout'),
    path('login', views.login_request, name='login'),
    path('auctionAdmin/',views.admin,name="adminPanel"),
]
