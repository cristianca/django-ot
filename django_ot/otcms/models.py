from django.conf import settings
from django.db import models
from django.utils.translation import ugettext_lazy as _

from cms.models.pagemodel import Page
from django_ot.models import OtConfig


class CmsOtConfig(OtConfig):

    template = models.CharField(_("template"), max_length=100,
        choices=Page.template_choices,
        help_text=_('The template used to render the content.'))
    language = models.CharField(_('language'), choices=settings.LANGUAGES,
        max_length=15)
    placeholder = models.CharField(_('placeholder'), max_length=255)
    parent_page = models.ForeignKey('cms.Page', null=True, blank=True)

