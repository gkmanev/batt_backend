from rest_framework import viewsets
from .models import BatteryLiveStatus
from .serializers import BatteryLiveSerializer
from django.utils import timezone

class StateViewSet(viewsets.ModelViewSet):
    queryset = BatteryLiveStatus.objects.all()
    serializer_class = BatteryLiveSerializer
    queryset = queryset.filter(state_of_charge__gte=0, state_of_charge__lte=100)

    def get_queryset(self):
        queryset =  super().get_queryset()        
        date_range = self.request.query_params.get('date_range',None)     

        # Filter by date_range if provided
        if date_range:
            today = timezone.now().date()           
            if date_range == 'today':
                queryset = queryset.filter(timestamp__gte=today).order_by('timestamp')

        return queryset