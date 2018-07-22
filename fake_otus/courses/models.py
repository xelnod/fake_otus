from django.db import models

from core.models import BaseModel


class Course(BaseModel):
    title = models.CharField(max_length=255)
    description = models.TextField(default='')
