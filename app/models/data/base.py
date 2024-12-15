from django.db import models


class DataRoot(models.Model):
    created_at = models.DateTimeField(auto_now=True)