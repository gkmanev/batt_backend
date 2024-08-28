from django.core.management.base import BaseCommand
from django.utils.dateparse import parse_datetime
from django.utils.timezone import make_aware
from datetime import timedelta
from battery_backed.models import BatteryLiveStatus

class Command(BaseCommand):
    help = 'Empty db'

    def handle(self, *args, **kwargs):
        BatteryLiveStatus.objects.all().delete()        

        self.stdout.write(self.style.SUCCESS('Database successfully empted'))
