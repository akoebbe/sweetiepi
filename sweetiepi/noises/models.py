from django.db import models


class NoiseFile(models.Model):
    name = models.CharField(max_length=255)
    file = models.FileField(upload_to='noises')

    def __unicode__(self):
        return self.name
