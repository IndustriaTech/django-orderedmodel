from django.db import models
from django.core.exceptions import ValidationError


class OrderedModelManager(models.Manager):
    def swap(self, obj1, obj2):
        tmp, obj2.order = obj2.order, 0
        obj2.save(swapping=True)
        obj2.order, obj1.order = obj1.order, tmp
        obj1.save()
        obj2.save()

    def max_order(self):
        try:
            return self.order_by('-order').values_list('order', flat=True)[0]
        except IndexError:
            return 0


class OrderedModel(models.Model):
    order = models.PositiveIntegerField(blank=True, default=1, db_index=True)

    objects = OrderedModelManager()

    class Meta:
        abstract = True
        ordering = ['order']

    def save(self, swapping=False, *args, **kwargs):
        if not self.id:
            self.order = self.max_order() + 1
        if self.order == 0 and not swapping:
            raise ValidationError("Can't set 'order' to 0")
        super(OrderedModel, self).save(*args, **kwargs)

    @classmethod
    def swap(cls, obj1, obj2):
        cls.objects.swap(obj1, obj2)

    @classmethod
    def max_order(cls):
        return cls.objects.max_order()
