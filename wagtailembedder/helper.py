from django.core.exceptions import ObjectDoesNotExist

from wagtail.admin.rich_text.converters import editor_html
from wagtail.core.rich_text import EmbedHandler
from wagtail.embeds.models import Embed
from wagtail.embeds.embeds import get_embed

from wagtailembedder.format import embed_to_editor_html, embed_to_frontend_html
from wagtailembedder.views.snippets import get_snippet_model_from_url_params


from draftjs_exporter.dom import DOM

from wagtail.admin.rich_text.converters.contentstate_models import Entity
from wagtail.admin.rich_text.converters.html_to_contentstate import AtomicBlockEntityElementHandler
from wagtail.embeds import embeds
from wagtail.embeds.rich_text.editor_html import MediaEmbedHandler
from wagtail.embeds.exceptions import EmbedException


class SnippetEmbedHandler(EmbedHandler):
    identifier = 'snippet'

    @staticmethod
    def get_instance(attrs):
        try:
            model = get_snippet_model_from_url_params(
                attrs['app-name'],
                attrs['content-type-name']
            )
            return model.objects.get(id=id)
        except ObjectDoesNotExist:
            return ''

    @staticmethod
    def expand_db_attributes(attrs):
        """
        Given a dict of attributes from the <embed> tag, return the real HTML
        representation for use on the front-end.
        """
        return embed_to_frontend_html(attrs['id'], attrs['app-name'], attrs['content-type-name'])


class HTMLEmbedSnippetConversion:
    """
    SnippetEmbedHandler will be invoked whenever we encounter an element in HTML content
    with an attribute of data-embedtype="snippet". The resulting element in the database
    representation will be:
    <embed embedtype="snippet" id="x" app-name="xxx" content-type-name="xxx" >
    """
    @staticmethod
    def get_db_attributes(tag):
        """
        Given a tag that we've identified as a snippet embed (because it has a
        data-embedtype="snippet" attribute), return a dict of the attributes we should
        have on the resulting <embed> element.
        """
        return {
            'id': tag['data-id'],
            'app-name': tag['data-app-name'],
            'content-type-name': tag['data-content-type-name'],
        }

    @staticmethod
    def expand_db_attributes(attrs):
        """
        Given a dict of attributes from the <embed> tag, return the editor
        HTML representation.
        """
        return embed_to_editor_html(attrs['id'], attrs['app-name'], attrs['content-type-name'])


HTMLEmbedSnippetConversionRule = [
    editor_html.EmbedTypeRule('media', MediaEmbedHandler),
    editor_html.EmbedTypeRule('snippet', HTMLEmbedSnippetConversion)
]