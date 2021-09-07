from django.http import request
from django.shortcuts import render
from django.core.paginator import Paginator
from .models import GoodsCategory, GoodsInfo


def index(request):
# 首页    
    categories = GoodsCategory.objects.all()
    
    for cag in categories:
        cag.goods_list = cag.goodsinfo_set.order_by('id')[:4]
    
    cart_goods_list = []
    cart_goods_count = 0

    for goods_id, goods_num in request.COOKIES.items():
        if not goods_id.isdigit():
            continue
        cart_goods = GoodsInfo.objects.get( id = goods_id)
        cart_goods.goods_num = goods_num
        cart_goods_list.append(cart_goods)
        cart_goods_count = cart_goods_count + int(goods_num)
    
    return render (request, 'index.html', {'categories': categories,
                                           'cart_good_list': cart_goods_list,
                                           'cart_goods_count': cart_goods_count })


def goods():
       
    cag_id = request.GET.get('cag', 1)
   
    page_id = request.GET.get('page', 1)
  
    goods_data = GoodsInfo.objects.filter(goods_cag_id=cag_id)
    
    paginator = Paginator(goods_data, 12)
    
    page_data = paginator.page(page_id)
   
    categories = GoodsCategory.objects.all()

    current_cag = GoodsCategory.objects.get(id=cag_id)
    
    
    cart_goods_list = []
    
    cart_goods_count = 0
   
    for goods_id, goods_num in request.COOKIES.items():
        
        
        if not goods_id.isdigit():
            continue

        cart_goods = GoodsInfo.objects.get(id=goods_id)
        cart_goods.goods_num = goods_num
        cart_goods_list.append(cart_goods)
       
        cart_goods_count = cart_goods_count + int(goods_num)

    return render(request, 'goods.html', {'page_data': page_data,
                                          'categories': categories,
                                          'current_cag': current_cag,
                                          'cart_goods_list': cart_goods_list,
                                          'cart_goods_count': cart_goods_count,
                                          'paginator': paginator,
                                          'cag_id': cag_id})

def detail(request):
    goods_id = request.GET.get('id', 1)
  
    goods_data = GoodsInfo.objects.get(id=goods_id)
   
    categories = GoodsCategory.objects.all()
  
    cart_goods_list = []
  
    cart_goods_count = 0
    
    for goods_id, goods_num in request.COOKIES.items():
      
        if not goods_id.isdigit():
            continue
 
        cart_goods = GoodsInfo.objects.get(id=goods_id)
        cart_goods.goods_num = goods_num
     
        cart_goods_list.append(cart_goods)
      
        cart_goods_count = cart_goods_count + int(goods_num)
    
    return render(request, 'detail.html', {'categories': categories,
                                           'goods_data': goods_data,
                                           'cart_goods_list': cart_goods_list,
                                           'cart_goods_count': cart_goods_count})

