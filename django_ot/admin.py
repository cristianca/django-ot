from django.contrib import admin
from .models import OtAccount, OtConfig, OtNews
from .forms import OtConfigAdminForm, OtConfigAdminFormset


class OtConfigInline(admin.TabularInline):

    model = OtConfig
    form = OtConfigAdminForm
    formset = OtConfigAdminFormset
    extra = 1


class OtAccountAdmin(admin.ModelAdmin):

    inlines = (OtConfigInline,)


class OtNewsAdmin(admin.ModelAdmin):

    list_display = ('hash', 'content_type', 'object_id', 'ot_config')
    list_filter = ('ot_config', 'content_type')


admin.site.register(OtAccount, OtAccountAdmin)