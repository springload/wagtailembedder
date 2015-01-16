from django.core.exceptions import ObjectDoesNotExist
from django.template.loader import render_to_string
from wagtail.wagtailsnippets.views.snippets import get_content_type_from_url_params
# from wagtail.wagtailembedder.embeds import get_embed


def embed_to_frontend_html(id, content_type_app_name, content_type_model_name):
    try:
        content_type = get_content_type_from_url_params(content_type_app_name, content_type_model_name)
        model = content_type.model_class()
        instance = model.objects.get(id=id)
    except ObjectDoesNotExist:
        return ''

    if instance is not None:
        # Render template
        return render_to_string(content_type_app_name + '/snippets/' + content_type_model_name + '.html', {
            'snippet': instance,
        })
    else:
        return ''


def embed_to_editor_html(id, content_type_app_name, content_type_model_name):
    try:
        content_type = get_content_type_from_url_params(content_type_app_name, content_type_model_name)
        model = content_type.model_class()
        instance = model.objects.get(id=id)
    except ObjectDoesNotExist:
        return ''

    if instance is not None:
        # Render template
        return render_to_string('wagtailembedder/editor/embed_editor.html', {
            'embed': instance,
            'content_type_app_name': content_type_app_name,
            'content_type_model_name': content_type_model_name,
        })
    else:
        return ''
