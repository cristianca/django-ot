from requests.exceptions import ConnectionError
from django import forms
from django.forms.models import BaseInlineFormSet
from .models import OtConfig
from .consts import CONNECTION_ERROR


class OtConfigAdminFormset(BaseInlineFormSet):

    def _construct_form(self, i, **kwargs):
        form = super(OtConfigAdminFormset, self)._construct_form(i, **kwargs)
        if self.instance and self.instance.pk:
            form.account = self.instance
        return form


class OtConfigAdminForm(forms.ModelForm):

    class Meta:
        model = OtConfig

    def set_account(self, account):
        self._account = account
        try:
            channels = account.api.get_channel_list()
        except ConnectionError:
            self.fields['channel'].help_text = CONNECTION_ERROR
        else:
            channel_choices = [
                (channel.id, u'%s: %s' % (channel.channel_type, channel.name))
                for channel in channels]
            channel_choices.insert(0, ('', '------'))
            self.fields['channel'] = forms.ChoiceField(choices=channel_choices,
                required=False)

    def get_account(self, account):
        return getattr(self, '_account', None)

    account = property(get_account, set_account)