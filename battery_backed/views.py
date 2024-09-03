from rest_framework import viewsets
from .models import BatteryLiveStatus
from .serializers import BatteryLiveSerializer
from django.utils import timezone

class StateViewSet(viewsets.ModelViewSet):
    queryset = BatteryLiveStatus.objects.all()
    serializer_class = BatteryLiveSerializer
    

    def get_queryset(self):
        queryset =  super().get_queryset()        
        date_range = self.request.query_params.get('date_range', None)     
        dev_id = self.request.query_params.get('devId', None)
        # Filter by date_range if provided
        if date_range:                
            if date_range == 'today':
                if dev_id:
                    queryset = BatteryLiveStatus.today.filter(devId=dev_id)
                else:
                    queryset = BatteryLiveStatus.today.all()
            elif date_range == 'month':
                if dev_id:
                    queryset = BatteryLiveStatus.month.filter(devId=dev_id)
                else:
                    queryset = BatteryLiveStatus.month.all()
            else:
                if dev_id:
                    queryset = BatteryLiveStatus.year.filter(devId=dev_id)
                else:
                    queryset = BatteryLiveStatus.year.all()

            # Adjust the state_of_charge values based on your conditions
        for obj in queryset:
            if obj.state_of_charge <= 0:
                obj.state_of_charge = 0
            elif obj.state_of_charge >= 100:
                obj.state_of_charge = 100

        return queryset