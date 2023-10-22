from django.http import HttpResponse
from django.db import IntegrityError, transaction
from .models import Brand, ProductInventory, Stock

def new(request):
    try:
        Brand.objects.create(brand_id=100, name='Nike')
    except IntegrityError:
        return HttpResponse("Sorry i can't insert that.")
    return HttpResponse("Hi")


def trans(request):
    try:
        with transaction.atomic():
            ProductInventory(sku='12', upc='12', product_type_id=1, product_id=2, brand_id=1, retail_price='100.00', store_price='100.00', sale_price='100.00', weight='100').save()

            Stock.objects.create(product_inventory_id=4, units=100)
    except IntegrityError:
        return HttpResponse("error has occurred.")
    return HttpResponse("Done")

