# models.py
from django.db import models
from datetime import date

# Supplier Model
class Supplier(models.Model):
    Supplier_id = models.AutoField(primary_key=True)
    Name = models.CharField(max_length=100)
    Code = models.CharField(max_length=50, unique=True)
    Address = models.TextField()
    Contact_no = models.CharField(max_length=15)
    Email = models.EmailField(unique=True)

    def __str__(self):
        return f"{self.Name} ({self.Code})"


from django.db import models
from decimal import Decimal
from datetime import date

# Supplier Model (example, assuming you already have a Supplier model)
class Supplier(models.Model):
    Supplier_id = models.AutoField(primary_key=True)
    Name = models.CharField(max_length=200)
    Code = models.CharField(max_length=100)
    Address = models.CharField(max_length=300)
    Contact_no = models.CharField(max_length=15)
    Email = models.EmailField()

    def __str__(self):
        return self.Name

#Item model
from django.db import models

class Item(models.Model):
    item_id = models.AutoField(primary_key=True)  # Auto-incremented primary key
    name = models.CharField(max_length=255)  # Name of the item
    specification = models.TextField()  # Specification of the item
    location = models.CharField(max_length=255)  # Location of the item in the lab
    company = models.CharField(max_length=255)  # Company name
    fund_type = models.CharField(max_length=100)  # Type of funding (e.g., government, private, etc.)
    status_choices = [
        ('working', 'Working'),
        ('repair', 'Repair'),
        ('damaged', 'Damaged'),
    ]
    status = models.CharField(
        max_length=10, 
        choices=status_choices, 
        default='working'  # Default status
    )  # Status of the item

    # Category field with predefined choices
    category_choices = [
        ('organic', 'Organic'),
        ('inorganic', 'Inorganic'),
        ('glassware', 'Glassware'),
        ('equipment', 'Equipment'),
        ('furniture', 'Furniture'),
    ]
    category = models.CharField(
        max_length=20, 
        choices=category_choices, 
        default='equipment'  # Default category
    )

    def __str__(self):
        return self.name


#stuedent model
from django.db import models

class Student(models.Model):
    student_id = models.AutoField(primary_key=True)  # Auto-incremented primary key
    name = models.CharField(max_length=255)  # Name of the student
    department = models.CharField(max_length=255)  # Department of the student
    batch = models.CharField(max_length=10)  # Batch/Year of the student
    roll_no = models.CharField(max_length=20)  # Roll number of the student

    def __str__(self):
        return self.name

#usage model
from django.db import models
from .models import Item  # Import Item model

class Usage(models.Model):
    usageid = models.AutoField(primary_key=True)  # Auto-increment primary key
    date = models.DateField(default=date.today)  # Date of usage
    time = models.TimeField()  # Time of usage
    batch = models.CharField(max_length=50)  # Batch name or ID
    quantity = models.PositiveIntegerField()  # Quantity used
    itemid = models.ForeignKey(Item, on_delete=models.CASCADE)  # Foreign key to Item table

    def __str__(self):
        return f"Usage {self.usageid} for Item {self.itemid.name}"


# PurchaseMain Model
class PurchaseMain(models.Model):
    purchase_id = models.CharField(max_length=50, primary_key=True)
    date = models.DateField(default=date.today)
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)
    supplier = models.ForeignKey(Supplier, on_delete=models.CASCADE)

    def __str__(self):
        return f"Purchase {self.purchase_id} - {self.supplier.Name}"
    

class PurchaseSub(models.Model):
    purchase_id = models.ForeignKey(PurchaseMain, on_delete=models.CASCADE, related_name='sub_items')
    item_id = models.ForeignKey(Item, on_delete=models.CASCADE)
    quantity_purchased = models.IntegerField()
    price_per_unit = models.DecimalField(max_digits=10, decimal_places=2)
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)

    def save(self, *args, **kwargs):
        self.total_amount = self.quantity_purchased * self.price_per_unit
        super().save(*args, **kwargs)

    def __str__(self):
        return f"Sub-item {self.item_id} for Purchase {self.purchase_id}"