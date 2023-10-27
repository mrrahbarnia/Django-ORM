from django.db import models
from django.db.models import Model
from django.core.exceptions import ObjectDoesNotExist

class ProductIdField(models.CharField):

    def __init__(self, *args, **kwargs):
        kwargs['max_length'] = 10
        kwargs['unique'] = True
        super().__init__(*args, **kwargs)

class OrderField(models.IntegerField):

    def pre_save(self, model_instance, add):
        if getattr(model_instance, self.attname) is None:
            try:
                x = self.model.objects.latest(self.attname)
                value = x.order + 1
            except ObjectDoesNotExist:
                value = 1
            setattr(model_instance, self.attname, value)
            return value
        else:
            return super().pre_save(model_instance, add)