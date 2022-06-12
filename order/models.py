from django.db import models

# 데이터 베이스를 다루기 위해
# pk 자동 생성 id로
class Shop (models.Model):
    shop_name=models.CharField(max_length=20)
    shop_address=models.CharField(max_length=40)

class Menu(models.Model):
    #shop을 fk로 참조 ,shop이사라지면 삭제
    shop=models.ForeignKey(Shop,on_delete=models.CASCADE)
    food_name=models.CharField(max_length=20)

#
class Orders(models.Model):
    shop=models.ForeignKey(Shop,on_delete=models.CASCADE)
    order_date=models.DateTimeField('date ordered')
    address=models.CharField(max_length=40)
    # 배송 예상시간 기본값-1 사장님이 입력하면 변경
    estimated_time=models.IntegerField(default=-1)
    deliver_finish=models.BooleanField(default=0)



class Order_foodlist(models.Model):
    order=models.ForeignKey(Orders,on_delete=models.CASCADE)
    food_name=models.CharField(max_length=20)