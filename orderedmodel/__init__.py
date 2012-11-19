from .models import OrderedModel
from .admin import OrderedModelAdmin

__all__ = ['OrderedModel', 'OrderedModelAdmin']

try:
    from django.conf import settings
except ImportError:
    pass
else:
    if 'mptt' in settings.INSTALLED_APPS:
        from .mptt_models import OrderableMPTTModel
        from .mptt_admin import OrderedMPTTModelAdmin
        __all__ += ['OrderableMPTTModel', 'OrderedMPTTModelAdmin']
