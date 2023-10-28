from django.db import connection, reset_queries
from ecommerce.inventory.models import Brand, ProductInventory, Product, Media, ProductAttribute, Category
from pygments import highlight
from pygments.lexers import PostgresLexer
from pygments.formatters import TerminalFormatter
from sqlparse import format
from Customfields.models import Category, Product, Product_Category
from user.models import Person
from django.contrib.auth.models import User

reset_queries()
connection.queries

x = Brand.objects.all()


def sql(x):
    formatted = format(str(x.query), reindent=True)
    print(highlight(formatted, PostgresLexer(), TerminalFormatter()))

# Default django filter set on exact.
x = Brand.objects.filter(name__exact='acorn')
# Ignoring capital letters and making them into lower case.
x = Brand.objects.filter(name__iexact='AcOrN')

# variable in any position
x = Brand.objects.filter(name__contains='by')
# Not key sensitive
x = Brand.objects.filter(name__icontains='bY')

# Greater than or less than
x = ProductInventory.objects.filter(retail_price__gt=100)
x = ProductInventory.objects.filter(retail_price__gte=100)
x = ProductInventory.objects.filter(retail_price__lt=100)
x = ProductInventory.objects.filter(retail_price__lte=100)

# starts with and ends with
# like a%
x = Product.objects.filter(name__startswith='a')
# not key sensitive
x = Product.objects.filter(name__istartswith='a')
# like %a
x = Product.objects.filter(name__endswith='e')
# not key sensitive
x = Product.objects.filter(name__iendswith='e')

# range lookup field
x = ProductInventory.objects.filter(retail_price__range=(1, 100))
x = ProductInventory.objects.filter(created_at__range=('2020-02-02', '2021-11-02'))

# filter by day, month and year
x = ProductInventory.objects.filter(updated_at__day=1)
x = ProductInventory.objects.filter(updated_at__month=1)
x = ProductInventory.objects.filter(updated_at__year=1)
x = ProductInventory.objects.filter(updated_at__week_day=4)

# ordering
Product.objects.all().order_by('id').values('id')[:10]
x = Product.objects.all().order_by('-id').values('id')[:10]
# random---needs a lot of resources
Product.objects.all().order_by('?').values('id')[:10]

# grabbing first and last object
Product.objects.all().first()
Product.objects.all().last()

Product.objects.all().latest('id')
Product.objects.all().earliest('created_at')

ProductInventory.objects.filter(product_id=1)
ProductInventory.objects.raw("SELECT * FROM inventory_productinventory WHERE product_id=1")

Media.objects.filter(is_feature=True, product_inventory__product__id=1)
Media.objects.raw("SELECT * FROM inventory_media INNER JOIN inventory_productinventory ON inventory_media.product_inventory_id=inventory_productinventory.id WHERE inventory_media.is_feature=True AND inventory_productinventory.product_id=1")

ProductAttribute.objects.filter(product_type_attributes__product_type__id=1)
ProductAttribute.objects.raw("SELECT * FROM inventory_productattribute INNER JOIN inventory_producttypeattribute ON inventory_productattribute.id=inventory_producttypeattribute.product_attribute_id INNER JOIN inventory_producttype ON inventory_producttypeattribute.product_type_id=inventory_producttype.id WHERE inventory_producttype.id=1")
Product.objects.filter(product__attribute_values__product_attribute=1).distinct()
Product.objects.raw("SELECT * FROM inventory_product INNER JOIN inventory_productinventory ON inventory_product.id=inventory_productinventory.product_id INNER JOIN inventory_productattributevalues ON inventory_productinventory.id=inventory_productattributevalues.productinventory_id INNER JOIN inventory_productattributevalue ON inventory_productattributevalues.attributevalues_id=inventory_productattributevalue.id WHERE inventory_productattributevalue.id=1")
ProductInventory.objects.filter(product_inventory__units__lt=50)
ProductInventory.objects.raw("SELECT * FROM inventory_productinventory INNER JOIN inventory_stock ON inventory_productinventory.id=inventory_stock.product_inventory_id WHERE inventory_stock.units <= 50")
ProductInventory.objects.filter(product_inventory__last_checked__range=('2020-01-01', '2022-10-10'))
ProductInventory.objects.raw("SELECT * FROM inventory_productinventory INNER JOIN inventory_stock ON inventory_productinventory.id=inventory_stock.product_inventory_id WHERE inventory_stock.last_checked BETWEEN '2020-01-01' AND '2022-10-10'")
Product.objects.filter(product__product_type__producttype__id=1).distinct()
Brand.objects.filter(brand__product_type__product_type_attributes__id=1).distinct()


Category.objects.all()
Product.objects.all()
Product(name='test', is_active=True).save()
cat1 = Category.objects.create(name='test', slug='test1', is_active=True)
prod1 = Product(name='test', slug='test', is_active=True).save()
prod1.categories.add(cat1)
prod1 = Product.objects.create(name='test2', slug='test2', is_active=True)
prod1.categories.all()
cat1.product_set.all()  # If we dont implement related name in the model
cat = Category.objects.get(id=3)
cat.product.all() # Using related name called product that implemented in models
prod = Product.objects.get(id=3)
prod.categories.all()
# For addin additional field in link table we must use through_defaults option
prod.categories.add(cat, through_defaults={'order': 1})


Person.objects.create_user(username='test', password='T123@example')
User.objects.create_user(username='test1', password='T123@example')