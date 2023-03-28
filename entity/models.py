from django.db import models
class Entity(models.Model):
    EntityTyp = (
        ('Col', 'College'),
        ('Com', 'Company')
    )
    EntityID = models.AutoField(primary_key=True)  # College Address or Company ID autoincrement with  primary key
    EntityName = models.CharField(max_length=500)  # College Address or Company Name
    EntityAddress = models.CharField(max_length=500)  # College Address or Company Address
    EntityPasswd = models.CharField(max_length=500)  # College Address or Company Password
    EntityType = models.CharField(max_length=500,choices=EntityTyp)  # College or Company
    EntityCity = models.CharField(max_length=500)  # College or Company City
    EntityState = models.CharField(max_length=500)  # College or Company State
    EntityPincode = models.IntegerField(max_length=10)  # College or Company Pincode
    EntityContactNo = models.CharField(max_length=500)  # College or Company Contact No
    EntityStatus = models.BooleanField(default=False) #is active or inactive
    EntityDate = models.DateTimeField(auto_now=True)
    EntityLogo = models.FileField(upload_to='entity_logo', blank=True)
