from django.shortcuts import render
from order.models import Shop, Menu,Orders, Order_foodlist
from order.serializers import ShopSerializer
from django.http import JsonResponse,HttpResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser

#보안 요소 데이터 변경 제한 
@csrf_exempt 
def shop(request):
    if request.method =='GET':
        shop=Shop.objects.all()
        # serializer - database안에 있는 목록을 json파일로 변경해주는 역할
        serializer= ShopSerializer(shop,many=True)
        return JsonResponse(serializer.data,safe=False) 
    # 데이터 추가 post방식 많이 사용함 
    elif request.method =='POST':
        data=JSONParser().parse(request)
        serializer=ShopSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data,status=201)
        return JsonResponse(serializer.errors,status=400)
