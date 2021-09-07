from django.contrib import admin
from cart.models import OrderGoods, OrderInfo 

# Register your models here.
admin.site.register(OrderInfo)
admin.site.register(OrderGoods)