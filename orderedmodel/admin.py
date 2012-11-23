# -*- coding: utf-8 -*-

from django.contrib import admin
from django.conf import settings
try:
    from django.conf.urls import patterns
except:
    from django.conf.urls.defaults import patterns
from django.shortcuts import get_object_or_404
from django.http import HttpResponseRedirect


class BaseOrderedModelAdmin(admin.ModelAdmin):

    def __init__(self, model, admin_site):
        super(BaseOrderedModelAdmin, self).__init__(model, admin_site)
        if 'reorder' not in self.list_display:
            self.list_display = list(self.list_display) + ['reorder']

    def get_urls(self):
        my_urls = patterns('',
                (r'^(?P<pk>\d+)/move_up/$', self.admin_site.admin_view(self.move_up)),
                (r'^(?P<pk>\d+)/move_down/$', self.admin_site.admin_view(self.move_down)),
        )
        return my_urls + super(BaseOrderedModelAdmin, self).get_urls()

    def reorder(self, item):
        button = '<a href="{{0}}/move_{{1}}"><img src="{0}orderedmodel/arrow-{{1}}.gif" alt="{{1}}" /></a>'.format(settings.STATIC_URL)

        html = ''
        html += button.format(item.pk, 'down')
        html += '&nbsp;' + button.format(item.pk, 'up')
        return html
    reorder.allow_tags = True

    def move_down(self, request, pk):
        if self.has_change_permission(request):
            item = get_object_or_404(self.model, pk=pk)
            item.move_down()
        return HttpResponseRedirect('../../')

    def move_up(self, request, pk):
        if self.has_change_permission(request):
            item = get_object_or_404(self.model, pk=pk)
            item.move_up()
        return HttpResponseRedirect('../../')


class OrderedModelAdmin(BaseOrderedModelAdmin):
    ordering = ['order']
    exclude = ['order']


class OrderedStackedInline(admin.StackedInline):
    class Media:
        js = (
            "orderedmodel/jquery.init.js",
            "cms/js/libs/jquery.ui.core.js",
            "cms/js/libs/jquery.ui.sortable.js",
            "orderedmodel/jquery.inlineordering.js",
            )


class OrderedTabularInline(admin.TabularInline):
    class Media:
        js = (
            "orderedmodel/jquery.init.js",
            "cms/js/libs/jquery.ui.core.js",
            "cms/js/libs/jquery.ui.sortable.js",
            "orderedmodel/jquery.inlineordering.js",
            )
