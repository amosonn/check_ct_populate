from django.db import models

from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey


class Wrapper(models.Model):
    content_type = models.ForeignKey(ContentType)
    object_id = models.PositiveIntegerField(db_index=True)
    wrapped = GenericForeignKey('content_type', 'object_id')
