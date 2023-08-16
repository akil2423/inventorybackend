from django.urls import path
from . import views

urlpatterns = [
	path('', views.apiOverview, name="api-overview"),
	# path('viewProduct/<str:pk>', views.viewProduct, name="viewProduct"),
	path('viewProduct/', views.viewProduct, name="viewProduct"),
	path('addProduct', views.addProduct, name="addProduct"),
 	path('editProduct/<str:pk>', views.editProduct, name="editProduct"),
     path('viewLocation/', views.viewLocation, name="viewLocation"),
	path('addLocation', views.addLocation, name="addLocation"),
 	path('editLocation/<str:pk>', views.editLocation, name="editLocation"),
     path('viewProductMovement/', views.viewProductMovement, name="viewProductMovement"),
	path('addProductMovement/', views.addProductMovement, name="addProductMovement"),
 	path('editProductMovement/<str:pk>', views.editProductMovement, name="editProductMovement"),
    



]
