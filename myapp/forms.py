# forms.py
from django import forms
from .models import Supplier

class SupplierForm(forms.ModelForm):
    class Meta:
        model = Supplier
        fields = ['Name', 'Code', 'Address', 'Contact_no', 'Email']


#item.py
from .models import Item

class ItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ['name', 'specification', 'location', 'company', 'fund_type', 'status', 'category']


#student.py
from .models import Student

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['name', 'department', 'batch', 'roll_no']


#usage.py
from .models import Usage

class UsageForm(forms.ModelForm):
    class Meta:
        model = Usage
        fields = ['date', 'time', 'batch', 'quantity', 'itemid']


#purchasemain.py
from .models import PurchaseMain

class PurchaseForm(forms.ModelForm):
    class Meta:
        model = PurchaseMain
        fields = ['purchase_id', 'date', 'total_amount', 'supplier']


#purchasesub.py
from .models import PurchaseSub

class PurchaseSubForm(forms.ModelForm):
    class Meta:
        model = PurchaseSub
        fields = ['item_id','purchase_id', 'quantity_purchased', 'price_per_unit']
        

