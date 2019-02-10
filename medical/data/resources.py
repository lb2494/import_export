from import_export import resources
from .models import Patient

class PatientResources(resources.ModelResource):
    class Meta:
        model = Patient