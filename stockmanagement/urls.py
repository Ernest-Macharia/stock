from stockmanagement import views
from django.urls import path

urlpatterns = [
        
	path('', views.home, name='home'),
	path('list_items/', views.list_items, name='list_items'),
	path('add_items/', views.add_items, name='add_items'),
	path('update_items/<str:pk>/', views.update_items, name="update_items"),
	path('delete_items/<str:pk>/', views.delete_items, name="delete_items"),
	path('stock_detail/<str:pk>/', views.stock_detail, name="stock_detail"),
	path('issue_items/<str:pk>/', views.issue_items, name="issue_items"),
	path('receive_items/<str:pk>/', views.receive_items, name="receive_items"),
	path('reorder_level/<str:pk>/', views.reorder_level, name="reorder_level"),

	path('appreciate/', views.appreciate, name="appreciate"),
	path('depreciate/', views.depreciate, name="depreciate"),
	path('maintenance_dates/<str:pk>/', views.maintenance_dates, name="maintenance_dates"),
]