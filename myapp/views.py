#login views
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
    



# supplier views
from django.shortcuts import render, get_object_or_404, redirect
from .models import Supplier
from .forms import SupplierForm

def supplier_table(request):
    suppliers = Supplier.objects.all()
    return render(request, 'supplier_table.html', {'suppliers': suppliers})

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


#edit supplier 
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

#item views
from django.shortcuts import render, get_object_or_404, redirect
from .models import Item
from .forms import ItemForm

# Display a list of items
def item_list(request):
    items = Item.objects.all()
    return render(request, 'item_list.html', {'items': items})

#add item
from django.shortcuts import render, redirect
from .models import Item

def add_item(request):
    if request.method == "POST":
        # Extract form data
        item_type = request.POST.get('item_type')
        condition = request.POST.get('condition')
        exp_date = request.POST.get('exp_date')
        itemid = request.POST.get('itemid')
        name = request.POST.get('name')
        specification = request.POST.get('specification')
        location = request.POST.get('location')
        company = request.POST.get('company')
        fundtype = request.POST.get('fundtype')

        # Save the data to the database
        Item.objects.create(
            name=name,
            specification=specification,
            location=location,
            company=company,
            fund_type=fundtype,
            status=condition,  # Assuming 'condition' matches status_choices
            category=item_type  # Assuming 'item_type' matches category_choices
        )

        # Redirect to the item list page
        return redirect('item_list')  # Replace 'item_list' with your URL name for the list view

    return render(request, 'add_item.html')

#edit item
def edit_item(request, item_id):
    item = get_object_or_404(Item, pk=item_id)
    if request.method == 'POST':
        form = ItemForm(request.POST, instance=item)
        if form.is_valid():
            form.save()
            return redirect('item_list')
        else:
            return render(request, 'add_edit_item.html', {'form': form, 'action': 'Edit'})
    else:
        form = ItemForm(instance=item)
    return render(request, 'add_edit_item.html', {'form': form, 'action': 'Edit'})

# Delete an item
def delete_item(request, item_id):
    item = get_object_or_404(Item, pk=item_id)
    if request.method == 'POST':
        item.delete()
        return redirect('item_list')
    return render(request, 'confirm_delete.html', {'item': item})


#student view
from django.shortcuts import render, get_object_or_404, redirect
from .models import Student
from .forms import StudentForm

# Display list of students
def student_list(request):
    students = Student.objects.all()
    return render(request, 'student_list.html', {'students': students})

# Add a new student
def add_student(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('student_list')  # Redirect after saving
    else:
        form = StudentForm()
    return render(request, 'add_edit_student.html', {'form': form, 'action': 'Add'})

# Edit an existing student
def edit_student(request, student_id):
    student = get_object_or_404(Student, pk=student_id)
    if request.method == 'POST':
        form = StudentForm(request.POST, instance=student)
        if form.is_valid():
            form.save()
            return redirect('student_list')
    else:
        form = StudentForm(instance=student)
    return render(request, 'add_edit_student.html', {'form': form, 'action': 'Edit'})

# Delete a student
def delete_student(request, student_id):
    student = get_object_or_404(Student, pk=student_id)
    if request.method == 'POST':
        student.delete()
        return redirect('student_list')
    return render(request, 'confirm_delete_student.html', {'student': student})


#usage views
from django.shortcuts import render, get_object_or_404, redirect
from .models import Usage
from .forms import UsageForm

# View for listing all usage entries
def usage_list(request):
    usages = Usage.objects.all()
    return render(request, 'usage_list.html', {'usages': usages})


# View for adding a new usage entry
def add_usage(request):
    if request.method == "POST":
        form = UsageForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('usage_list')  # Redirect to the usage list page
    else:
        form = UsageForm()
    return render(request, 'add_usage.html', {'form': form})

# View for updating an existing usage entry
def update_usage(request, pk):
    usage = get_object_or_404(Usage, pk=pk)
    if request.method == "POST":
        form = UsageForm(request.POST, instance=usage)
        if form.is_valid():
            form.save()
            return redirect('usage_list')
    else:
        form = UsageForm(instance=usage)
    return render(request, 'update_usage.html', {'form': form})

# View for deleting a usage entry
def delete_usage(request, pk):
    usage = get_object_or_404(Usage, pk=pk)
    if request.method == "POST":
        usage.delete()
        return redirect('usage_list')
    return render(request, 'delete_usage.html', {'usage': usage})



#purchasemain views
from django.shortcuts import render, redirect, get_object_or_404
from .models import PurchaseMain
from .forms import PurchaseForm  # Import form for purchase

# View to display all purchases
def purchase_list(request):
    purchases = PurchaseMain.objects.all()
    return render(request, 'purchase_list.html', {'purchases': purchases})

# View to add a new purchase
def add_purchase(request):
    if request.method == "POST":
        form = PurchaseForm(request.POST)
        if form.is_valid():
            form.save()  # Save the new purchase to the database
            return redirect('purchase_list')  # Redirect to the purchase list
    else:
        form = PurchaseForm()
    return render(request, 'add_purchase.html', {'form': form})

# View to update an existing purchase
def update_purchase(request, purchase_id):
    purchase = get_object_or_404(PurchaseMain, purchase_id=purchase_id)
    if request.method == "POST":
        form = PurchaseForm(request.POST, instance=purchase)
        if form.is_valid():
            form.save()  # Update the existing purchase
            return redirect('purchase_list')  # Redirect to the purchase list
    else:
        form = PurchaseForm(instance=purchase)
    return render(request, 'update_purchase.html', {'form': form})

# View to delete a purchase
def delete_purchase(request, purchase_id):
    purchase = get_object_or_404(PurchaseMain, purchase_id=purchase_id)
    if request.method == "POST":
        purchase.delete()  # Delete the purchase
        return redirect('purchase_list')  # Redirect to the purchase list
    return render(request, 'delete_purchase.html', {'purchase': purchase})


#purchasesub views
from django.shortcuts import render, get_object_or_404, redirect
from .models import PurchaseMain, PurchaseSub
from .forms import PurchaseSubForm

# List Sub-items for a Purchase
def purchase_sub_list(request):
    # purchase = get_object_or_404(PurchaseMain)
    # sub_items = purchase.sub_items.all()
    purchase = PurchaseSub.objects.all()
    
    return render(request, 'purchase_sub_list.html', {'purchase': purchase})

# add purchasesub
def add_purchase_sub(request):
    if request.method == 'POST':
        form = PurchaseSubForm(request.POST)
        if form.is_valid():
            form.save()  # Save the new PurchaseSub instance
            return redirect('purchase_sub_list')  # Redirect to the sub-item list
    else:
        form = PurchaseSubForm()
    return render(request, 'add_purchase_sub.html', {'form': form})


# # Edit a Sub-item
def edit_purchase_sub(request,sub_id):
    sub_item = get_object_or_404(PurchaseSub, pk=sub_id)
    if request.method == 'POST':
        form = PurchaseSubForm(request.POST, instance=sub_item)
        if form.is_valid():
            form.save()
            return redirect('purchase_sub_list')
    else:
        form = PurchaseSubForm(instance=sub_item)
    return render(request, 'edit_purchase_sub.html', {'form': form, 'sub_item': sub_item})

# Delete a Sub-item
def delete_purchase_sub(request, sub_id):
    sub_item = get_object_or_404(PurchaseSub, pk=sub_id)
    if request.method == 'POST':
        sub_item.delete()
        return redirect('purchase_sub_list')  # Redirect to the sub-item list
    return render(request, 'delete_purchase_sub.html', {'sub_item': sub_item})
