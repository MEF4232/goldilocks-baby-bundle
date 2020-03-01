from django.db import models

class Practice(models.Model):
    name = models.CharField(max_length=200)