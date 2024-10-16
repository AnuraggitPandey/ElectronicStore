from django.contrib import admin
from django.urls import path,include
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from store.views import *



urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('store.urls')),
    path('login',login_page,name='login'),
    path('register',register_page,name='register'),
    path('add-cart/<product_uid>',add_cart,name='add_cart'),
    path('register',include('store.urls')),
    path('cart',cart,name='cart'),
    path('details',address_ord,name='details'),
    path('logout',signout,name='logout'),
    path('takemail',takemail,name='mail'),
    path('confirmation',confirmation,name='confirmation'),
    path('remove_cart_items/<cart_item_uid>',remove_cart_items,name='remove_cart_items'),
    path('proceed-to-pay',razorpaycheck,name="razorpaycheck"),
    path('order_done',orderdone,name="order-done"),
    path('home',include('store.urls')),
    path('about',include('store.urls')),
    path('contact',include('store.urls')),
    path('order',include('store.urls')),
]
# static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
        
urlpatterns += staticfiles_urlpatterns()