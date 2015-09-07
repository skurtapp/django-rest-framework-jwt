from django.db import models


class ParseUserProxy(models.Model):
    """
    A proxy model to the Parse User table
    """
    objectId = models.CharField(unique=True, max_length=16, primary_key=True)

    def __str__(self):
        return self.objectId
