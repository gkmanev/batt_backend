from django.db import models
from datetime import datetime, timedelta
from pytz import timezone



class MonthManager(models.Manager):    
    def get_queryset(self):
        today = datetime.now(timezone('Europe/London')).date()
        beginning_of_month = today.replace(day=1)
        return super().get_queryset().filter(timestamp__gt = beginning_of_month).order_by('timestamp')


class YearManager(models.Manager):    
    def get_queryset(self):
        today = datetime.now(timezone('Europe/London')).date()
        beginning_of_year = today.replace(month=1, day=1)
        return super().get_queryset().filter(timestamp__gt = beginning_of_year).order_by('timestamp')


class TodayManager(models.Manager):
    def get_queryset(self):
        today = datetime.now(timezone('Europe/London')).date()
        tomorrow = today + timedelta(1)
        today_start = str(today)+'T'+'00:00:00Z'
        today_end = str(tomorrow)+'T'+'00:00:00Z'
        return super().get_queryset().filter(timestamp__gt = today_start, timestamp__lt = today_end).order_by('timestamp')


class BatteryLiveStatus(models.Model):
    devId = models.CharField(default='batt-0001', max_length=20)
    timestamp = models.DateTimeField()
    state_of_charge = models.FloatField(default=0)
    flow_last_min = models.FloatField(default=0)
    invertor_power = models.FloatField(default=0)
    today = TodayManager()
    month = MonthManager()
    year = YearManager()
    objects = models.Manager()

    
    