from django.shortcuts import render, get_object_or_404
from .models import sotuvchi, mahsulot
from django.http import JsonResponse
from .serializers import SellerSerializer, productSerializer

# Create your views here.
def mahsulotdetailsviews(request, mahsulot_id):
    product = get_object_or_404(mahsulot, id = mahsulot_id )
    productdetails = productSerializer(product)

    return JsonResponse(productdetails.data, safe = False)

def mahsulotallviews(request):
    allproducts = mahsulot.objects.all()
    res = productSerializer(allproducts,many = True)
    print(res,res.data)
    return JsonResponse(res.data, safe = False)

def sotuvchidetailsviews(request, sotuvchi_id):
    seller = get_object_or_404(sotuvchi, id = sotuvchi_id  )
    sellerdetails = SellerSerializer(seller)
    return JsonResponse(sellerdetails.data, safe = False)

def sotuvchiallviews(request):
    allsellers = sotuvchi.objects.all()
    res = SellerSerializer(allsellers, many = True)
    return JsonResponse(res.data, safe = False)
