from django.contrib import admin

# Register your models here.

from p1.models import Calles, Semaforos, Manzanas

admin.site.register(Calles)
admin.site.register(Semaforos)
admin.site.register(Manzanas)