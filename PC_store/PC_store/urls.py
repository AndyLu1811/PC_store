"""PC_store URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from goods.views import goods, index, detail
from cart.views import add_cart, show_cart, remove_cart, place_order
urlpatterns = [
    path('admin/', admin.site.urls),
    path('index/', index), #首页
    path('detail/', detail),
    path('cart/add_cart/', add_cart),
    path('goods/', goods),
    path('cart/show_cart/', show_cart),
    path('cart/remove_cart/', remove_cart),
    path('cart/place_order/', place_order),

]
