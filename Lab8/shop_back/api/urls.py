from django.urls import path
from api import views

urlpatterns = [
    path('products/', views.product_list),
    path('products/<int:product_id>/', views.product_details),
    path('categories/', views.product_categoties),
    path('categories/<int:category_id>/', views.category_details),
    path('categories/<int:category_id>/products/', views.products_by_category),
]