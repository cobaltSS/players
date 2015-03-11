from django.db import models

class Players(models.Model):
    name = models.CharField(max_length=255)
    wins = models.IntegerField(default=0)
    lesions = models.IntegerField(default=0)

    class Meta:
        verbose_name_plural = 'players'

    def __unicode__(self):
        return '%s' % self.name

