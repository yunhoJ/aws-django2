from django.shortcuts import render
from user.serializers import Userserializer
from user.models import User
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse,JsonResponse

@csrf_exempt
def user(request):
    if request.method=='GET':
        user =User.objects.all()
        return render(request,'user/user_list.html',{"user_list":user})
    elif request.method=='POST':
        data=JSONParser().parse(request)
        serializer=Userserializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data ,status=201)
        return JsonResponse(serializer.errors, status=400)

@csrf_exempt
def login(request):
    if request.method=='GET':
        return render(request, "user/login.html")
    elif request.method=='POST':
        name=request.POST['name']
        try:
            request.session["user_id"]=User.objects.get(name=name).id
            print("세션 :",request.session["user_id"])
            return render( request,"user/success.html")
        except:
            return render(request,"user/fail.html")