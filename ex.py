from django.db import connection, reset_queries
from inventory.models import Brand, ProductInventory, ProductType, Product, Category
from sqlparse import format
from pygments import highlight
from pygments.formatters import TerminalFormatter
from pygments.lexers import PostgresLexer
from django.db import IntegrityError

connection.queries
x = Brand.objects.filter(name="Rebook")

def sql(x):
    sqlformatted = format(str(x.query), reindent=True)
    print(highlight(sqlformatted, PostgresLexer(), TerminalFormatter()))

# Return a dictionary by values utility
x = Brand.objects.filter(name="Rebook").values()
x = Brand.objects.filter(name="Rebook").values("name")

Brand.objects.create(brand_id=1, name="Nike")
Brand(brand_id=15, name="Adidas").save()

try:
    Brand.objects.create(brand_id=4, name="D&G2")
except IntegrityError:
    print("I cant")

cursor = connection.cursor()
cursor.execute('INSERT INTO inventory_brand(brand_id, name, nickname) VALUES (%s, %s, %s)',('1', 'Nike', ''))

ProductType().save()
Product.objects.create(web_id=1)
ProductInventory(sku='123', upc='123', product_type_id=1, product_id=2, brand_id=1, retail_price='100.00', store_price='100.00', sale_price='100.00', weight='100').save()

cursor.execute("INSERT INTO inventory_productinventory(sku,upc,product_type_id,product_id,brand_id,is_active,is_default,retail_price,store_price,sale_price,is_on_sale,is_digital,weight,created_at,updated_at) VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",['1234','1234',1,1,1,True,True,'100','100','100',True,True,'100','2023-10-21 12:29:49.153383','2023-10-21 12:29:49.153383'])

x = Category(name='Cat1', slug='123')
x = Category(name='Cat2', slug='121')

Product.objects.create(web_id='2', slug='123', name='slug')

y = Product.objects.get(id=2)
x = Category.objects.all()
y.category.add(*x)

# Inserting a list into a single table using bulk method
data = [
    {'brand_id': 1, 'name': 'Rebook'},
    {'brand_id': 2, 'name': 'Nike'}
]
Brand.objects.bulk_create([Brand(**x) for x in data])

def insert_multiple_bulk_create():
    Brand.objects.bulk_create([Brand(brand_id=n, name=n) for n in range(10000)])

# Tool for calculate a performance of inserting data into the database
import cProfile
profile = cProfile.Profile()
profile.runcall(insert_multiple_bulk_create)
profile.print_stats(sort='tottime')

# generating fixtures automatically
python manage.py dumpdata > db.json # entire project
python manage.py dumpdata inventory > db.json # only an app
python manage.py dumpdata inventory.brand > db.json # only an app
python manage.py dumpdata inventory.brand --indent 2 > db.json # only an app with appropriate indent
