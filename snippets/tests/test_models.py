from django.test import TestCase
from snippets.models import Device, DeviceLog
from django.contrib.auth.models import User

class DeviceModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        print("setUpTestData: Data Set-Up for Device Model")
        cur_user = User.objects.create_user(username='testuser', password='12345')
        Device.objects.create(mac='255.456.475.1', owner=cur_user)

    def test_mac_label(self):
        print("Test test-mac_label: Data Set-Up for Device Model - Check Label Name - mac")
        device = Device.objects.get(id=1)
        field_label = device._meta.get_field('mac').verbose_name
        self.assertEqual(field_label, 'mac')

    def test_mac_max_length(self):
        print("Test test-mac_max_length: Data Set-Up for Device Model - Check Max Length - mac")
        device = Device.objects.get(id=1)
        max_length = device._meta.get_field('mac').max_length
        self.assertEqual(max_length, 150)

    def test_object_name(self):
        print("Test test-object_name: Data Set-Up for Device Model - __str__ function to get mac")
        device = Device.objects.get(id=1)
        expected_object_name = device.mac
        self.assertEqual(expected_object_name, str(device))

class DeviceLogModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        print("setUpTestData: Data Set-Up for DeviceLog Model")
        cur_user = User.objects.create_user(username='testuser', password='12345')
        cur_device = Device.objects.create(mac='255.456.475.1', owner=cur_user)
        DeviceLog.objects.create(value='7', owner=cur_device)

    def test_value_label(self):
        print("Test value_label: Data Set-Up for Device Model - Check Label Name - value")
        device_val = DeviceLog.objects.get(id=1)
        field_label = device_val._meta.get_field('value').verbose_name
        self.assertEqual(field_label, 'value')

    def test_object_val(self):
        print("Test test-object_value: Data Set-Up for Device Model - __str__ function to get value")
        device_val = DeviceLog.objects.get(id=1)
        expected_object_name = str(device_val.value)
        self.assertEqual(expected_object_name, str(device_val))