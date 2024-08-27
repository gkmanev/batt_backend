from django.db import models
from datetime import datetime, timedelta
from pytz import timezone


class BatteryLiveStatus(models.Model):
    devId = models.CharField(default='batt-0001', max_length=20)
    timestamp = models.DateTimeField(auto_now=True)
    state_of_charge = models.FloatField(default=0)
    flow_last_min = models.FloatField(default=0)
    invertor_power = models.FloatField(default=0)

    
    