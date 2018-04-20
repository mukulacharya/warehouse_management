import datetime

from django.contrib.auth.models import User
from django.db import models


class BaseModel(models.Model):
    created_on = models.DateTimeField(editable=False, default=datetime.datetime.now)
    updated_on = models.DateTimeField(editable=False, auto_now=True)
    created_by = models.ForeignKey(User, editable=False, blank=True, null=True,
                                   related_name="%(class)s_created_by")
    updated_by = models.ForeignKey(User, editable=False, blank=True, null=True,
                                   related_name="%(class)s_updated_by")

    class Meta:
        abstract = True

    def save(self, *args, **kwargs):
        super(BaseModel, self).save(*args, **kwargs)
