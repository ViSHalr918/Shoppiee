from django.contrib import admin

# Register your models here.

from .models import Product,OrderSummary

admin.site.register(Product)
admin.site.register(OrderSummary)