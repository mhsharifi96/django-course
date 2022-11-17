from django.urls import path
from . import views
urlpatterns = [
    path('', views.index),
    path('load/', views.load_products), # initialize to product 
    path('product/<int:product_id>/', views.product, name='product'),
    path('limit', views.limit_seen_main_page, name='limit'),
    path('cookie',views.sample_cookie,name='set-cookie'),
    path('cookie2',views.sample_cookie2,name='set-cookie2'),
    path('read-cookie',views.read_cookie,name='read-cookie'),

]


