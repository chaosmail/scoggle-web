import datetime

from django.db import models


class AutoDateTimeField(models.DateTimeField):
    """Creates a datetime field that automatically
    updates when the entry is edited""" 
    def pre_save(self, model_instance, add):
        return datetime.datetime.now()

