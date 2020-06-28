from django.contrib.auth.decorators import permission_required
from django.core.exceptions import ObjectDoesNotExist
from django.core.exceptions import PermissionDenied
from django.utils.html import escapejs

from wagtail.admin.modal_workflow import render_modal_workflow

from wagtail.snippets.permissions import user_can_edit_snippet_type
from wagtail.snippets.models import get_snippet_models

from wagtailembedder.format import embed_to_editor_html
from wagtailembedder.views.snippets import get_snippet_model_from_url_params


@permission_required('wagtailadmin.access_admin')
def index(request):
    """
    Fetches all human-readabe names of all snippet classes and presents them
    in a list.
    """
    snippet_types = [
        (
            content_type._meta.app_label,
            content_type._meta.model.__name__,
            content_type._meta.verbose_name,
            getattr(content_type._meta, 'description', ''),
        )
        for content_type in get_snippet_models()
        if user_can_edit_snippet_type(request.user, content_type)
    ]

    return render_modal_workflow(
        request,
        'wagtailembedder/snippets/types_list.html',
        template_vars={
            'snippet_types': snippet_types,
        },
        json_data={
            'step': 'types-list',
        }
    )


def index_objects(request, content_type_app_name, content_type_model_name):
    """
    Fetch objects of related model of the given ContentType and call the template
    to properly display them in a list.
    """

    model = get_snippet_model_from_url_params(content_type_app_name, content_type_model_name)
    items = model.objects.all()
    snippet_type_name = model._meta.verbose_name
    snippet_type_name_plural = model._meta.verbose_name_plural

    return render_modal_workflow(
        request,
        'wagtailembedder/snippets/type_index.html',
        template_vars={
            'content_type': {'app_label': content_type_app_name, 'model': content_type_model_name},
            'snippet_type_name': snippet_type_name,
            'snippet_type_name_plural': snippet_type_name_plural,
            'items': items,
        },
        json_data={
            'step': 'type-index',
        }
    )


def choose_snippet(request, id, content_type_app_name, content_type_model_name):
    """
    Choose snippet and display its representation in the Hallo.js richtext field.
    """

    model = get_snippet_model_from_url_params(content_type_app_name, content_type_model_name)
    if not user_can_edit_snippet_type(request.user, model):
        raise PermissionDenied
    try:
        model.objects.get(id=id)
    except ObjectDoesNotExist:
        return render_modal_workflow(
            request,
            None,
            template_vars={
                'error': 'Sorry, an error occurred. Contact support or try again later.'
            }
        )
    embed_html = embed_to_editor_html(id, content_type_app_name, content_type_model_name)

    return render_modal_workflow(
        request,
        None,
        json_data={
            'step': 'choose_snippet',
            'embed_html': embed_html,
        }
    )
