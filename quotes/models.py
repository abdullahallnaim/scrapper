from django.db import models

# Create your models here.
from django.db import models

class Quote(models.Model):
    text = models.TextField()
    author = models.CharField(max_length=255)
    source = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return f'"{self.text}" - {self.author}'
