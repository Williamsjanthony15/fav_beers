from django.db import models
from django.contrib.auth import get_user_model
from django.urls import reverse
# Create your models here.

class Beer(models.Model):
    title = models.CharField(max_length=64)
    description = models.TextField(default='')
    userName = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.name

    def get_absolute_url(self):
        return reverse('beerDelete', args=[str(self.id)])