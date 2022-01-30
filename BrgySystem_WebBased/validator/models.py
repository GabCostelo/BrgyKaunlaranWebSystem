from django.db import models

# Create your models here.
class SaintJohnStreet(models.Model):
    middle_name = models.CharField(max_length=255,blank=True)
    last_name = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    def __str__(self):
        return self.last_name

class SaintPeterStreet(models.Model):
    middle_name = models.CharField(max_length=255,blank=True)
    last_name = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    def __str__(self):
        return self.last_name

class NDomingoStreet(models.Model):
    middle_name = models.CharField(max_length=255,blank=True)
    last_name = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    def __str__(self):
        return self.last_name

class NatibStreet(models.Model):
    middle_name = models.CharField(max_length=255,blank=True)
    last_name = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    def __str__(self):
        return self.last_name

class DriodStreet(models.Model):
    middle_name = models.CharField(max_length=255,blank=True)
    last_name = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    def __str__(self):
        return self.last_name

class CristobalStreet(models.Model):
    middle_name = models.CharField(max_length=255,blank=True)
    last_name = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    def __str__(self):
        return self.last_name

class BatayStreet(models.Model):
    middle_name = models.CharField(max_length=255,blank=True)
    last_name = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    def __str__(self):
        return self.last_name

class BaleteStreet(models.Model):
    middle_name = models.CharField(max_length=255,blank=True)
    last_name = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    def __str__(self):
        return self.last_name

class HemadyStreet(models.Model):
    middle_name = models.CharField(max_length=255,blank=True)
    last_name = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    def __str__(self):
        return self.last_name

class PTuazonStreet(models.Model):
    middle_name = models.CharField(max_length=255,blank=True)
    last_name = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    def __str__(self):
        return self.last_name

class PlanasSiteIStreet(models.Model):
    middle_name = models.CharField(max_length=255,blank=True)
    last_name = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    def __str__(self):
        return self.last_name

class PlanasSiteIIStreet(models.Model):
    middle_name = models.CharField(max_length=255,blank=True)
    last_name = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    def __str__(self):
        return self.last_name

class PlanasSiteIIIStreet(models.Model):
    middle_name = models.CharField(max_length=255,blank=True)
    last_name = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    def __str__(self):
        return self.last_name

class BarioPanopioStreet(models.Model):
    middle_name = models.CharField(max_length=255,blank=True)
    last_name = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    def __str__(self):
        return self.last_name

class AuroraBlvdStreet(models.Model):
    middle_name = models.CharField(max_length=255,blank=True)
    last_name = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    def __str__(self):
        return self.last_name

class BanahawStreet(models.Model):
    middle_name = models.CharField(max_length=255,blank=True)
    last_name = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    def __str__(self):
        return self.last_name

class CBenitezStreet(models.Model):
    middle_name = models.CharField(max_length=255,blank=True)
    last_name = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    def __str__(self):
        return self.last_name

class SanGabrielStreet(models.Model):
    middle_name = models.CharField(max_length=255,blank=True)
    last_name = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    def __str__(self):
        return self.last_name

class AdaStreet(models.Model):
    middle_name = models.CharField(max_length=255,blank=True)
    last_name = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    def __str__(self):
        return self.last_name

class PBernardoStreet(models.Model):
    middle_name = models.CharField(max_length=255,blank=True)
    last_name = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    def __str__(self):
        return self.last_name

class BostonStreet(models.Model):
    middle_name = models.CharField(max_length=255,blank=True)
    last_name = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    def __str__(self):
        return self.last_name

class SeattleStreet(models.Model):
    middle_name = models.CharField(max_length=255,blank=True)
    last_name = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    def __str__(self):
        return self.last_name

class ArayatStreet(models.Model):
    middle_name = models.CharField(max_length=255,blank=True)
    last_name = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    def __str__(self):
        return self.last_name
