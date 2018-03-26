from django.conf.urls import include, url
from django.conf import settings
from django.utils.html import format_html, format_html_join

import wagtail
from wagtailembedder import urls
from wagtailembedder.helper import add_embed_handler

try:
    from django.urls import reverse
except ImportError:  # Django < 2.0
    from django.core.urlresolvers import reverse

try:
    from wagtail.admin.rich_text import HalloPlugin
    from wagtail.core import hooks
except ImportError:  # Wagtail < 2.0
    from wagtail.wagtailadmin.rich_text import HalloPlugin
    from wagtail.wagtailcore import hooks


@hooks.register('register_admin_urls')
def register_admin_urls():
    add_embed_handler()
    return [
        url(r'^classembedder/', include(urls)),
    ]


@hooks.register('insert_editor_js')
def editor_js():
    """
    Add extra JS files to the admin to register the plugin and set the reversed URL in JS vars
    """

    return format_html("""
            <script>
                /*registerHalloPlugin('halloembedder');*/
                window.embedderChooserUrls = [];
                window.embedderChooserUrls.embedderChooser = '{0}';
            </script>
        """, reverse('wagtailembedder_class_list')
    )


# @hooks.register('insert_editor_css')
# def editor_css():
#     """
#     Add extra CSS files to the admin.
#     """
#     css_files = [
#         'wagtailembedder/css/admin.css',
#     ]
#     css_includes = format_html_join(
#         '\n', '<link rel="stylesheet" href="{0}{1}">', ((settings.STATIC_URL, filename) for filename in css_files))

#     return css_includes


@hooks.register('register_rich_text_features')
def register_snippet_feature(features):
    # features.default_features.append('snippet')

    features.register_editor_plugin(
        'hallo',
        'snippet',
        HalloPlugin(
            name='halloembedder',
            js=['wagtailembedder/js/hallo-embedder.js'],
            css=['wagtailembedder/css/admin.css'],
        )
    )

# @hooks.register('before_serve_page')
# def add_handler(page, request, serve_args, serve_kwargs):
#     """
#     Call add_embed_handler() to set a custom handler for embedded snippets
#     """
#     add_embed_handler()
