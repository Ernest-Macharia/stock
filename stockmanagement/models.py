
from django.db import models



class Stock(models.Model):
    
    category_choice = (
    	    ('Furniture', 'Furniture'),
    	    ('IT Equipment', 'IT Equipment'),
    	    ('Phone', 'Phone'),
    	)
    department_choice = (
            ('IT', 'IT'),
            ('Finance', 'Finance'),
            ('Human Resource', 'Human Resource'),
        )
    category = models.CharField(max_length=50, blank=True, null=True,choices=category_choice)
    department = models.CharField(max_length=50, blank=True, null=True,choices=department_choice)
    item_name = models.CharField(max_length=50, blank=True, null=True)
    quantity = models.IntegerField(default='0', blank=True, null=True)
    appreciation = models.CharField(max_length=50, blank=True, null=True)
    receive_quantity = models.IntegerField(default='0', blank=True, null=True)
    receive_by = models.CharField(max_length=50, blank=True, null=True)
    issue_quantity = models.IntegerField(default='0', blank=True, null=True)
    issue_by = models.CharField(max_length=50, blank=True, null=True)
    issue_to = models.CharField(max_length=50, blank=True, null=True)
    phone_number = models.CharField(max_length=50, blank=True, null=True)
    created_by = models.CharField(max_length=50, blank=True, null=True)
    start_date = models.DateTimeField(auto_now_add=False, auto_now=True)
    end_date = models.DateTimeField(auto_now_add=False, auto_now=True)
    reorder_level = models.IntegerField(default='0', blank=True, null=True)
    last_updated = models.DateTimeField(auto_now_add=False, auto_now=True)
    months = models.PositiveIntegerField(null=True)
    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
    export_to_CSV = models.BooleanField(default=False)

    def __str__(self):
	    return self.item_name

class Appreciate(models.Model):
    name = models.ForeignKey(Stock,null=True, on_delete=models.CASCADE)
    value = models.DecimalField(max_digits=19, decimal_places=2, null=True)
    appreciation_rate = models.PositiveIntegerField(null=True)
    months = models.PositiveIntegerField(null=True)


class Depreciate(models.Model):
    name = models.ForeignKey(Stock,null=True, on_delete=models.CASCADE)
    value = models.DecimalField(max_digits=19, decimal_places=2, null=True)
    depreciation_rate = models.PositiveIntegerField(null=True)
    months = models.PositiveIntegerField(null=True)



