import importlib
import hashlib

from django.contrib.contenttypes.generic import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.db import models
from django.utils.translation import ugettext_lazy as _

from pyot import Api

from .consts import OT_ACTION_CHOICES
from .managers import OtConfigManager


class HttpApi(Api):
    """Temporary http class as https is not working properlly"""
    API_URL = u'http://app.opentopic.com/%(site_slug)s/api/%(api_version)s/'


class OtAccount(models.Model):

    slug = models.SlugField(_('Account Slug'), max_length=255)
    user = models.CharField(_('User'), max_length=255)
    api_key = models.CharField(_('Api Key'), max_length=500)

    class Meta:
        verbose_name = _('Opentopic Account')
        verbose_name_plural = _('Opentopic Accounts')

    def __unicode__(self):
        return self.slug

    @property
    def api(self):
        if not hasattr(self, '_api'):
            self._api = HttpApi(self.slug, self.user, self.api_key)
        return self._api


class OtConfig(models.Model):

    account = models.ForeignKey(OtAccount)
    channel = models.IntegerField(_('Channel'), null=True, blank=True)
    action = models.CharField(_('Action'), null=True, blank=True,
        choices=OT_ACTION_CHOICES, max_length=500)
    is_active = models.BooleanField(_('Is Active'), default=False)

    objects = OtConfigManager()

    class Meta:
        verbose_name = _('Opentopic Config')
        verbose_name_plural = _('Opentopic Configs')

    def __unicode__(self):
        return u'%s %s' % (unicode(self.account), self.get_channel_display())

    def import_news(self):
        api = self.account.api
        channel = api.get_channel_detail(self.channel)
        news = channel.get_news()
        m, f = self.action.rsplit('.', 1)
        action_func = getattr(importlib.import_module(m), f)
        for n in news:
            hash = unicode(hashlib.md5(unicode(n._json)).hexdigest())[:250]
            try:
                ot_news = OtNews.objects.get(ot_news_pk=n.id, ot_config=self)
            except OtNews.DoesNotExist:
                is_updated = True
                ot_news = OtNews.objects.create(
                    ot_config=self,
                    ot_news_pk=n.id,
                    hash=hash)
                content_object = None
            else:
                if ot_news.hash == hash:
                    is_updated = False
                else:
                    is_updated = True
                    ot_news.hash = hash
                    ot_news.save()
                    content_object = ot_news.content_object

            if is_updated:
                content_object = action_func(ot_config=self, news=n,
                    content_object=content_object)
                ot_news.content_object = content_object
                ot_news.save()

    def get_channel_display(self):
        return u''


class OtNews(models.Model):
    ot_config = models.ForeignKey(OtConfig)
    ot_news_pk = models.PositiveIntegerField(_('News Id in Opentopic'))
    hash = models.CharField(_('Update Hash'), max_length=255)

    content_type = models.ForeignKey(ContentType, null=True, blank=True)
    object_id = models.PositiveIntegerField(_('Object id'), null=True,
        blank=True)
    content_object = GenericForeignKey('content_type', 'object_id')

    class Meta:
        verbose_name = _('Opentopic News')
        verbose_name_plural = _('Opentopic News')

    def __unicode__(self):
        return self.hash