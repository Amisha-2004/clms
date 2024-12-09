# from django.shortcuts import render
# from django.http import HttpResponse
# from django.contrib import messages

# from django.shortcuts import render,redirect, get_object_or_404

# from django.contrib import messages
# from django.contrib.auth import authenticate, login
# from django.contrib.auth.hashers import make_password
# from datetime import datetime



# # Create your views here.
# # def login(request):
# #     # if request.method == 'POST':
# #     #     username = request.POST['username']
# #     #     password = request.POST['password']
# #     #     user = authenticate(request, username=username, password=password)

# #     #     if user is not None:
# #     #         login(request, user)
# #     #         # Redirect based on the user's role
# #     #         if user.role_id == 4:
# #     #             return redirect('admin_dashboard')  # Redirect to your custom admin dashboard
# #     #         elif user.role_id == 3:
# #     #             return redirect('foreman_dashboard')  # Redirect to your custom admin dashboard
# #     #         elif  user.role_id == 2:
# #     #             return redirect('worker_dashboard')  # Redirect to your custom admin dashboard
# #     #         else:
# #     #             return redirect('reporter_dashboard')  # Redirect to user dashboard (or another page)
# #     #     else:
# #     #         messages.error(request, 'Invalid username or password.')
# #     #         return redirect('user_login')
       
# #     return render(request, 'login.html')

# # from django.shortcuts import render, redirect
# # from django.contrib.auth import authenticate, login
# # from django.contrib import messages

# # def user_login(request):
# #     if request.method == 'POST':
# #         # Get username and password from POST request
# #         username = request.POST['username']
# #         password = request.POST['password']

# #         # Authenticate the user
# #         user = authenticate(request, username=username, password=password)

# #         if user is not None:
# #             # Log the user in if authentication is successful
# #             login(request, user)
           
# #             # Check the role_id of the user and redirect accordingly
# #             if user.id == 1:  # HOD role
# #                 return redirect('hod_dashboard')
# #             elif user.id == 2:  # Lab Assistant role
# #                 return redirect('lab_assistant_dashboard')
# #             elif user.id == 3:  # Lab Incharge role
# #                 return redirect('lab_incharge_dashboard')
# #             else:
# #                 # If no role matches, redirect to a general dashboard or homepage
# #                 return redirect('home')
# #         else:
# #             # If authentication fails, show an error message
# #             messages.error(request, 'Invalid username or password.')

# #     return render(request, 'login.html')
# # from django.shortcuts import render, redirect
# # from django.contrib.auth import authenticate, login
# # from django.contrib import messages

# # def users(request):
# #     if request.method == 'POST':
# #         username = request.POST['username']
# #         password = request.POST['password']

# #         # Authenticate the user
# #         user = authenticate(request, username=username, password=password)

# #         if user is not None:
# #             # Log the user in if authentication is successful
# #             login(request, user)  # Ensure the user object is passed correctly here

# #             # Check the role of the user (if using a custom role field)
# #             if user.role == 1:  # HOD role
# #                 return redirect('hod_dashboard')
# #             elif user.role == 2:  # Lab Assistant role
# #                 return redirect('lab_assistant_dashboard')
# #             elif user.role == 3:  # Lab Incharge role
# #                 return redirect('lab_incharge_dashboard')
# #             else:
# #                 # If no role matches, redirect to a general dashboard or homepage
# #                 return redirect('home')
# #         else:
# #             # If authentication fails, show an error message
# #             messages.error(request, 'Invalid username or password.')

# #     return render(request, 'login.html')
# from django.shortcuts import render, redirect
# from django.contrib.auth import authenticate, login
# from django.contrib import messages

# def user_login(request):
#     if request.method == 'POST':
#         # Get the username and password from the POST request
#         username = request.POST['username']
#         password = request.POST['password']
#         print(f"Authenticating with username: {username} and password: {password}")
#         # Attempt to authenticate the user with the provided credentials
#         user = authenticate(request, username=username, password=password)

#         # Check if the user is authenticated (not None)
#         if user is not None:
#             # User is authenticated, now log the user in
#             login(request, user)

