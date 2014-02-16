from django.contrib import admin

from django_ot.admin import OtAccountAdmin as BaseOtAccountAdmin
from django_ot.admin import OtConfigInline
from django_ot.models import OtAccount

from .models import CmsOtConfig


class CmsOtConfigAdmin(OtConfigInline):
    model = CmsOtConfig
    raw_id_fields = ('parent_page',)


class OtAccountAdmin(BaseOtAccountAdmin):
    inlines = (CmsOtConfigAdmin,)


admin.site.unregister(OtAccount)
admin.site.register(OtAccount, OtAccountAdmin)
