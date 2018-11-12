from django.db import models

class Ludzie(models.Model):
    name = models.CharField(max_length=30)
