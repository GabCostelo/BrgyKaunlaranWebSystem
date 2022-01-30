from django.contrib import admin
from documentRequest.models import docType,BrgyIndigency,BrgyClearance,BrgyResidency
# Register your models here.

admin.site.register(BrgyIndigency)
admin.site.register(BrgyClearance)
admin.site.register(BrgyResidency)
