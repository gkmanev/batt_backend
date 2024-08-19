from django.db import models
from datetime import datetime, timedelta
from pytz import timezone


class StateOfCharge(models.Model):
    timestamp = models.DateTimeField(auto_now=True)
    state_of_charge = models.FloatField(default=0)
    current_status = models.CharField(default="idle", max_length=50)
    invertor_power = models.FloatField(default=0)

    
    