from django.shortcuts import render

from order.models import Shop, Menu,Orders, Order_foodlist
from order.serializers import ShopSerializer,MenuSerializer
from django.http import JsonResponse,HttpResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser

from rest_framework.parsers import JSONParser
@csrf_exempt 
def timeinput(request ,shop):
    if request.method == 'GET':
        order_list=Orders.objects.filter(shop=shop)
        return render (request, 'boss/order_list.html', {'order_list':order_list})
    elif request.method== 'POST':
        order_item=Orders.objects.get(pk=int(request.POST["order_id"]))
        order_item.estimated_time=int(request.POST["estimated_time"])
        order_item.save()
        return render (request, 'boss/success.html',{"shop_id":shop})
    else :
        return HttpResponse(status=404)