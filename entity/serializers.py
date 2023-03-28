from rest_framework import serializers
from entity.models import Entity

class EntitySerializers(serializers.ModelSerializer):
    class Meta:
        model=Entity
        fields=('EntityID', 'EntityName', 'EntityAddress', 'EntityPasswd', 'EntityType', 'EntityCity', 'EntityState', 'EntityPincode', 'EntityContactNo')

