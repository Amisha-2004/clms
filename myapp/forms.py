# forms.py
from django import forms
from .models import Supplier, Purchase

class SupplierForm(forms.ModelForm):
    class Meta:
        model = Supplier
        fields = ['Name', 'Code', 'Address', 'Contact_no', 'Email']

class PurchaseForm(forms.ModelForm):
    class Meta:
        model = Purchase
        fields = ['supplier', 'Item_purchased', 'Quantity_purchased', 'Unit_price']


# from django import forms
# from .models import Purchase

# class PurchaseForm(forms.ModelForm):
#     class Meta:
#         model = Purchase
#         fields = ['Date_of_purchase', 'supplier', 'Item_purchased', 'Quantity_purchased', 'Unit_price']


# from django import forms
# from .models import Purchase

class PurchaseForm(forms.ModelForm):
    class Meta:
        model = Purchase
        fields = ['Date_of_purchase', 'supplier', 'Item_purchased', 'Quantity_purchased', 'Unit_price']

#         from django import forms
# from .models import Item

# class ItemForm(forms.ModelForm):
#     class Meta:
#         model = Item
#         fields = ['name', 'specification', 'location', 'company', 'fund_type', 'status']

