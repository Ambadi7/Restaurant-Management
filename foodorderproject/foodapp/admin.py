from django.contrib import admin
from.models import Customer
from.models import Resturant_staff
from.models import Customers_complaint
from.models import fooditem
from.models import admin_data
from.models import cart
from.models import CompletedOrder
from.models import OngoingOrder
from.models import Order
from.models import pay


# Register your models here.

admin.site.register(Customer)
admin.site.register(Resturant_staff)
admin.site.register(Customers_complaint)
admin.site.register(fooditem)
admin.site.register(admin_data)
admin.site.register(cart)
admin.site.register(CompletedOrder)
admin.site.register(OngoingOrder)
admin.site.register(Order)
admin.site.register(pay)