#             # Check the role of the user and redirect based on role
#             if user.groups.filter(name='HOD').exists():
#                 return redirect('hod_dashboard')
              
#             elif user.groups.filter(name='Lab Assistant').exists():
#                 return redirect('lab_assistant_dashboard')
#             elif user.groups.filter(name='Lab Incharge').exists():
#                 return redirect('lab_incharge_dashboard')
#             else:
#                 # If user does not belong to any known group, redirect to a general home page
#                 return redirect('/home/')
#         else:
#             # Authentication failed, show an error message
#             messages.error(request, 'Invalid username or password.')

#     # Render the login page if the method is GET or if authentication fails
#     return render(request, 'login.html')
 
# def hod_dashboard(request):
#     return render(request, 'home.html')
    
# # def worker_dashboard(request):
# #     return render(request, 'worker.html')
 



from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.shortcuts import render, redirect

def user_login(request):
    if request.method == 'POST':
        # Get the username and password from the POST request
        username = request.POST['username']
        password = request.POST['password']
        
        # Attempt to authenticate the user with the provided credentials
        user = authenticate(request, username=username, password=password)

        if user is not None:
            # If authentication is successful, log the user in
            login(request, user)

            # Check the role of the user and redirect based on role
            if username=='hod':
                return redirect('hod_dashboard')  # Redirect to HOD dashboard
            elif user.groups.filter(name='Lab Assistant').exists():
                return redirect('lab_assistant_dashboard')  # Redirect to Lab Assistant dashboard
            elif user.groups.filter(name='Lab Incharge').exists():
                return redirect('lab_incharge_dashboard')  # Redirect to Lab Incharge dashboard
            else:
                # Redirect to a general home page for users without a specific role
                return redirect('hod_dashboard')
        else:
            # If authentication fails, show an error message
            messages.error(request, 'Invalid username or password.')

    # Render the login page if the method is GET or if authentication fails
    return render(request, 'login.html')


def hod_dashboard(request):
     return render(request, 'home.html')
    



# views.py
from django.shortcuts import render, get_object_or_404, redirect
from .models import Supplier, Purchase
from .forms import SupplierForm, PurchaseForm

# Supplier Table View
def supplier_table(request):
    suppliers = Supplier.objects.all()
    return render(request, 'supplier_table.html', {'suppliers': suppliers})

# Purchase Table View
def purchase_table(request):
    purchases = Purchase.objects.all()
    return render(request, 'purchase_table.html', {'purchases': purchases})

# Add Supplier
def add_supplier(request):
    if request.method == 'POST':
        form = SupplierForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('supplier_table')
    else:
        form = SupplierForm()
    return render(request, 'add_supplier.html', {'form': form})

# Edit Supplier
# def edit_supplier(request, pk):
#     supplier = get_object_or_404(Supplier, pk=pk)
#     if request.method == 'POST':
#         form = SupplierForm(request.POST, instance=supplier)
#         if form.is_valid():
#             form.save()
#             return redirect('supplier_table')
#     else:
#         form = SupplierForm(instance=supplier)
#     return render(request, 'edit_supplier.html', {'form': form})
# views.py
from django.shortcuts import render, get_object_or_404, redirect
from .forms import SupplierForm
from .models import Supplier

# views.py
from django.shortcuts import render, get_object_or_404, redirect
from .forms import SupplierForm
from .models import Supplier

def edit_supplier(request, pk):  # Accept `pk` argument here
    supplier = get_object_or_404(Supplier, pk=pk)  # Use `pk` in get_object_or_404
    
    if request.method == 'POST':
        form = SupplierForm(request.POST, instance=supplier)
        if form.is_valid():
            form.save()
            return redirect('supplier_table')  # Redirect to the supplier list page
    else:
        form = SupplierForm(instance=supplier)
    
    return render(request, 'edit_supplier.html', {'form': form})



# Delete Supplier
def delete_supplier(request, pk):
    supplier = get_object_or_404(Supplier, pk=pk)
    supplier.delete()
    return redirect('supplier_table')

# Add Purchase
# def add_purchase(request):
#     if request.method == 'POST':
#         form = PurchaseForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('purchase_table')
#     else:
#         form = PurchaseForm()
#     return render(request, 'add_purchase.html', {'form': form})

