from django.core.exceptions import ObjectDoesNotExist
from django.template.loader import render_to_string

from wagtailembedder.views.snippets import get_snippet_model_from_url_params


def embed_to_frontend_html(id, content_type_app_name, content_type_model_name):
    """
    Provides the Snippet representation through the appropiate template
    """
    try:
        model = get_snippet_model_from_url_params(content_type_app_name, content_type_model_name)
        instance = model.objects.get(id=id)
    except ObjectDoesNotExist:
        return ''

    if instance is not None:
        # Render template
        template_name = '{app}/snippets/{model}.html'.format(
            app=content_type_app_name, model=content_type_model_name.lower())
        context = {'snippet': instance}
        return render_to_string(template_name, context)
    else:
        return ''


def embed_to_editor_html(id, content_type_app_name, content_type_model_name):
    """
    Provides the Snippet representation to display in the RichTextEditor
    """
    try:
        model = get_snippet_model_from_url_params(content_type_app_name, content_type_model_name)
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
