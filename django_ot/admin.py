from django.contrib import admin
from .models import OtAccount, OtConfig
from .forms import OtConfigAdminForm, OtConfigAdminFormset


class OtConfigInline(admin.TabularInline):

    model = OtConfig
    form = OtConfigAdminForm
    formset = OtConfigAdminFormset
    extra = 1


class OtAccountAdmin(admin.ModelAdmin):

    inlines = (OtConfigInline,)


admin.site.register(OtAccount, OtAccountAdmin)