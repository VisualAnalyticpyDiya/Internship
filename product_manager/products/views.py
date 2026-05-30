from django.shortcuts import render
from django.http import JsonResponse
from .models import Product
import json
from django.views.decorators.csrf import csrf_exempt

def product_page(request):
    all_products = Product.objects.all()
    return render(request, 'products/list.html', {'products':all_products})
@csrf_exempt
def product_api(request):
    if request.method == 'GET':
        data = list(Product.objects.values())
        return JsonResponse(data, safe=False)
    elif request.method == 'POST':
        body = json.loads(request.body)
        if float(body.get('price', 0)) <=0:
            return JsonResponse('price must be greater than 0', status=400)
        new_product =Product.objects.create(
             name=body['name'],
            price=body['price'],
            stock=body['stock']
        )
        return JsonResponse({'message': 'product successfully added!', 'id': new_product.id}, status=201)
        
    return JsonResponse({'message': 'Invalid request method'},status=400)

