from django.shortcuts import render, get_object_or_404
from .models import sotuvchi, mahsulot
from django.http import JsonResponse

# Create your views here.
def mahsulotdetailsviews(request, mahsulot_id):
    product = get_object_or_404(mahsulot, id = mahsulot_id )
    productdetails = {
        'nomi': product.nomi,
        'ishlab chiqarilgan sana' : product.ics,
        'miqdori' : product.miqdori,
        'egasi' :  product.owner
    }

    return JsonResponse(productdetails, safe = False)

def mahsulotallviews(request):
    allproducts = mahsulot.objects.all()
    res = []

    for i in allproducts:
        res.append({
            'nomi' : i.nomi,
            'ishlab chiqarilgan sana' : i.ics,
            'miqdori' : i.miqdori,
            'egasi' : i.owner
        })
    
    return JsonResponse(res, safe = False)

def sotuvchidetailsviews(request, sotuvchi_id):
    seller = get_object_or_404(sotuvchi, id = sotuvchi_id  )
    sellerdetails = {
        'ism': seller.ism,
        'familiya' : seller.familiya,
        'tugilgan sana' : seller.tugilgan_sana,
    }

    return JsonResponse(sellerdetails, safe = False)

def sotuvchiallviews(request):
    allsellers = sotuvchi.objects.all()
    res = []

    for i in allsellers:
        res.append({
            'ism' : i.ism,
            'familiya' : i.familiya,
            'tugilgan sana' : i.tugilgan_sana,
        })
    
    return JsonResponse(res, safe = False)
