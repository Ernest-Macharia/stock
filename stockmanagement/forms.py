from django import forms
from .models import Stock
class StockCreateForm(forms.ModelForm):
	class Meta:
		model = Stock
		fields = ['category','item_name','quantity']

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
		fields = ['category', 'item_name', 'quantity']

       

class StockSearchForm(forms.ModelForm):
	export_to_CSV = forms.BooleanField(required=False)
	class Meta:
		model = Stock
		fields = ['category', 'item_name']
                                                