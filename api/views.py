from django.shortcuts import render
from django.http import JsonResponse

from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import ProductSerializer,LocationSerializer,ProductMovementSerializer
from .models import Product,Location,ProductMovement
# Create your views here.

@api_view(['GET'])
def apiOverview(request):
	api_urls = {
		'Detail View':'/audio-detail/<str:pk>/',
		'Create':'/audio-create/',
		'Update':'/audio-update/<str:pk>/',
		'Delete':'/audio-delete/<str:pk>/',
		'Detail-start' : '/audio-detail-start/',
		}

	return Response(api_urls)
# @api_view(['GET'])
# def index(request):
# 	return render (request,'personal/home.html')

# =========================== PRODUCT  =================================== #


@api_view(['GET'])
def viewProduct(request):
	try:
		
		# print(pk,"primary key")
		# audio = Product.objects.get(product_id=pk)
		audio = Product.objects
		serializer = ProductSerializer(audio, many=True)
		print(serializer.data,"ssssss")
		prodlist=[]
		
		for key in serializer.data:
			print(key)
			print(key["product_id"])
			trans_data={
    	"id": key["product_id"],
    	"productname": key["product_name"],
   
    	}
			prodlist.append(trans_data)
			print(prodlist,"fgg")



		return Response(prodlist)
	except Exception as er:
		print(er,"errrrrrrrrr")


@api_view(['POST'])
def addProduct(request):
	try:
        
		print(request,"requesttttttttttttttt")
		print(request.data)
		serializer=ProductSerializer(data=request.data)
		print(serializer,"errttyu")
		if serializer.is_valid():
			serializer.save()
		print(serializer.data)
		return Response(
		{"id":serializer.data["product_id"],
   "productname":serializer.data["product_name"]}
   )
	except Exception as er:
		print(er,"errrrrrrrrrrr")



@api_view(['PUT'])
def editProduct(request, pk):
	audio = Product.objects.get(product_id=pk)
	serializer = ProductSerializer(instance=audio, data=request.data)
	
	if serializer.is_valid():
		serializer.save()
		context={
    "id": serializer.data["product_id"],
    "productname": serializer.data["product_name"],
   
    }

	return Response(context)

# =========================== LOCATION  =================================== #

@api_view(['GET'])
def viewLocation(request):
	try:
        
		# print(pk,"requesttttttttttttttt")
		# print(request.data,"request.dataaaaaaaaa")
		audio = Location.objects
		print(audio,"audiooooooooo")
		serializer=LocationSerializer(audio,many= True)
		
		print(serializer.data,"sdfgghhj")
		prodlist=[]

		for key in serializer.data:
			print(key)
			print(key["location_id"])
			trans_data={"id":key["location_id"],
  		 "locationname":key["location_name"]}
			prodlist.append(trans_data)
			print(prodlist)



		return Response(prodlist)
	except Exception as er:
		print(er,"errrrrrrrrrrr")

	


@api_view(['POST'])
def addLocation(request):
	try:
        
		print(request,"requesttttttttttttttt")
		print(request.data)
		serializer=LocationSerializer(data=request.data)
		print(serializer,"errttyu")
		if serializer.is_valid():
			serializer.save()
		print(serializer.data)
		return Response(
		{"id":serializer.data["location_id"],
  		 "locationname":serializer.data["location_name"]}
  		 )
	except Exception as er:
		print(er,"errrrrrrrrrrr")



@api_view(['PUT'])
def editLocation(request, pk):
	audio = Location.objects.get(location_id=pk)
	serializer = LocationSerializer(instance=audio, data=request.data)
	
	if serializer.is_valid():
		serializer.save()
		context={
    "id": serializer.data["location_id"],
    "locationname": serializer.data["location_name"],
    
    }

	return Response(context)



# =========================== PRODUCT MOVEMENT  =================================== #


@api_view(['GET'])
def viewProductMovement(request):

	try:
		
		audio = ProductMovement.objects
		serializer = ProductMovementSerializer(audio, many=True)
		print(serializer.data,"fggghj")
		prodlist=[]

		for key in serializer.data:
			print(key)
			print(key["productmovement_id"],key["timestamp"],key["from_location"],key["to_location"],key["product_id"],key["Location_id"],key["quantity"])
		trans_data={
    		"id": key['productmovement_id'],
    		"timestamp": key["timestamp"],
    		"fromlocation": key["from_location"], 
    		"to_location": key["to_location"],
    		"product_id":  key["product_id"],
    		"Location_id":  key["Location_id"],
    		"quantity":  key["quantity"],
     		}
		prodlist.append(trans_data)
		print(prodlist,"ghjhjj")
		
		return Response(prodlist)
	except  Exception as er:
		print(er)




@api_view(['POST'])
def addProductMovement(request):
	try:

		print(request.data)
		serializer = ProductMovementSerializer(data=request.data)
		print(serializer)

		if serializer.is_valid():
			serializer.save()
		print(serializer.data)
		context={
    	"id": serializer.data["productmovement_id"],
    	"timestamp": serializer.data["timestamp"],
    	"fromlocation": serializer.data["from_location"],  # High volume no overlap
    	"to_location":  serializer.data["to_location"],
    	"product_id":  serializer.data["product_id"],
    	"Location_id":  serializer.data["Location_id"],
    	"quantity":  serializer.data["quantity"],
     }
		return Response(context)
	except Exception as er:
		print(er)




@api_view(['PUT'])
def editProductMovement(request, pk):
	audio = ProductMovement.objects.get(productmovement_id=pk)
	serializer = ProductMovementSerializer(instance=audio, data=request.data)
	
	if serializer.is_valid():
		serializer.save()
		context={
    	"id": serializer.data["productmovement_id"],
    	"timestamp": serializer.data["timestamp"],
    	"fromlocation": serializer.data["from_location"],  # High volume no overlap
    	"to_location":  serializer.data["to_location"],
    	"product_id":  serializer.data["product_id"],
    	"Location_id":  serializer.data["Location_id"],
    	"quantity":  serializer.data["quantity"],
     }

	return Response(context)

# @api_view(['DELETE'])
# def audioDelete(request, pk):
	audio = Audio.objects.get(id=pk)
	audio.delete()

	return Response('Item succsesfully delete!') #throw error cuz delete


# @api_view(['GET'])
# def audioDetailWithStartTime(request):
# 	start_time= request.GET.get('start')
# 	end_time=request.GET.get('end')
# 	# audio = Audio.objects.filter(start_time=start_time,end_time=end_time)
# 	audio = Audio.objects.filter(start_time__gte=start_time).filter(end_time__lte=end_time)
# 	serializer = AudioSerializer(audio, many=True)
# 	print(serializer.data)


# 	return Response(serializer.data)


