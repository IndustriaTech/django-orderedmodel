from django.db import models


def get_max_order(manager):
    try:
        return manager.order_by('-order').values_list('order', flat=True)[0]
    except IndexError:
        return 0


class OrderedModelManager(models.Manager):
    def swap(self, obj1, obj2):
        """
        Swap places in order of two objects.
        If some of the objects is empty (mostly obj2) then do nothing
        """
        if not (obj1 and obj2):
            return
        if not (isinstance(obj1, self.model) and isinstance(obj2, self.model)):
            raise TypeError("%r and %r must be instances of %r" %
                            (obj1, obj2, self.model))
        obj1.order, obj2.order = obj2.order, obj1.order
        obj1.save()
        obj2.save()

    def max_order(self):
        return get_max_order(self)

    def fix_ordering(self):
        """
        This method must be executed only if this application is
        added to existing project.
        """
        for index, item in enumerate(self.only('order'), 1):
            item.order = index
            item.save()


class OrderedModel(models.Model):
    order = models.PositiveIntegerField(blank=True, default=1, db_index=True)

    objects = OrderedModelManager()

    class Meta:
        abstract = True
        ordering = ['order']

    def save(self, *args, **kwargs):
        if not self.id:
            self.order = get_max_order(self.__class__.objects) + 1
        super(OrderedModel, self).save(*args, **kwargs)

    def move_down(self):
        self.swap(self.get_next_by_order())

    def move_up(self):
        self.swap(self.get_previous_by_order())

    def swap(self, obj):
        """
        Swap places in order of two objects.
        If some of the objects is empty (mostly obj2) then do nothing
        """
        if not (obj):
            return
        if not (isinstance(obj, self.__class__)):
            raise TypeError("%r must be instances of %r" %
                            (obj, self.__class__))
        self.order, obj.order = obj.order, self.order
        self.save()
        obj.save()

    def get_next_by_order(self):
        try:
            return self.__class__.objects.filter(order__gt=self.order).order_by('order')[0]
        except IndexError:  # Last item
            return

    def get_previous_by_order(self):
        try:
            return self.__class__.objects.filter(order__lt=self.order).order_by('-order')[0]
        except IndexError:  # First item
            return
