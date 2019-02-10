from import_export.admin import ImportExportModelAdmin
from django.contrib import admin
from .models import Patient

@admin.register(Patient)
class PatientAdmin(ImportExportModelAdmin):
    pass