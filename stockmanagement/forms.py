from django import forms
from .models import Stock,Appreciate,Depreciate
class StockCreateForm(forms.ModelForm):
	class Meta:
		model = Stock
		fields = ['category','department', 'item_name','quantity']

	def clean_category(self):
		category = self.cleaned_data.get('category')
		if not category:
		    raise forms.ValidationError('This field is required')
		for items in Stock.objects.all():
		    if items.category == category:
		        raise forms.ValidationError(str(category) + " " + 'is already created')
		    return category

	def clean_item_name(self):
		item_name = self.cleaned_data.get('item_name')
		if not item_name:
		    raise forms.ValidationError('This field is required')
		for items in Stock.objects.all():
		    if items.item_name == item_name:
		        raise forms.ValidationError(str(item_name) + " " + 'is already created')
		    return item_name

class StockUpdateForm(forms.ModelForm):
	class Meta:
		model = Stock
		fields = ['category', 'department','item_name', 'quantity']

       

class StockSearchForm(forms.ModelForm):
	export_to_CSV = forms.BooleanField(required=False)
	class Meta:
		model = Stock
		fields = ['category', 'item_name']

class IssueForm(forms.ModelForm):
	class Meta:
		model = Stock 
		fields = ['issue_quantity', 'issue_to']

class ReceiveForm(forms.ModelForm):
    class Meta:
    	model = Stock
    	fields = ['receive_quantity','receive_by']
    	

class ReorderLevelForm(forms.ModelForm):
    class Meta:
        model = Stock
        fields = ['reorder_level']

class AppreciationForm(forms.ModelForm):
    class Meta:
        model = Appreciate
        exclude = []

class DepreciationForm(forms.ModelForm):
    class Meta:
        model = Depreciate
        exclude = []
                               
class MaintenanceForm(forms.ModelForm):
    class Meta:
        model = Stock
        fields = ['months']                                                