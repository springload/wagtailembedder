
from django.contrib.auth.decorators import permission_required
from django.core.exceptions import ObjectDoesNotExist
from django.core.exceptions import PermissionDenied

from wagtail.wagtailadmin.modal_workflow import render_modal_workflow

from wagtail.wagtailsnippets.models import get_snippet_content_types
from wagtail.wagtailsnippets.permissions import user_can_edit_snippet_type
from wagtail.wagtailsnippets.views.snippets import get_content_type_from_url_params
from wagtail.wagtailsnippets.models import get_snippet_models

from wagtailembedder.format import embed_to_editor_html


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
            content_type._meta.description,
        )
        for content_type in get_snippet_models()
        if user_can_edit_snippet_type(request.user, content_type)
    ]
    return render_modal_workflow(
        request,
        'wagtailembedder/snippets/types_list.html',
        'wagtailembedder/snippets/types_list.js',
        {
            'snippet_types': snippet_types,
        }
    )


def index_objects(request, content_type_app_name, content_type_model_name):
    """
    Fetch objects of related model of the given ContentType and call the template
    to properly display them in a list.
    """
    snippet_types = get_snippet_content_types()
    for content_type in snippet_types:
        if content_type.model == content_type_model_name.lower():
            items = content_type.model_class().objects.all()
            snippet_type_name = content_type.model_class()._meta.verbose_name
            snippet_type_name_plural = content_type.model_class()._meta.verbose_name_plural

            return render_modal_workflow(
                request,
                'wagtailembedder/snippets/type_index.html',
                'wagtailembedder/snippets/type_index.js',
                {
                    'content_type': content_type,
                    'snippet_type_name': snippet_type_name,
                    'snippet_type_name_plural': snippet_type_name_plural,
                    'items': items,
                }
            )

    raise ObjectDoesNotExist


def choose_snippet(request, id, content_type_app_name, content_type_model_name):
    """
    Choose snippet and display its representation in the Hallo.js richtext field.
    """
    content_type = get_content_type_from_url_params(content_type_app_name, content_type_model_name)
    if not user_can_edit_snippet_type(request.user, content_type):
        raise PermissionDenied
    model = content_type.model_class()
    try:
        model.objects.get(id=id)
    except ObjectDoesNotExist:
        return render_modal_workflow(
            request,
            None,
            None,
            {'error': 'Sorry, an error occurred. Contact support or try again later.'}
        )
    embed_html = embed_to_editor_html(id, content_type_app_name, content_type_model_name)

    return render_modal_workflow(
        request,
        None,
        'wagtailembedder/editor/snippet_chosen.js',
        {'embed_html': embed_html}
    )
