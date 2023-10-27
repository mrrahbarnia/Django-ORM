from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=10)
    slug = models.SlugField()
    is_active = models.BooleanField()

    class Meta:
        verbose_name_plural = 'categories'

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=10)
    description = models.TextField()
    slug = models.SlugField()
    is_active = models.BooleanField()
    categories = models.ManyToManyField(
        Category, related_name='product', through='Product_Category'
    )

    def __str__(self):
        return self.name


class Product_Category(models.Model):
    product = models.ForeignKey(
        Product, related_name='product', on_delete=models.CASCADE
    )
    category = models.ForeignKey(
        Category, related_name='category', on_delete=models.CASCADE
    )
    # Example of additional fields in link table
    order = models.IntegerField()

    class Meta:
        unique_together = ("product", "category")
        verbose_name_plural = 'product_categories'
    
    def __str__(self):
        return f'product_id: {self.product_id}, category_id: {self.category_id}'