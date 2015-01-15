from django.conf.urls import url

from wagtailembedder.views import chooser


urlpatterns = [
    url(r'^chooser/snippet_types/$', chooser.index, name='wagtailembedder_class_list'),
    url(r'^chooser/snippet_objects/(\w+)/(\w+)/$', chooser.index_objects, name='wagtailembedder_class_chosen'),
]
