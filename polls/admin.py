import json


from django.contrib import admin

# import django_admin_listfilter_dropdown.filters
from django.core.serializers.json import DjangoJSONEncoder
from django.db.models import Count, Sum, Min, Max
from django.db.models.functions import Trunc, TruncDay
from django.forms import DateTimeField, DateField
from django.http import JsonResponse
from django.urls import path

from .models import Question, Mieter, Mietobjekt, Nebenkosten, Nebenkosten_Typ, Kosten, \
    Mietzins, Year, Unterhalt, MietobjektSummary, MietzinseingaengeSummary, Mietzinseingaenge

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


@admin.register(Unterhalt)
class UnterhaltAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Unterhalt._meta.fields]


# admin.site.register(Nebenkosten_Typ)
admin.site.register(Kosten)
# admin.site.register(Month)

# ---- Table Mietzinseingaenge
@admin.register(Mietzinseingaenge)
class MietzinseingaengeAdmin(admin.ModelAdmin):
    list_display = ("mieter", "betrag", "datum", "month")

    #  list_filter  = ('mieter')

    def formfield_for_manytomany(self, db_field, request, **kwargs):
        if db_field.name == "nebenkosten":
            kwargs["queryset"] = Nebenkosten.objects.filter(aktiv=True).filter(mieter=7)
        return super(MietzinseingaengeAdmin, self).formfield_for_manytomany(db_field, request, **kwargs)

    def changelist_view(self, request, extra_context=None):
        # Aggregate new subscribers per day
        chart_data = (
            Mietzinseingaenge.objects.values("month")
                .annotate(y=Sum("betrag"))
                .order_by("-month")
        )
        print(chart_data)

        # Serialize and attach the chart data to the template context
        as_json = json.dumps(list(chart_data), cls=DjangoJSONEncoder)
        extra_context = extra_context or {"chart_data": as_json}

        # Call the superclass changelist_view to render the page
        return super().changelist_view(request, extra_context=extra_context)

    '''
    def changelist_view(self, request, extra_context=None):
        # Aggregate new subscribers per day
        chart_data = (
            Mietzinseingaenge.objects.annotate(date=TruncDay("year"))
                .values("betrag").
                annotate(y=Count("id"))
                .order_by("-mieter")
        )
        # datum , -date

        # Serialize and attach the chart data to the template context
        as_json = json.dumps(list(chart_data), cls=DjangoJSONEncoder)
        extra_context = extra_context or {"chart_data": as_json}

        # Call the superclass changelist_view to render the page
        return super().changelist_view(request, extra_context=extra_context)
          '''

    '''   
    def get_urls(self):
        urls = super().get_urls()
        extra_urls = [
            path("chart_data/", self.admin_site.admin_view(self.chart_data_endpoint))
        ]
        # NOTE! Our custom urls have to go before the default urls, because they
        # default ones match anything.
        return extra_urls + urls

    # JSON endpoint for generating chart data that is used for dynamic loading
    # via JS.
    def chart_data_endpoint(self, request):
        chart_data = self.chart_data()
        return JsonResponse(list(chart_data), safe=False)

    def chart_data(self):
        return (
            Mietzinseingaenge.objects.annotate(date=TruncDay("year"))
            .values("mieter")
            .annotate(y=Count("id"))
            .order_by("-date")
        )
'''

    # datum


#   list_filter = (("mieter", RelatedDropdownFilter),)
#   def get_form(self, request, obj=None, **kwargs):
#       if obj is not None and obj.type is not None:
#           kwargs['form'] = tagform_factory(obj.type)
#       return super(TagAdmin, self).get_form(request, obj, **kwargs)


@admin.register(MietzinseingaengeSummary)
class MietzinseingaengeSummaryAdmin(admin.ModelAdmin):
    change_list_template = 'admin/mietzinseingaenge_summary_change_list.html'
    date_hierarchy = 'datum'
    list_filter = ('mieter','year','month')

    def changelist_view(self, request, extra_context=None):
        response = super().changelist_view(request, extra_context=extra_context, )

        try:
            qs = response.context_data['cl'].queryset
        except (AttributeError, KeyError):
            return response

        metrics = {'total_month': Count('month'),
                   'total_betrag': Sum('betrag'), }
        # print('qs: '+str(qs))
        response.context_data['summary'] = list(qs.values('mieter__first_name')
                                                .annotate(**metrics)
                                                .order_by('-total_betrag'))

        # Total berechnen
        response.context_data['summary_total'] = dict(qs.aggregate(**metrics))

        # -----
        # annotate ist fuer many to many objekte
        # print(qs)
        #summary_over_time = qs.values('mieter__first_name').annotate(**metrics).order_by('-total_betrag')
        summary_over_time = qs.values('datum').annotate(**metrics).order_by('-total_betrag')


       # summary_over_time = qs.annotate(period=Trunc('datum','day',output_field=DateField(),),
       # ).values('period').annotate(total=Sum('price')).order_by('period')
        # summary_over_time = qs.annotate(period=Trunc('created','day',output_field=DateTimeField(),),
        # ).values('period').annotate(total=Sum('price')).order_by('period')

        print(summary_over_time)
        summary_range = summary_over_time.aggregate(low=Min('total_betrag'), high=Max('total_betrag'), )
        high = summary_range.get('high', 0)
        low = summary_range.get('low', 0)

        response.context_data['summary_over_time'] = [
            {'datum': x['datum'], 'monat': x['total_month'] or 0,
             'betrag': x['total_betrag'] ,
             } for x in summary_over_time]

        return response


@admin.register(MietobjektSummary)
class MietobjektSummaryAdmin(admin.ModelAdmin):
    change_list_template = 'admin/mietobjekt_summary_change_list.html'
    # date_hierarchy = 'building' # muss immer ein datum sein

    list_filter = ('name',)

    def changelist_view(self, request, extra_context=None):
        response = super().changelist_view(
            request,
            extra_context=extra_context,
        )

        try:
            qs = response.context_data['cl'].queryset
        except (AttributeError, KeyError):
            return response

        metrics = {
            'total_rent': Count('id'),
            'total_betrag': Sum('betrag'),  # von Tabelle Unterhalt
        }
        print('qs: ' + str(qs))
        response.context_data['summary'] = list(
            qs
                .values('name', 'betrag', 'datum')
                .annotate(**metrics)
                .order_by('-total_betrag')
        )
        return response
        # -----

    '''    summary_over_time = qs.annotate( period=Trunc('mieter','betrag',
                output_field=DateTimeField(),),
        ).values('period').annotate(total=Sum('price')).order_by('period')

        summary_range = summary_over_time.aggregate(low=Min('total'),high=Max('total'),)
        high = summary_range.get('high', 0)
        low = summary_range.get('low', 0)

        response.context_data['summary_over_time'] = [{
            'period': x['period'],
            'total': x['total'] or 0,
            'pct': ((x['total'] or 0) - low) / (high - low) * 100
               if high > low else 0,
        } for x in summary_over_time]
'''
