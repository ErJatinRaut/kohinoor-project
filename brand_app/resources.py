from import_export import resources
from .models import brands

class PersonResource(resources.ModelResource):
    class Meta:
        model = brands