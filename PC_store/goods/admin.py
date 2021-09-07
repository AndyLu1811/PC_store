from django.contrib import admin
from goods.models import GoodsCategory, GoodsInfo

# Register your models here.
admin.site.register(GoodsCategory)
admin.site.register(GoodsInfo)