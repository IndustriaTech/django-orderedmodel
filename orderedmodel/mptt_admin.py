from mptt.admin import MPTTModelAdmin

from .admin import BaseOrderedModelAdmin


class OrderedMPTTModelAdmin(BaseOrderedModelAdmin, MPTTModelAdmin):
    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        """
        Fix for django filer and mptt version lower than 0.5.3
        """
        return super(MPTTModelAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)
