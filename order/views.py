from django.shortcuts import render

from order.models import Shop, Menu,Orders, Order_foodlist
from order.serializers import ShopSerializer,MenuSerializer
from django.http import JsonResponse,HttpResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser

#보안 요소 데이터 변경 제한 
@csrf_exempt 
def shop(request):
    if request.method =='GET':
        # 해당 코드는 json형태로 출력되기때문에 템플릿으로 코드 변경 
        # shop=Shop.objects.all()
        # # serializer - database안에 있는 목록을 json파일로 변경해주는 역할
        # serializer= ShopSerializer(shop,many=True)
        # return JsonResponse(serializer.data,safe=False) 

        shop=Shop.objects.all()
        return render (request, 'order/shop_list.html', {'shop_list':shop})
        
    elif request.method =='POST':
        data=JSONParser().parse(request)
        serializer=ShopSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data,status=201)
        return JsonResponse(serializer.errors,status=400)

@csrf_exempt 
def menu(request,shop):
    if request.method =='GET':
        #Menu.objects.get은 하나만 불러올수 있음 
        menu=Menu.objects.filter(shop=shop)
        # serializer=MenuSerializer(menu,many=True)
        # return JsonResponse(serializer.data,safe=False) 
        shop_title=Shop.objects.get(id=shop)
        return render (request, 'order/menu_list.html', {'menu_list':menu,"shop_title":shop_title,})
    
    elif request.method =='POST':
        data=JSONParser().parse(request)
        serializer=MenuSerializer(data=data)
        #데이터 베이스 형식에 맞으면 save
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data,status=201)
        return JsonResponse(serializer.errors,status=400)

from django.utils import timezone
@csrf_exempt 
def order(request):
    if request.method=="POST":
        address=request.POST['address']
        shop=request.POST['shop']
        order_date= timezone.now()
        food_list=request.POST.getlist('menu')

        shop_item=Shop.objects.get(pk=int(shop))
        shop_item.orders_set.create(address=address,order_date=order_date,shop=int(shop))
        
        order_item=Orders.objects.get(pk=shop_item.orders_set.latest('id').id)# 오더 테이블 상 마지막 id
        for food in food_list:
           order_item.order_foodlist_set.create(food_name=food)   
        return render (request, 'order/success.html')
    elif request.method=='GET':
        order_list=Orders.objects.all()
        return render (request, 'order/order_list.html', {'order_list':order_list})