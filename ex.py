from django.db import connection, reset_queries
from ecommerce.inventory.models import Brand, ProductInventory, Product
from pygments import highlight
from pygments.lexers import PostgresLexer
from pygments.formatters import TerminalFormatter
from sqlparse import format

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