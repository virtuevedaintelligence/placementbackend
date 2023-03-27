from django.db import models
class Entity(models.Model):
    EntityID = models.AutoField(primary_key=True)  # College Address or Company ID
    EntityName = models.CharField(max_length=500)  # College Address or Company Name
    EntityAddress = models.CharField(max_length=500)  # College Address or Company Address
    EntityPasswd = models.CharField(max_length=500)  # College Address or Company Password
    EntityType = models.CharField(max_length=500)  # College or Company
    EntityCity = models.CharField(max_length=500)  # College or Company City
    EntityState = models.CharField(max_length=500)  # College or Company State
    EntityPincode = models.CharField(max_length=500)  # College or Company Pincode
    EntityContactNo = models.CharField(max_length=500)  # College or Company Contact No