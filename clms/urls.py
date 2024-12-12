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

    #items URLs
    path('add/', views.add_item, name='add_item'),
    path('items/', views.item_list, name='item_list'),
    path('items/add/', views.add_item, name='add_item'),
    path('items/edit/<int:item_id>/', views.edit_item, name='edit_item'),
    path('items/delete/<int:item_id>/', views.delete_item, name='delete_item'),

    #stuents URLs
    path('students/', views.student_list, name='student_list'),
    path('students/add/', views.add_student, name='add_student'),
    path('students/edit/<int:student_id>/', views.edit_student, name='edit_student'),
    path('students/delete/<int:student_id>/', views.delete_student, name='delete_student'),
    
    
    #Usage URLs
    path('usage/', views.usage_list, name='usage_list'),
    path('usage/add/', views.add_usage, name='add_usage'),
    path('usage/update/<int:pk>/', views.update_usage, name='update_usage'),
    path('usage/delete/<int:pk>/', views.delete_usage, name='delete_usage'),
    
    #purchasemain URLs
    path('purchase/', views.purchase_list, name='purchase_list'),
    path('purchases/', views.purchase_list, name='purchase_list'),  # List of all purchases
    path('add_purchase/', views.add_purchase, name='add_purchase'),  # Add a new purchase
    path('update_purchase/<str:purchase_id>/', views.update_purchase, name='update_purchase'),  # Update a purchase
    path('delete_purchase/<str:purchase_id>/', views.delete_purchase, name='delete_purchase'),  # Delete a purchase

    #purchasesub URLs
    path('purchase-sub/', views.purchase_sub_list, name='purchase_sub_list'),
    path('purchase/add/', views.add_purchase_sub, name='add_purchase_sub'),
    path('purchase/edit/<int:sub_id>/', views.edit_purchase_sub, name='edit_purchase_sub'),
    path('purchase/delete/<int:sub_id>/', views.delete_purchase_sub, name='delete_purchase_sub'), 
 
]

