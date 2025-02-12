from django.urls import path
from . import views

urlpatterns=[
    path('shop_login',views.shop_login),
    path('logout',views.shop_logout),


















    # ...........................admin.......................................

    path('shop_home',views.shop_home),
    path('add_product',views.add_product),
    path('edit_product/<id>',views.edit_product),
    path('delete_product/<id>',views.delete_product),



















    # ...........................user..................................................
    path('',views.user_home),
    path('register',views.register),
    path('view_product/<pid>',views.view_product),
    path('helmets',views.helmets),
    path('jackets',views.jackets),
    path('gloves',views.gloves),

    path('add_to_cart/<pid>',views.add_to_cart),
]
