from django.conf import settings
from django.urls import path, include
from django.conf.urls.static import static

from . import views
urlpatterns = [
    path('', views.sign_in, name='login'),
    path('product',views.product,name="product"),
    path('index', views.index, name="index"),
    path('product1/<int:id>', views.product1, name="product1"),
    path('order/<int:id>', views.order, name="order"),
    path('orderdetail/<int:id>',views.orderdetail,name="orderdetail"),
    path("add/<int:product_id>/", views.order, name="add_order"),
    path("update/<int:id>",views.update_order,name="update_order"),
    path("productcate/<int:id>",views.product_cate, name="product_cate")
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)