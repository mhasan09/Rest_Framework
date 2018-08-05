from rest_framework import serializers
from .models import inventory
class invertorySerializers(serializers.HyperlinkedModelSerializer):
    class Meta:
        model=inventory
        fields=('id','url','product_name','description')