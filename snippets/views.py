from django.shortcuts import render
from snippets.models import Device, DeviceLog
from snippets.serializers import DeviceSerializer, DeviceLogSerializer
from rest_framework import generics
from django.contrib.auth.models import User
from snippets.serializers import UserSerializer
from snippets.permissions import IsOwnerUser,IsOwnerDevice
from rest_framework.permissions import IsAuthenticated

class DeviceLogList(generics.ListCreateAPIView):

    def get_queryset(self):
        user = self.request.user
        user_ids = Device.objects.filter(owner=user)
        deviceslogs = DeviceLog.objects.filter(owner__in=user_ids)
        return deviceslogs
    queryset = get_queryset
    serializer_class = DeviceLogSerializer
    permission_classes = [IsAuthenticated ]
    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class DeviceLogDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = DeviceLog.objects.all()
    serializer_class = DeviceLogSerializer
    permission_classes = [IsAuthenticated & IsOwnerDevice]
    

    # http GET http://192.168.1.28:8000/devices/ 'Authorization: Token cedfddbbf59e019c07fe5c53e24073881f9234ae'
    # http GET http://192.168.1.28:8000/devicelogs/ 'Authorization: Token 852501d5336397bfe0be496236bd016b6f402436'

    # http --form POST http://192.168.1.28:8000/devices/ mac="emre.test.device3" 'Authorization: Token 852501d5336397bfe0be496236bd016b6f402436'
    # http --form POST http://192.168.1.28:8000/devicelogs/ value="11"  'Authorization: Token 852501d5336397bfe0be496236bd016b6f402436'

    """
        >>> qs = Device.objects.filter(owner="1").values_list()
        >>> print(qs.query)
    """

class DeviceList(generics.ListCreateAPIView):
    
    def get_queryset(self):
        user = self.request.user
        return Device.objects.filter(owner=user)
    queryset = get_queryset
    serializer_class = DeviceSerializer
    permission_classes = [IsAuthenticated & IsOwnerUser]
    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)
    

class DeviceDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Device.objects.all()
    serializer_class = DeviceSerializer
    permission_classes = [IsAuthenticated & IsOwnerUser]




class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer