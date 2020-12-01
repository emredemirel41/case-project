
from django.test import TestCase
from snippets.models import Device, DeviceLog
from django.contrib.auth.models import User
from snippets.serializers import DeviceSerializer, DeviceLogSerializer
from http import HTTPStatus
from rest_framework.authtoken.models import Token
from rest_framework.test import APIClient
from snippets.permissions import IsOwnerUser,IsOwnerDevice
from rest_framework.permissions import IsAuthenticated
from rest_framework import status

class API_GET_REQUEST_TestCase(TestCase):
    def setUp(self):
        print("setUpTestData: Data Set-Up for API - GET REQUEST")
        # User 1
        cur_user1 = User.objects.create_user(username='testuser1', password='12345')
        Token.objects.create(user=cur_user1)

        # Device 1 - User 1
        cur_device1 = Device.objects.create(mac='100.456.475.1', owner=cur_user1)

        # Value 1 - Device 1 - User 1
        DeviceLog.objects.create(value='111', owner=cur_device1)
        # Value 2 - Device 1 - User 1
        DeviceLog.objects.create(value='211', owner=cur_device1)

        # Device 2 - User 1
        cur_device2 = Device.objects.create(mac='200.456.475.1', owner=cur_user1)

        # Value 1 - Device 2 - User 1
        DeviceLog.objects.create(value='121', owner=cur_device2)
        # Value 2 - Device 2 - User 1
        DeviceLog.objects.create(value='221', owner=cur_device2)


        # User 2
        cur_user2 = User.objects.create_user(username='testuser2', password='12345')
        Token.objects.create(user=cur_user2)

        # Device 3 - User 2
        cur_device3 = Device.objects.create(mac='300.456.475.2', owner=cur_user2)

        # Value 1 - Device 3 - User 2
        DeviceLog.objects.create(value='132', owner=cur_device3)
        # Value 2 - Device 3 - User 2
        DeviceLog.objects.create(value='232', owner=cur_device3)

        # Device 4 - User 2
        cur_device4 = Device.objects.create(mac='400.456.475.2', owner=cur_user2)

        # Value 1 - Device 4 - User 2
        DeviceLog.objects.create(value='142', owner=cur_device4)
        # Value 2 - Device 4 - User 2
        DeviceLog.objects.create(value='242', owner=cur_device4)

    # Devices List Testing
    def test_get_all_devices(self):
        print("devices/ - List Devices - GET REQUEST TESTING...")
        # get API response
        token = Token.objects.get(user__username='testuser1')
        client = APIClient()
        client.credentials(HTTP_AUTHORIZATION='Token ' + token.key)
        response = client.get('/devices/', format='json')

        # check status
        print(response.status_code)
        print(response.data)
        self.assertEqual(response.status_code, HTTPStatus.OK)


    # Devices Detail Testing
    def test_get_one_devices_detail(self):
        print("devices/int:pk/ - Detail Devices - GET REQUEST TESTING...")
        # get API response
        token = Token.objects.get(user__username='testuser1')
        client = APIClient()
        client.credentials(HTTP_AUTHORIZATION='Token ' + token.key)
        response = client.get('/devices/1/', format='json')
        #If you change device number and username for different results...
        #403 = User try to get data he don't have own

        # check status
        print(response.status_code)
        print(response.data)
        self.assertEqual(response.status_code, HTTPStatus.OK )





        # DeviceLogs List Testing
    def test_get_all_devicelogs(self):
        print("devices/ - List DeviceLogs - GET REQUEST TESTING...")
        # get API response
        token = Token.objects.get(user__username='testuser1')
        client = APIClient()
        client.credentials(HTTP_AUTHORIZATION='Token ' + token.key)
        response = client.get('/devicelogs/', format='json')

        # check status
        print(response.status_code)
        print(response.data)
        self.assertEqual(response.status_code, HTTPStatus.OK)


    # DeviceLogs Detail Testing
    def test_get_one_devicelogs_detail(self):
        print("devices/int:pk/ - Detail DeviceLogs - GET REQUEST TESTING...")
        # get API response
        token = Token.objects.get(user__username='testuser1')
        client = APIClient()
        client.credentials(HTTP_AUTHORIZATION='Token ' + token.key)
        response = client.get('/devicelogs/1/', format='json')
        #If you change devicelog number and username for different results...
        #403 = Forbidden

        # check status
        print(response.status_code)
        print(response.data)
        self.assertEqual(response.status_code, HTTPStatus.OK)




     # DeviceLogs List Testing based on Macaddress
    def test_get_based_macaddress_devicelogs(self):
        print("device/macaddress - List DeviceLogs Based on Mac Address- GET REQUEST TESTING...")
        # get API response
        token = Token.objects.get(user__username='testuser1')
        client = APIClient()
        client.credentials(HTTP_AUTHORIZATION='Token ' + token.key)
        response = client.get('/device/100.456.475.1', format='json')

        # check status
        print(response.status_code)
        print(response.data)
        self.assertEqual(response.status_code, HTTPStatus.OK)




class API_POST_REQUEST_TestCase(TestCase):
    def setUp(self):
        print("setUpTestData: Data Set-Up for API - POST REQUEST")
        # User 1
        cur_user1 = User.objects.create_user(username='testuser1', password='12345')
        Token.objects.create(user=cur_user1)
        # Device 1 - User 1
        cur_device1 = Device.objects.create(mac='100.456.475.1', owner=cur_user1)

        # Device 2 - User 1
        cur_device2 = Device.objects.create(mac='200.456.475.1', owner=cur_user1)


        # User 2
        cur_user2 = User.objects.create_user(username='testuser2', password='12345')
        Token.objects.create(user=cur_user2)
        # Device 3 - User 2
        cur_device3 = Device.objects.create(mac='300.456.475.2', owner=cur_user2)


    # Device POST Testing 
    def test_post_device_devicelogs(self):
        print("devices/ - Add Device - POST REQUEST TESTING...")
        # get API response

        token = Token.objects.get(user__username='testuser1')
        client = APIClient()
        client.credentials(HTTP_AUTHORIZATION='Token ' + token.key)
        response = client.post('/devices/', {'mac': '909.909.909.1'}, format='json')

        # check status
        print(response.status_code)
        print(response.data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)


    # DeviceLog POST Testing 
    def test_post_device_devicelogs(self):
        print("devicelogs/ - Add DeviceLogs - POST REQUEST TESTING...")
        # get API response

        token = Token.objects.get(user__username='testuser1')
        client = APIClient()
        client.credentials(HTTP_AUTHORIZATION='Token ' + token.key)
        response = client.post('/devicelogs/', {'mac': '100.456.475.1', 'value': '191'}, format='json')

        # check status
        print(response.status_code)
        print(response.data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)