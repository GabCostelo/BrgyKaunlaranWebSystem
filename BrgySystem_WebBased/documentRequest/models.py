from django.db import models
from accounts.models import User
import datetime

# Create your models here.
class docType(models.Model):
    is_Pending = models.BooleanField(default=True)
    is_Done = models.BooleanField(default=False)

    class Meta:
        abstract = True

class BrgyIndigency(docType):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    middle_name = models.CharField(max_length=100)
    age = models.PositiveIntegerField()
    nationality = models.CharField(max_length=100)
    purpose = models.CharField(max_length=100)
    Address = models.CharField(max_length=255)
    email =  models.CharField(max_length=255)
    cedula = models.ImageField(null=True, blank=True, default = '#' ,upload_to="BrgyIndigencyCedula/")
    validId = models.ImageField(null=True, blank=True, default = '#' ,upload_to="BrgyIndigencyID/")
    otherDocument = models.ImageField(null=True, blank=True, default = '#' ,upload_to="BrgyIndigencyOtherDocs/")
    requested_by = models.ForeignKey(User,on_delete=models.CASCADE)
    requested_at = models.DateField(default=datetime.date.today)

    def __str__(self):
        return str(self.requested_by)

class BrgyClearance(docType):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    middle_name = models.CharField(max_length=100)
    age = models.PositiveIntegerField()
    nationality = models.CharField(max_length=100)
    purpose = models.CharField(max_length=100)
    Address = models.CharField(max_length=255)
    email =  models.CharField(max_length=255)
    cedula = models.ImageField(null=True, blank=True, default = '#' ,upload_to="BrgyClearanceCedula/")
    requested_by = models.ForeignKey(User,on_delete=models.CASCADE)
    requested_at = models.DateField(default=datetime.date.today)

    def __str__(self):
        return str(self.requested_by)


class BrgyResidency(docType):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    middle_name = models.CharField(max_length=100)
    age = models.PositiveIntegerField()
    nationality = models.CharField(max_length=100)
    purpose = models.CharField(max_length=100)
    Address = models.CharField(max_length=255)
    email =  models.CharField(max_length=255)
    requested_by = models.ForeignKey(User,on_delete=models.CASCADE)
    requested_at = models.DateField(default=datetime.date.today)
    cedula = models.ImageField(null=True, blank=True, default = '#' ,upload_to="BrgyIndigencyCedula/")
    validId = models.ImageField(null=True, blank=True, default = '#' ,upload_to="BrgyIndigencyID/")

    def __str__(self):
        return str(self.requested_by)
