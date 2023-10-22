from django.db import connection, reset_queries
from pygments import highlight
from pygments.lexers import PostgresLexer
from pygments.formatters import TerminalFormatter
from sqlparse import format
from ecommerce.inventory.models import Brand, ProductInventory, Product, Category, Stock, ProductAttribute
from django.core.exceptions import ObjectDoesNotExist, MultipleObjectsReturned

x = Brand.objects.all().query
print(x)

cursor = connection.cursor()
x = cursor.execute('SELECT * FROM inventory_brand')

x = Brand.objects.raw('SELECT * FROM inventory_brand')

try:
    x = Brand.objects.get(id=15)
    print(x.name)
except ObjectDoesNotExist:
    print("Does not exist")

x = Brand.objects.raw("SELECT * FROM inventory_brand WHERE id=1 OR id=2")
for i in x:
    print(i.id, i.name)

x = Brand.objects.filter(id=1)
x = Brand.objects.filter(id=1, name='361')
x = Brand.objects.filter(id=1, name='361') | Brand.objects.filter(id=2)
x = Brand.objects.filter(id__gt=1)
x = Brand.objects.filter(id__gte=1)
x = Brand.objects.filter(id__lt=2)
x = Brand.objects.filter(id__lte=2)
x = Brand.objects.filter(name__startswith='a')
x = Brand.objects.exclude(name__startswith='a')

x = Brand.objects.raw("SELECT * FROM inventory_brand WHERE id=1")
x = Brand.objects.raw("SELECT * FROM inventory_brand WHERE id=1 AND name='361'")
x = Brand.objects.raw("SELECT * FROM inventory_brand WHERE id=1 AND name='361' OR id=2")
x = Brand.objects.raw("SELECT * FROM inventory_brand WHERE id=1 AND name='361' OR id=2 OR NOT id=8")

ProductInventory.objects.filter(brand__name='a.x.n.y.')
Product.objects.filter(category__name='boots')
Category.objects.filter(category__name='lips too too effort tan anke boot')
ProductInventory.objects.filter(product__category__name='heels')
Category.objects.filter(category__product__id=12)

x = ProductInventory.objects.raw("SELECT * FROM inventory_productinventory INNER JOIN inventory_product ON inventory_productinventory.product_id=inventory_product.id INNER JOIN inventory_category ON inventory_product.category_id=inventory_category.id WHERE inventory_category.name='heels'")

formatted = format(str(x.query), reindent=True)
print(highlight(formatted, PostgresLexer(), TerminalFormatter()))

ProductInventory.objects.filter(product_inventory__units__gt='50')
Stock.objects.filter(product_inventory__sku__gt=6327000212)

ProductInventory.objects.filter(attribute_values__product_attribute__name="woman-shoe-size")
ProductAttribute.objects.filter(product_attribute__product_attribute_values__id=1)
ProductAttribute.objects.filter(product_type_attributes__product_type__id=1)
ProductInventory.objects.filter(attribute_values__product_attribute__name='woman-shoe-size')