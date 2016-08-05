from django.db import models

class Formula(models.Model):
    name = models.CharField( max_length=255,)
    value = models.CharField( max_length=255,)
    attribute = models.CharField(max_length=255,)
    updatedBy = models.CharField(max_length=255,)
    references = models.CharField( max_length=255,)
    permissions = models.CharField(max_length=255,)
    updatedAt = models.CharField( max_length=255,)
