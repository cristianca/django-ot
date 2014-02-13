from django import forms
from django.forms.models import BaseInlineFormSet
from .models import OtConfig


class OtConfigAdminFormset(BaseInlineFormSet):

    def _construct_form(self, i, **kwargs):
        form = super(OtConfigAdminFormset, self)._construct_form(i, **kwargs)
        form.account = self.instance
        return form


class OtConfigAdminForm(forms.ModelForm):

    class Meta:
        model = OtConfig

    def set_account(self, account):
        self._account = account
        channels = account.api.get_channel_list()
        channel_choices = [
            (channel.id, u'%s: %s' % (channel.channel_type, channel.name))
            for channel in channels]
        channel_choices.insert(0, ('', '------'))
        self.fields['channel'] = forms.ChoiceField(choices=channel_choices,
            required=False)

    def get_account(self, account):
        return getattr(self, '_account', None)

    account = property(get_account, set_account)