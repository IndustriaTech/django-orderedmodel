`django-orderedmodel` -- orderable models for [Django](http://www.djangoproject.com/)
========================================================

`django-orderedmodel` intends to help you create Django models which can be
moved up\\down (or left\\right) with respect to each other.

This is a clone of [original django-ordermodel](https://github.com/kirelagin/django-orderedmodel), with added new features

How to use
-------------

There are a few simple steps to follow to make your models orderable:

1. Add django-ordered model to your enviroment
  * With [pip](http://www.pip-installer.org/en/latest/)
    - `pip install git+git://github.com/MagicSolutions/django-orderedmodel.git`.
  * Without pip
    - `git clone git://github.com/MagicSolutions/django-orderedmodel.git`.
    - Copy (or, even better, symlink) `orderedmodel` directory to your
      Django project.
2. Add `'orderedmodel'` to `INSTALLED_APPS` in your `settings.py`.
3. Ensure that your project is [using `django.contrib.staticfiles`](https://docs.djangoproject.com/en/dev/howto/static-files/)
   to serve static content
4. Derive your Model from `orderedmodel.OrderedModel`.
5. Derive your ModelAdmin from `orderedmodel.OrderedModelAdmin`.
6. Enjoy!

Now you can use `order_by('order')` in your query to get instances of your model
in desired order (actually it is not neccessary to call `order_by` explicitly
unless you have changed default ordering in your model's Meta).

Example
-------

Suppose you have a django app called _testapp_.
You need an orderable model `TestModel`.

**models.py**:

```python
from django.db import models
from orderedmodel import OrderedModel

class TestModel(OrderedModel):
  name = models.CharField(max_length=30)
```

**admin.py**:

```python
from django.contrib import admin
from orderedmodel import OrderedModelAdmin

from testapp.models import TestModel


class TestModelAdmin(OrderedModelAdmin):
  list_display = ['name', 'reorder']

admin.site.register(TestModel, TestModelAdmin)
```


Yep! Now if you create several instances of your model
and look into admin site you'll see something like this:

![Admin screenshot](http://kirelagin.ru/~kirrun/orderedmodel/admin.png)

Django versions
---------------

Current version of `django-orderedmodel` requires *Django-1.3+*.


Django-MPTT
-----------

Now there is a basic supoort of [django-mptt](http://django-mptt.github.com/django-mptt/). If you want to make simple reordering in admin and to use mptt for tree structure, you can use `orderedmodel.OrderableMPTTModel` and `orderedmodel.OrderedMPTTModelAdmin` instead of `orderedmodel.OrderedModel` and `orderedmodel.OrderedModelAdmin`

