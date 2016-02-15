from wagtail.wagtailcore.rich_text import EMBED_HANDLERS

from wagtailembedder.format import embed_to_editor_html, embed_to_frontend_html


class SnippetEmbedHandler(object):
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
    def expand_db_attributes(attrs, for_editor):
        """
        Given a dict of attributes from the <embed> tag, return the real HTML
        representation.
        """
        if for_editor:
            return embed_to_editor_html(attrs['id'], attrs['app-name'], attrs['content-type-name'])
        else:
            return embed_to_frontend_html(attrs['id'], attrs['app-name'], attrs['content-type-name'])


def add_embed_handler():
    """
    Add our own SnippetEmbedHandler into the wagtailcore EMBED_HANDLERS var
    """
    EMBED_HANDLERS['snippet'] = SnippetEmbedHandler
    return True
