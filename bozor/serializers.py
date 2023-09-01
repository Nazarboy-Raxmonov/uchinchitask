from rest_framework import serializers
from .models import sotuvchi, mahsulot

class SellerSerializer(serializers.ModelSerializer):
    class Meta:
        model = sotuvchi
        fields = ('ism','familiya','tugilgan_sana')

class productSerializer(serializers.ModelSerializer):
    class Meta:
        model = mahsulot
        fields = ('nomi','ics','miqdori','owner')