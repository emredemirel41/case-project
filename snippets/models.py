from django.db import models




class Device(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    mac = models.CharField(max_length=150,unique=True)
    owner = models.ForeignKey('auth.User', related_name='devices', on_delete=models.CASCADE)
    class Meta:
        ordering = ['created']

    def save(self, *args, **kwargs):
        super(Device, self).save(*args, **kwargs)
    def __str__(self):
        return self.mac

class DeviceLog(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    value = models.CharField(max_length=100)
    owner = models.ForeignKey(Device, related_name='devicelogs', on_delete=models.CASCADE)
    class Meta:
        ordering = ['created']

    def save(self, *args, **kwargs):
        super(DeviceLog, self).save(*args, **kwargs)
        
    def __str__(self):
        return self.value