from django.contrib import admin

# import django_admin_listfilter_dropdown.filters

from .models import Question, Mieter, Mietobjekt, Nebenkosten, Nebenkosten_Typ, Kosten, Mietzinseingaenge, \
 Mietzins, Year

admin.site.register(Question)

# ---- Table Nebenkosten Typ
@admin.register(Nebenkosten_Typ)
class Nebenkosten_TypAdmin(admin.ModelAdmin):
    list_display = ("typ", "a_conto")

# Register your models here.
@admin.register(Mieter)
class MieterAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Mieter._meta.fields]

admin.site.register(Year)


@admin.register(Mietobjekt)
class MietobjektAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Mietobjekt._meta.fields]
# admin.site.register(Nebenkosten)
# ---- Table Mietzinseingaenge
@admin.register(Nebenkosten)
class NebenkostenAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Nebenkosten._meta.fields]

@admin.register(Mietzins)
class MietzinsAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Mietzins._meta.fields]

# admin.site.register(Nebenkosten_Typ)
admin.site.register(Kosten)
# admin.site.register(Month)

# ---- Table Mietzinseingaenge
@admin.register(Mietzinseingaenge)
class MietzinseingaengeAdmin(admin.ModelAdmin):
    list_display = ("mieter", "betrag","datum","month")

    def formfield_for_manytomany(self, db_field, request, **kwargs):
        print(str(db_field))
        if db_field.name == "nebenkosten":
            kwargs["queryset"] = Nebenkosten.objects.filter(aktiv=True).filter(mieter=7)
        return super(MietzinseingaengeAdmin, self).formfield_for_manytomany(db_field, request, **kwargs)

 #   list_filter = (("mieter", RelatedDropdownFilter),)
 #   def get_form(self, request, obj=None, **kwargs):
 #       if obj is not None and obj.type is not None:
 #           kwargs['form'] = tagform_factory(obj.type)
 #       return super(TagAdmin, self).get_form(request, obj, **kwargs)


