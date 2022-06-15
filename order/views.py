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
def menu(request):
    if request.method =='GET':
        menu=Menu.objects.all()
        serializer=MenuSerializer(menu,many=True)# many=True 는 mune데이터가 여러개라도 상관안함 없으면 상관함 
        return JsonResponse(serializer.data,safe=False) 
    
    elif request.method =='POST':
        data=JSONParser().parse(request)
        serializer=MenuSerializer(data=data)
        #데이터 베이스 형식에 맞으면 save
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data,status=201)
        return JsonResponse(serializer.errors,status=400)
