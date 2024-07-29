from django.db import models

class DynamicModel(models.Model):
    model_name = models.CharField(max_length=255)
    data = models.JSONField()

    def __str__(self):
        return self.model_name
