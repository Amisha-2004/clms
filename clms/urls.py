"""
URL configuration for clms project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from myapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.user_login, name='login'),
    path('hod_dashboard/', views.hod_dashboard, name='hod_dashboard'),
       # Supplier URLs
    path('supplier/', views.supplier_table, name='supplier_table'),
    path('supplier/add/', views.add_supplier, name='add_supplier'),
    path('supplier/edit/<int:pk>/', views.edit_supplier, name='edit_supplier'),
    path('supplier/delete/<int:pk>/', views.delete_supplier, name='delete_supplier'),

    # Purchase URLs
    path('purchase/', views.purchase_table, name='purchase_table'),
    path('purchase/add/', views.add_purchase, name='add_purchase'),
    path('purchase/edit/<int:pk>/', views.edit_purchase, name='edit_purchase'),
    path('purchase/delete/<int:pk>/', views.delete_purchase, name='delete_purchase'),
    path('supplier/edit/<int:pk>/', views.edit_supplier, name='edit_supplier'),
    path('purchase_table/', views.purchase_table, name='purchase_table'),
    path('add_purchase/', views.add_purchase, name='add_purchase'),
    path('edit_purchase/<int:purchase_id>/', views.edit_purchase, name='edit_purchase'),
    path('delete_purchase/<int:purchase_id>/', views.delete_purchase, name='delete_purchase'),
    path('add-purchase/', views.add_purchase, name='add_purchase'),
    path('edit-purchase/<int:purchase_id>/', views.edit_purchase, name='edit_purchase'),
    path('delete-purchase/<int:purchase_id>/', views.delete_purchase, name='delete_purchase'),
    path('purchases/', views.purchase_list, name='purchase_list'),
    # path('', views.item_list, name='item_list'),  # List items
    # path('add/', views.add_item, name='add_item'),  # Add item
    # path('edit/<int:pk>/', views.edit_item, name='edit_item'),  # Edit item
    # path('delete/<int:pk>/', views.delete_item, name='delete_item'),
    

    
]

# # urls.py
# from django.urls import path
# from . import views

# urlpatterns = [
#     # Supplier URLs
#     path('supplier/', views.supplier_table, name='supplier_table'),
#     path('supplier/add/', views.add_supplier, name='add_supplier'),
#     path('supplier/edit/<int:pk>/', views.edit_supplier, name='edit_supplier'),
#     path('supplier/delete/<int:pk>/', views.delete_supplier, name='delete_supplier'),

#     # Purchase URLs
#     path('purchase/', views.purchase_table, name='purchase_table'),
#     path('purchase/add/', views.add_purchase, name='add_purchase'),
#     path('purchase/edit/<int:pk>/', views.edit_purchase, name='edit_purchase'),
#     path('purchase/delete/<int:pk>/', views.delete_purchase, name='delete_purchase'),
# ]

