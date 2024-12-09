# from django.db import models
# from datetime import date

# # Supplier Model
# class Supplier(models.Model):
#     Supplier_id = models.AutoField(primary_key=True)  # Primary key, auto-generated
#     Name = models.CharField(max_length=100)  # Name of the supplier
#     Code = models.CharField(max_length=50, unique=True)  # Unique code for the supplier
#     Address = models.TextField()  # Address of the supplier
#     Contact_no = models.CharField(max_length=15)  # Contact number
#     Email = models.EmailField(unique=True)  # Email address, must be unique

#     def __str__(self):
#         return f"{self.Name} ({self.Code})"

# # Purchase Model
# class Purchase(models.Model):
#     purchase_id = models.AutoField(primary_key=True)  # Primary key, auto-generated
#     Date_of_purchase = models.DateField(default=date.today)  # Date of purchase
#     supplier = models.ForeignKey('Supplier', on_delete=models.CASCADE, related_name='purchases')  # Foreign key to Supplier
#     Item_purchased = models.CharField(max_length=200)  # Name or description of the item purchased
#     Quantity_purchased = models.FloatField()  # Quantity purchased
#     Unit_price = models.DecimalField(max_digits=10, decimal_places=2)  # Unit price of the item
#     Total_price = models.DecimalField(max_digits=15, decimal_places=2)  # Total price (calculated)

#     def __str__(self):
#         return f"Purchase ID: {self.purchase_id} - {self.Item_purchased}"

#     def save(self, *args, **kwargs):
#         # Automatically calculate the total price before saving
#         self.Total_price = self.Quantity_purchased * self.Unit_price
#         super(Purchase, self).save(*args, **kwargs)

   
# from django.db import models
# from datetime import date

# class DailyUsage(models.Model):
#     usage_id = models.AutoField(primary_key=True)  # Primary Key
#     date = models.DateField(default=date.today)  # Date of usage
#     batch = models.CharField(max_length=100)  # Batch that used the chemical
#     quantity_used = models.FloatField()  # Quantity used
#     item_id = models.ForeignKey('Item', on_delete=models.CASCADE, related_name='usages')  # Foreign Key to Item model

#     def _str_(self):
#         return f"Usage ID: {self.usage_id} - {self.item.name}"
    



# from django.db import models


# class Student(models.Model):
#     Admn_no = models.CharField(max_length=20, primary_key=True)  # Admission number as the primary key
#     Name = models.CharField(max_length=100)  # Name of the student
#     Department = models.CharField(max_length=100)  # Department of the student
#     Batch = models.CharField(max_length=50)  # Batch or year (e.g., 2023-2027)
#     Roll_no = models.IntegerField()  # Class roll number

#     def __str__(self):
#         return f"{self.Name} ({self.Admn_no})"


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

# # Purchase Model
# class Purchase(models.Model):
#     purchase_id = models.AutoField(primary_key=True)
#     Date_of_purchase = models.DateField(default=date.today)
#     supplier = models.ForeignKey('Supplier', on_delete=models.CASCADE, related_name='purchases')
#     Item_purchased = models.CharField(max_length=200)
#     Quantity_purchased = models.FloatField()
#     Unit_price = models.DecimalField(max_digits=10, decimal_places=2)
#     Total_price = models.DecimalField(max_digits=15, decimal_places=2)

#     def __str__(self):
#         return f"Purchase ID: {self.purchase_id} - {self.Item_purchased}"

#     def save(self, *args, **kwargs):
#         self.Total_price = self.Quantity_purchased * self.Unit_price
#         super(Purchase, self).save(*args, **kwargs)


# from django.db import models
# from datetime import date

# class Purchase(models.Model):
#     purchase_id = models.AutoField(primary_key=True)
#     Date_of_purchase = models.DateField(default=date.today)
#     supplier = models.ForeignKey('Supplier', on_delete=models.CASCADE, related_name='purchases')
#     Item_purchased = models.CharField(max_length=200)
#     Quantity_purchased = models.FloatField()
#     Unit_price = models.DecimalField(max_digits=10, decimal_places=2)
#     Total_price = models.DecimalField(max_digits=15, decimal_places=2)

#     def __str__(self):
#         return f"Purchase ID: {self.purchase_id} - {self.Item_purchased}"

#     def save(self, *args, **kwargs):
#         self.Total_price = self.Quantity_purchased * self.Unit_price
#         super(Purchase, self).save(*args, **kwargs)


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


# Purchase Model
class Purchase(models.Model):
    purchase_id = models.AutoField(primary_key=True)
    Date_of_purchase = models.DateField(default=date.today)
    supplier = models.ForeignKey(Supplier, on_delete=models.CASCADE, related_name='purchases')
    Item_purchased = models.CharField(max_length=200)
    Quantity_purchased = models.FloatField()
    Unit_price = models.DecimalField(max_digits=10, decimal_places=2)
    Total_price = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)

    def __str__(self):
        return f"Purchase ID: {self.purchase_id} - {self.Item_purchased}"

    def save(self, *args, **kwargs):
        # Ensure compatibility by converting the quantity and unit price to Decimal before multiplication
        self.Total_price = Decimal(self.Quantity_purchased) * Decimal(self.Unit_price)
        super(Purchase, self).save(*args, **kwargs)


# class Purchase(models.Model):
#     purchase_id = models.AutoField(primary_key=True)
#     date = models.DateField(auto_now_add=True)  # Automatically sets the current date when the record is created.
#     supplier = models.ForeignKey(Supplier, on_delete=models.CASCADE, related_name='purchases')
#     total_amount = models.DecimalField(max_digits=10, decimal_places=2)  # e.g., 1200.50

#     def __str__(self):
#         return f"Purchase ID: {self.purchase_id} | Supplier: {self.supplier.name} | Total Amount: {self.total_amount}"


# from django.db import models

# # Define the Item model
# class Item(models.Model):
#     item_id = models.AutoField(primary_key=True)  # Auto-incremented primary key
#     name = models.CharField(max_length=255)  # Name of the item
#     specification = models.TextField()  # Specification of the item
#     location = models.CharField(max_length=255)  # Location of the item in the lab
#     company = models.CharField(max_length=255)  # Company name
#     fund_type = models.CharField(max_length=100)  # Type of funding (e.g., government, private, etc.)
#     status_choices = [
#         ('working', 'Working'),
#         ('repair', 'Repair'),
#         ('damaged', 'Damaged')
#     ]
#     status = models.CharField(max_length=10, choices=status_choices, default='working')  # Status of the item
    
#     def __str__(self):
#         return self.name