# # Edit Purchase
# def edit_purchase(request, pk):
#     purchase = get_object_or_404(Purchase, pk=pk)
#     if request.method == 'POST':
#         form = PurchaseForm(request.POST, instance=purchase)
#         if form.is_valid():
#             form.save()
#             return redirect('purchase_table')
#     else:
#         form = PurchaseForm(instance=purchase)
#     return render(request, 'edit_purchase.html', {'form': form})

# # Delete Purchase
# def delete_purchase(request, pk):
#     purchase = get_object_or_404(Purchase, pk=pk)
#     purchase.delete()
#     return redirect('purchase_table')


# def add_purchase(request):
#     if request.method == 'POST':
#         form = PurchaseForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('purchase_table')
#     else:
#         form = PurchaseForm()
#     return render(request, 'add_edit_purchase.html', {'form': form, 'title': 'Add Purchase', 'heading': 'Add Purchase'})

# def edit_purchase(request, purchase_id):
#     purchase = get_object_or_404(Purchase, pk=purchase_id)
#     if request.method == 'POST':
#         form = PurchaseForm(request.POST, instance=purchase)
#         if form.is_valid():
#             form.save()
#             return redirect('purchase_table')
#     else:
#         form = PurchaseForm(instance=purchase)
#     return render(request, 'add_edit_purchase.html', {'form': form, 'title': 'Edit Purchase', 'heading': 'Edit Purchase'})


from django.shortcuts import render, redirect, get_object_or_404
from .models import Purchase
from .forms import PurchaseForm

# Add Purchase View
def add_purchase(request):
    if request.method == 'POST':
        form = PurchaseForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('purchase_list')
    else:
        form = PurchaseForm()
    return render(request, 'add_purchase.html', {'form': form})

# Edit Purchase View
def edit_purchase(request, purchase_id):
    purchase = get_object_or_404(Purchase, pk=purchase_id)
    if request.method == 'POST':
        form = PurchaseForm(request.POST, instance=purchase)
        if form.is_valid():
            form.save()
            return redirect('purchase_list')
    else:
        form = PurchaseForm(instance=purchase)
    return render(request, 'edit_purchase.html', {'form': form})

# Delete Purchase View
def delete_purchase(request, purchase_id):
    purchase = get_object_or_404(Purchase, pk=purchase_id)
    if request.method == 'POST':
        purchase.delete()
        return redirect('purchase_list')
    return render(request, 'delete_purchase.html', {'purchase': purchase})

# List Purchase View
def purchase_list(request):
    purchases = Purchase.objects.all()
    return render(request, 'purchase_list.html', {'purchases': purchases})



# from django.shortcuts import render, get_object_or_404, redirect
# from .models import Item
# from .forms import ItemForm

# # List all items
# def item_list(request):
#     items = Item.objects.all()  # Fetch all items from the database
#     return render(request, 'item_list.html', {'items': items})

# # Add a new item
# def add_item(request):
#     if request.method == 'POST':
#         form = ItemForm(request.POST)
#         if form.is_valid():
#             form.save()  # Save the new item to the database
#             return redirect('item_list')  # Redirect to the item list page after saving
#     else:
#         form = ItemForm()
#     return render(request, 'add_item.html', {'form': form})

# # Edit an existing item
# def edit_item(request, pk):
#     item = get_object_or_404(Item, pk=pk)  # Fetch the item to edit using its primary key
#     if request.method == 'POST':
#         form = ItemForm(request.POST, instance=item)  # Bind the form with the existing item
#         if form.is_valid():
#             form.save()  # Save the changes
#             return redirect('item_list')  # Redirect to the item list page after saving
#     else:
#         form = ItemForm(instance=item)
#     return render(request, 'edit_item.html', {'form': form})

# # Delete an item
# def delete_item(request, pk):
#     item = get_object_or_404(Item, pk=pk)  # Fetch the item using its primary key
#     if request.method == 'POST':
#         item.delete()  # Delete the item from the database
#         return redirect('item_list')  # Redirect to the item list page after deletion
#     return render(request, 'confirm_delete_item.html', {'item': item})
