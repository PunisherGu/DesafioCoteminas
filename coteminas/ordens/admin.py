from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from .models import Person


from .models import ordem
admin.site.register(ordem)

@admin.register(Person)
class PersonAdmin(ImportExportModelAdmin):
    pass