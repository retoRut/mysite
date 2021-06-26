from django.contrib import admin


from .models import Question, Mieter, Mietobjekt, Nebenkosten, Nebenkosten_Typ, Kosten, Month, Year, Mietzinseingaenge, \
    ZahlungsTyp, Mietzinse

admin.site.register(Question)

# ---- Table Nebenkosten Typ
@admin.register(Nebenkosten_Typ)
class Nebenkosten_TypAdmin(admin.ModelAdmin):
    list_display = ("typ", "a_conto")

# Register your models here.
@admin.register(Mieter)
class MieterAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Mieter._meta.fields]

#admin.site.register(Mieter)
admin.site.register(Mietobjekt)
admin.site.register(Nebenkosten)
admin.site.register(Mietzinse)
# admin.site.register(Nebenkosten_Typ)
admin.site.register(Kosten)
admin.site.register(Month)
admin.site.register(Year)
admin.site.register(ZahlungsTyp)

# ---- Table Mietzinseingaenge
@admin.register(Mietzinseingaenge)
class MietzinseingaengeAdmin(admin.ModelAdmin):
    list_display = ("mieter", "betrag","datum","month","year" )





