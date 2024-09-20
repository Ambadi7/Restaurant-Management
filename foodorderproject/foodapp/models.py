from django.db import models

# Create your models here.
class Customer(models.Model) :
    c_name = models.CharField(max_length = 200)
    c_age = models.CharField(max_length=5)
    c_email = models.CharField(max_length=20)
    c_mobileNumber = models.CharField(max_length=12)
    c_username = models.CharField(max_length=20)
    c_password = models.CharField(max_length=20)
    
class Resturant_staff(models.Model) :
    rs_username = models.CharField(max_length=20)
    rs_name = models.CharField(max_length = 200)
    rs_email = models.CharField(max_length=20)
    rs_mobileNumber = models.CharField(max_length=12)
    rs_password = models.CharField(max_length=20)
    

class Customers_complaint(models.Model) :
    c_name = models.CharField(max_length = 200)
    c_username = models.CharField(max_length=20)
    c_email = models.CharField(max_length=20)
    c_complaint = models.CharField(max_length = 200)


class fooditem(models.Model):
    food_id = models.CharField(max_length=20)
    food_name =  models.CharField(max_length=20)
    description =  models.TextField()
    category =  models.CharField(max_length=10)
    quantity = models.IntegerField()
    price = models.IntegerField()
    image =  models.ImageField()

class admin_data(models.Model):
    a_username = models.CharField(max_length=20)
    a_name = models.CharField(max_length = 200)
    a_email = models.CharField(max_length=20)
    a_password = models.CharField(max_length=20)

# class Cart(models.Model):
#     # product = models.ForeignKey(fooditem , on_delete=models.SET_NULL, null=True)
#     product = models.CharField(max_length=20)
#     image = models.ImageField()
#     quantity = models.IntegerField(default=1)
#     total_price = models.PositiveIntegerField(default=0)
#     username = models.CharField(max_length=20)
#     user_email = models.CharField(max_length=20)

class CompletedOrder(models.Model):
    username = models.CharField(max_length=20)
    food_name =  models.CharField(max_length=20)
    status =    models.CharField(max_length=20)
    category =  models.CharField(max_length=10)
    quantity = models.IntegerField()
    price = models.IntegerField()
    phnumber = models.IntegerField()
class OngoingOrder(models.Model):
    username = models.CharField(max_length=20)
    food_name =  models.CharField(max_length=20)
    status =    models.CharField(max_length=20)
    category =  models.CharField(max_length=10)
    quantity = models.IntegerField()
    price = models.IntegerField()

class Order(models.Model):
    username = models.CharField(max_length=20)
    food_name =  models.CharField(max_length=20)
    status =    models.CharField(max_length=20)
    category =  models.CharField(max_length=10)
    quantity = models.IntegerField()
    price = models.IntegerField()


class cart(models.Model):
    product = models.CharField(max_length=20)
    image = models.ImageField()
    quantity = models.IntegerField(default=1)
    total_price = models.PositiveIntegerField(default=0)
    username = models.CharField(max_length=20)
    userEmail = models.EmailField(max_length = 200)
    c_mobileNumber = models.CharField(max_length=12)

class pay(models.Model):
    price = models.IntegerField()
    c_mobileNumber = models.CharField(max_length=12)