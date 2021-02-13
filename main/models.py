from django.db import models


class BaseModel(models.Model):
    creation_date = models.DateTimeField(auto_now_add=True, null=True)
    update_date = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(null=True, default=True)

    class Meta:
        abstract = True
