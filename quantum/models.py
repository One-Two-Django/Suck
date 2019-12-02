from django.db import models
from django.utils import timezone
from django.conf import settings
# Create your models here.

class Screen(models.Model):
    title = models.CharField(max_length=1000000000000)
    subtext = models.CharField(max_length=1000000000000)
    created_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title
class Pic(models.Model):
    screen = models.ForeignKey('Screen', on_delete=models.CASCADE)
    picture = models.ImageField()
    text = models.CharField(max_length=1000000000000)
    def __str__(self):
        return self.text

    def this_pic(self):
        return self.picture


