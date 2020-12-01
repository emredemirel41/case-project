from django.shortcuts import render
from snippets.models import Device, DeviceLog
from snippets.serializers import DeviceSerializer, DeviceLogSerializer
from rest_framework import generics
from django.contrib.auth.models import User
from snippets.serializers import UserSerializer
from snippets.permissions import IsOwnerUser,IsOwnerDevice
from rest_framework.permissions import IsAuthenticated
from django.http import Http404


class DeviceMacList(generics.ListCreateAPIView):
    def get_queryset(self):
        try:
            owner_id = Device.objects.get(mac=self.kwargs['mac'] , owner=self.request.user)
            return  DeviceLog.objects.filter(owner=owner_id)
        except Device.DoesNotExist:
            raise Http404
        
    queryset = get_queryset
    serializer_class = DeviceLogSerializer
    permission_classes = [IsAuthenticated ]





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
        try:
            device_id = Device.objects.get(mac=self.request.data["mac"] , owner=self.request.user)
            serializer.save(owner=device_id)
        except Device.DoesNotExist:
            raise Http404

class DeviceLogDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = DeviceLog.objects.all()
    serializer_class = DeviceLogSerializer
    permission_classes = [IsAuthenticated & IsOwnerDevice]
    

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