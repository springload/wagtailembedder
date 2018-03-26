try:
    from wagtail.snippets.views.snippets import get_snippet_model_from_url_params
except ImportError:  # Wagtail < 2.0
    try:
        from wagtail.wagtailsnippets.views.snippets import get_snippet_model_from_url_params

    except ImportError:  # Wagtail < 1.4
        from wagtail.wagtailsnippets.views.snippets import get_content_type_from_url_params

        def get_snippet_model_from_url_params(app_name, model_name):
            content_type = get_content_type_from_url_params(app_name, model_name.lower())
            model = content_type.model_class()

            return model
