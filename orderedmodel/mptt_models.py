from mptt.models import MPTTModel


class OrderableMPTTModel(MPTTModel):

    class Meta:
        abstract = True

    def move_down(self):
        self.__class__.objects.move_node(self, self.get_next_sibling(), 'right')

    def move_up(self):
        self.__class__.objects.move_node(self, self.get_previous_sibling(), 'left')
