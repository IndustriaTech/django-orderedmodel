from mptt.models import MPTTModel


class OrderedMPTTModel(MPTTModel):

    class Meta:
        abstract = True

    def move_down(self):
        next = self.get_next_sibling()
        if next:
            self.__class__.objects.move_node(self, next, 'right')

    def move_up(self):
        previous = self.get_previous_sibling()
        if previous:
            self.__class__.objects.move_node(self, previous, 'left')
