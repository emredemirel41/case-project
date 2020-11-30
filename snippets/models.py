from django.db import models


class Snippet(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=100, blank=True, default='')
    value = models.CharField(max_length=100)
    owner = models.ForeignKey('auth.User', related_name='snippets', on_delete=models.CASCADE)
    class Meta:
        ordering = ['created']

    def save(self, *args, **kwargs):
        super(Snippet, self).save(*args, **kwargs)
