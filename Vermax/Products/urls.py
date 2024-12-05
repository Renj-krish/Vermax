from django.urls import path
#from django.conf.urls.static import static
#from django.conf import settings
from . import views


urlpatterns = [
    path('', views.index, name='home'),
    path('product_list', views.product_list , name='product_list'),
    path('product_detail', views.detail_product , name='detail_product')
]