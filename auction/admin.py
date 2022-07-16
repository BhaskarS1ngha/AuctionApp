from django.contrib import admin
from .models import Auction,user,bid
# Register your models here.

admin.site.register(Auction)
admin.site.register(user)
admin.site.register(bid)