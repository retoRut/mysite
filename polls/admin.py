from django.contrib import admin


from .models import Question, Mieter

admin.site.register(Question)
# Register your models here.

admin.site.register(Mieter)