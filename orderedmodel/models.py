from django.db import models


class OrderedModelManager(models.Manager):
    def swap(self, obj1, obj2):
        """
        Swap places in order of two objects.
        If some of the objects is empty (mostly obj2) then do nothing
        """
        if not (obj1 and obj2):
            return
        obj1.order, obj2.order = obj2.order, obj1.order
        obj1.save()
        obj2.save()

    def max_order(self):
        try:
            return self.order_by('-order').values_list('order', flat=True)[0]
        except IndexError:
            return 0

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
            self.order = self.__class__.objects.max_order() + 1
        super(OrderedModel, self).save(*args, **kwargs)

    def move_down(self):
        self.__class__.objects.swap(self, self.get_next_by_order())

    def move_up(self):
        self.__class__.objects.swap(self, self.get_previous_by_order())

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
