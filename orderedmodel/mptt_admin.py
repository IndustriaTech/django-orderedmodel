from mptt.admin import MPTTModelAdmin

from .admin import BaseOrderedModelAdmin


class OrderedMPTTModelAdmin(MPTTModelAdmin, BaseOrderedModelAdmin):
    pass
