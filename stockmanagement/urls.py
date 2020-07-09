from stockmanagement import views
from django.urls import path

urlpatterns = [
        
	path('', views.home, name='home'),
	path('list_items/', views.list_items, name='list_items'),
	path('add_items/', views.add_items, name='add_items'),
	path('update_items/<str:pk>/', views.update_items, name="update_items"),
	path('delete_items/<str:pk>/', views.delete_items, name="delete_items"),
]