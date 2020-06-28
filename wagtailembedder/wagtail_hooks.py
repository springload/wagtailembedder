from django.conf.urls import include, url
from django.urls import reverse

from wagtail.admin.rich_text import HalloPlugin
from wagtail.core import hooks

from wagtailembedder import urls
from wagtailembedder.helper import SnippetEmbedHandler, HTMLEmbedSnippetConversionRule


@hooks.register('register_admin_urls')
def register_admin_urls():
    return [
        url(r'^classembedder/', include(urls)),
    ]


@hooks.register('register_rich_text_features')
def register_snippet_feature(features):
    # define a handler for converting <embed embedtype="snippet"> tags into frontend HTML
    features.register_embed_type(SnippetEmbedHandler)

    # Hello.js editor plugin
    features.register_editor_plugin(
        'hallo',
        'snippet',
        HalloPlugin(
            name='halloembedder',
            options={
                'modalUrl': reverse('wagtailembedder_class_list'),
            },
            js=['wagtailembedder/js/hallo-embedder.js'],
            css={'screen': ['wagtailembedder/css/admin.css']},
            order=999,
        )
    )

    # editorhtml -> DB
    features.register_converter_rule('editorhtml', 'embed', HTMLEmbedSnippetConversionRule)
