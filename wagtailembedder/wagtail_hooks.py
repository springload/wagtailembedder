from django.conf.urls import include, url
from django.conf import settings
from django.utils.html import format_html, format_html_join
from django.core.urlresolvers import reverse

from wagtail.wagtailadmin.rich_text import HalloPlugin
from wagtail.wagtailcore import hooks

from wagtailembedder import urls
from wagtailembedder.helper import add_embed_handler


@hooks.register('register_admin_urls')
def register_admin_urls():
    add_embed_handler()
    return [
        url(r'^classembedder/', include(urls)),
    ]


@hooks.register('register_rich_text_features')
def register_snippet_feature(features):
    features.register_editor_plugin(
        'hallo',
        'snippet',
        HalloPlugin(
            name='halloembedder',
            options={'chooser': reverse('wagtailembedder_class_list')},
            js=['wagtailembedder/js/hallo-embedder.js'],
            css={'screen': ['wagtailembedder/css/admin.css']},
            order=999,
        )
    )

@hooks.register('before_serve_page')
def add_handler(page, request, serve_args, serve_kwargs):
    """
    Call add_embed_handler() to set a custom handler for embedded snippets
    """
    add_embed_handler()
