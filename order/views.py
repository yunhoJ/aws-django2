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
        return render (request, 'order/menu_list.html', {'menu_list':menu,"shop_title":shop_title})
    
    elif request.method =='POST':
        data=JSONParser().parse(request)
        serializer=MenuSerializer(data=data)
        #데이터 베이스 형식에 맞으면 save
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data,status=201)
        return JsonResponse(serializer.errors,status=400)
