from django.db import models

from django.contrib.auth.models import User
from datetime import datetime

class Transaction(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    amount = models.FloatField()
    status = models.CharField(max_length=20, default='pending')
    created_at = models.DateTimeField(default=datetime.now)
