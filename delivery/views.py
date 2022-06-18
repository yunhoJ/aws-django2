from django.shortcuts import render
from order.models import Orders
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt 
def orders(request):
    if request.method=='GET':
        order_list=Orders.objects.all()
        return render(request,"delivery/order_list.html",{"order_list":order_list})
    elif request.method=='POST':
        order_item=Orders.objects.get(pk=int(request.POST["order_id"]))
        order_item.deliver_finish=1
        order_item.save()
        return render(request, "delivery/success.html")

        