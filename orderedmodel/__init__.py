from .models import OrderedModel
from .admin import OrderedModelAdmin

VERSION = (0, 1, 4)
__version__ = '.'.join(map(str, VERSION))

__all__ = ['OrderedModel', 'OrderedModelAdmin']

try:
    from django.conf import settings
except ImportError:
    pass
else:
    if 'mptt' in settings.INSTALLED_APPS:
        from .mptt_models import OrderedMPTTModel
        from .mptt_admin import OrderedMPTTModelAdmin
        __all__ += ['OrderedMPTTModel', 'OrderedMPTTModelAdmin']
