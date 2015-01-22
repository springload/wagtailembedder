wagtailembedder
==================

Snippets embedder for Wagtail richtext fields.

# Quickstart

``` $ pip install wagtailembedder [GITHUB SSH URI]```

add wagtailembedder to your settings.py in the INSTALLED_APPS section:

```
...
    'modelcluster',
    'wagtailembedder',
    'core',
...
```

For each of your models registered as a wagtail.wagtailsnippets create an html file to render the template inside a RichText field.
Example: if we have a ```SocialMediaLink``` snippet in our ```core``` app we need to create a template in ```core/templates/snippets/social_media_link.html```

If no template is defined then nothing will be outputted in the frontend when rendering a RichText field, don't be a dick and write some nice templates.

Templates names will match snippets models names replacing capital letters with underscores, Wagtail style.

