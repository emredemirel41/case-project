from rest_framework import serializers
from snippets.models import Device, DeviceLog
from django.contrib.auth.models import User

class DeviceLogSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.mac')
    class Meta:
        model = DeviceLog
        fields = ['id', 'value', 'owner']


class DeviceSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    class Meta:
        model = Device
        fields = ['id', 'mac', 'owner']



class UserSerializer(serializers.ModelSerializer):
    
    devices = serializers.PrimaryKeyRelatedField(many=True, queryset=Device.objects.all())

    class Meta:
        model = User
        fields = ['id', 'username', 'devices']