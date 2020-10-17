from django.shortcuts import render, redirect
from django.http import HttpResponse
import csv
from django.contrib import messages
from .models import Stock, Appreciate, Depreciate
from .forms import StockCreateForm, StockSearchForm, StockUpdateForm, IssueForm, ReceiveForm, ReorderLevelForm, AppreciationForm, DepreciationForm,MaintenanceForm
from django.contrib.auth.decorators import login_required
def home(request):
	title = 'Welcome: This is the Home Page'
	context = {
	"title": title,
	}
	return render(request, "home.html",context)
@login_required
def list_items(request):
	title = 'List of Items'
	form = StockSearchForm(request.POST or None)
	queryset = Stock.objects.all()
	context = {
		"title": title,
		"queryset": queryset,
		"form": form,
	}
	if request.method == 'POST':
	    if form['export_to_CSV'].value() == True:
		    response = HttpResponse(content_type='text/csv')
		    response['Content-Disposition'] = 'attachment; filename="List of stock.csv"'
		    writer = csv.writer(response)
		    writer.writerow(['CATEGORY', 'ITEM NAME', 'QUANTITY'])
		    instance = queryset
		    for stock in instance:
			    writer.writerow([stock.category, stock.item_name, stock.quantity])
	    return response
	    queryset = Stock.objects.filter(category__icontains=form['category'].value(),
									item_name__icontains=form['item_name'].value())
	    context = {
	    "form": form,
	    
	    "queryset": queryset,
	    }
	return render(request, "list_item.html", context)
@login_required
def add_items(request):
	form = StockCreateForm(request.POST or None)
	if form.is_valid():
		form.save()
		messages.success(request, 'Item successfully added')
		return redirect('/list_items')
	context = {
		"form": form,
		"title": "Add Item",
	}
	return render(request, "add_items.html", context)
@login_required
def update_items(request, pk):
	queryset = Stock.objects.get(id=pk)
	form = StockUpdateForm(instance=queryset)
	if request.method == 'POST':
		form = StockUpdateForm(request.POST, instance=queryset)
		if form.is_valid():
			form.save()
			messages.success(request, 'Item successfully updated')
			return redirect('/list_items')

	context = {
		'form':form
	}
	return render(request, 'add_items.html', context)
@login_required
def delete_items(request, pk):
	queryset = Stock.objects.get(id=pk)
	if request.method == 'POST':
		queryset.delete()
		messages.success(request, 'Item deleted successfully')
		return redirect('/list_items')
	return render(request, 'delete_items.html')
@login_required
def stock_detail(request, pk):
	queryset = Stock.objects.get(id=pk)
	context = {
	    'title': queryset.item_name,
	    'queryset': queryset
	}
	return render(request, 'detail_page.html', context)
@login_required
def issue_items(request, pk):
	queryset = Stock.objects.get(id=pk)
	form = IssueForm(request.POST or None, instance=queryset)
	if form.is_valid():
		instance = form.save(commit=False)
		instance.quantity -= instance.issue_quantity
		instance.issue_by = str(request.user)
		messages.success(request, "ITEM SUCCESSFULLY ISSUED." + str(instance.quantity) + "" + str(instance.item_name) + "is now left in store")
		instance.save() 
		return redirect('stock_detail', str(instance.id))
	context = {
        'title': 'Issue ' + str(queryset.item_name),
        'queryset': queryset,
        'form': form,
        'username': 'Issued By: ' + str(request.user)
	}
	return render(request, "add_items.html", context)
@login_required
def receive_items(request, pk):
	queryset = Stock.objects.get(id=pk)
	form = ReceiveForm(request.POST or None, instance=queryset)
	if form.is_valid():
		instance = form.save(commit=False)
		instance.quantity += instance.issue_quantity
		instance.issue_by = str(request.user)
		messages.success(request, "ITEM SUCCESSFULLY RECEIVED." + str(instance.quantity) + "" + str(instance.item_name) + "is now in store")
		instance.save() 
		return redirect('stock_detail', str(instance.id))
	context = {
        'title': 'Receive ' + str(queryset.item_name),
        'queryset': queryset,
        'form': form,
        'username': 'Received By: ' + str(request.user)
	}
	return render(request, "add_items.html", context)
@login_required
def reorder_level(request, pk):
	queryset = Stock.objects.get(id=pk)
	form = ReorderLevelForm(request.POST or None, instance=queryset)
	if form.is_valid():
		instance = form.save(commit=False)
		instance.save()
		messages.success(request, "Reorder level for " + str(instance.item_name) + " is updated to " + str(instance.reorder_level))
		return redirect("list_items")
	context = {
	    "instance": queryset,
	    "form": form,
	}
	return render(request, "add_items.html", context)
@login_required
def appreciate(request):
	title = "Calculate appreciation"
	
	form = AppreciationForm(request.POST or None)
	if form.is_valid():
		form.save()
		
		return redirect('/list_items')
	context = {
		"form": form,
		"title": "Calculate Appreciation",
	}
	return render(request, "appreciate.html", context)
	
	
@login_required
def depreciate(request):
	title = "Calculate depreciation"
	
	form = DepreciationForm(request.POST or None)
	if form.is_valid():
		form.save()
		
		return redirect("list_items")
	context = {
	    
	    "form": form,
	    "title": title,
	}
	return render(request, "depreciate.html", context)

@login_required
def maintenance_dates(request, pk):
	queryset = Stock.objects.get(id=pk)
	form = MaintenanceForm(request.POST or None, instance=queryset)
	if form.is_valid():
		instance = form.save(commit=False)
		instance.save()
		messages.success(request, "Reorder level for " + str(instance.item_name) + " is updated to " + str(instance.reorder_level))
		return redirect("list_items")
	context = {
	    "instance": queryset,
	    "form": form,
	}
	return render(request, "add_items.html", context)