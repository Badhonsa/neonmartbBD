


from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static

from account.views import *
from product.views import *
from product.views import ProductListView
urlpatterns = [
    path('admin/', admin.site.urls),
    path('products/', ProductListView.as_view(), name='products'),
    path('addtoCart/<int:product_id>/', add_to_cart, name='add_to_cart'),
    path('cart/', cart_view, name='cart'),
    path('product_details/<int:id>/', product_details, name='product_details'),
    path('home/', home, name='home'),

    path('', login_page, name='login'),
    path('verify_acc/',verify_acc, name='verify_acc'),
    path('reg/', registration_page, name='reg'),

    path('forget_pass/', forget_pass, name='forget_pass'),
    path('sidebar/', sidebar, name='sidebar'),
    path('addtoCart/<int:id>/', add_to_cart, name='addtoCart'),

]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
