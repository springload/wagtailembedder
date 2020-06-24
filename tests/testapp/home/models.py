from __future__ import absolute_import, unicode_literals

from django.db import models
from django.utils.encoding import python_2_unicode_compatible

try:
    from wagtail.admin.edit_handlers import FieldPanel
    from wagtail.core.models import Page
    from wagtail.core.fields import RichTextField
    from wagtail.snippets.models import register_snippet
except ImportError:
    from wagtail.admin.edit_handlers import FieldPanel
    from wagtail.core.models import Page
    from wagtail.core.fields import RichTextField
    from wagtail.snippets.models import register_snippet


@register_snippet
@python_2_unicode_compatible
class MySnippet(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class TestPage(Page):
    body = RichTextField(blank=True, features=['snippet'])

    content_panels = Page.content_panels + [
        FieldPanel('body'),
    ]
