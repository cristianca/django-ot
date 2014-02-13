import importlib

from django.db import models
from django.utils.translation import ugettext_lazy as _

from pyot import Api

from .consts import OT_ACTION_CHOICES
from .managers import OtConfigManager


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
            self._api = Api(self.slug, self.user, self.api_key)
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
        action_func(news)

    def get_channel_display(self):
        return u''


