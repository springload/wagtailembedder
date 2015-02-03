wagtailembedder
==================

Format: ![Wagtailembedder scnreenshot](http://i.imgur.com/qDPKz7r.png)

Snippets embedder for Wagtail RichTextField.

# Quickstart

``` $ pip install -e git+git@github.com:springload/wagtailembedder#egg=wagtailembedder```

add wagtailembedder to your settings.py in the INSTALLED_APPS section:

```
...
    'modelcluster',
    'wagtailembedder',
    'core',
...
```

For each of your models registered as a wagtail.wagtailsnippets create an html file to render the template inside a RichText field.
Example: if we have a ```SocialMediaLink``` snippet in our ```core``` app we need to create a template in ```core/templates/snippets/social_media_link.html```. The variable containing the snippet instance in the template is ```snippet```.

If no template is defined then an exception will be raised in the frontend when rendering a RichTextField with the embedded snippet in it. Make sure you write some templates for your snippets before start to embedding them.

Templates names will match snippets models names replacing capital letters with underscores, Wagtail style.

