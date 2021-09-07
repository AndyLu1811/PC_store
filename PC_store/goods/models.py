from django.db import models

# Create your models here.
class GoodsCategory(models.Model):
    cag_name = models.CharField(max_length=30)
    cag_css = models.CharField(max_length=20)
    cag_img = models.ImageField(upload_to='cag')
    def __str__(self):
        return self.cag_name

class GoodsInfo(models.Model):
    goods_name = models.CharField(max_length=30)
    goods_price = models.IntegerField(default=0)
    goods_desc = models.CharField(max_length=2000)
    goods_img = models.ImageField(upload_to='goods')
    goods_cag = models.ForeignKey('GoodsCategory',on_delete=models.CASCADE,)

    def __str__(self):
        return self.goods_name