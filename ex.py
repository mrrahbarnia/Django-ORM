from django.db import connection, reset_queries
from pygments import highlight
from pygments.lexers import PostgresLexer
from pygments.formatters import TerminalFormatter
from sqlparse import format
from ecommerce.inventory.models import Brand, ProductInventory, Product, Category, Stock, ProductAttribute
from django.core.exceptions import ObjectDoesNotExist, MultipleObjectsReturned

# Updating
Brand.objects.filter(id__range=(1, 5)).update(name="NewBrand")
Brand.objects.update_or_create(name='Nothing')
Brand.objects.update_or_create(name='Nothing', defaults={'name': 'edited'})

data = [(1, 'c'), (2, 'd')]
data_ids = [id for id, name in data]
updating_objects = Brand.objects.filter(id__in=data_ids)
update_list = []
for obj in updating_objects:
    obj.name = next(name for id, name in data if id==obj.id)
    update_list.append(obj)

Brand.objects.bulk_update(update_list, ['name'])

# Deleting
Brand.objects.all().delete()