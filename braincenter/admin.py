from django.contrib import admin
from .models import Series, SeriesType, SeriesSet
# Register your models here.

admin.site.register(Series)

admin.site.register(SeriesSet)

admin.site.register(SeriesType)



