from rest_framework import serializers
from .models import Cards, Firmware, Cars

class CardSerializer(serializers.ModelSerializer):
    id = serializers.CharField(required=False, write_only=True)
    class Meta:
        model = Cards
        fields = '__all__'

class FirmwareSerializer(serializers.ModelSerializer):
    class Meta:
        model = Firmware
        fields = '__all__'
    firmware_data = serializers.FileField()

class CarsSerializer(serializers.ModelSerializer):
    frimware_verison = FirmwareSerializer()
    class Meta:
        model = Cars
        fields = '__all__'
    
    def update(self, instance, validated_data):
        firmware_data = validated_data.pop('firmware_version', None)
        if firmware_data:
            firmware_instance, created = Firmware.objects.get_or_create(version=firmware_data['version'], defaults=firmware_data)
            instance.firmware_version = firmware_instance
        instance.license_plate_max = validated_data.get('license_plate_max', instance.license_plate_max)
        instance.mac_address = validated_data.get('mac_address', instance.mac_address)
        instance.rfids = validated_data.get('rfids', instance.rfids)
        instance.save()
        return instance
