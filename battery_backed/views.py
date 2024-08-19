from rest_framework import viewsets
from .models import StateOfCharge
from .serializers import BatterySocSerializer
from django.utils import timezone

class StateViewSet(viewsets.ModelViewSet):
    queryset = StateOfCharge.objects.all()
    serializer_class = BatterySocSerializer

    def get_queryset(self):
        queryset =  super().get_queryset()        
        date_range = self.request.query_params.get('date_range',None)     

        # Filter by date_range if provided
        if date_range:
            today = timezone.now().date() 
            if date_range == 'today':
                queryset = queryset.filter(timestamp__gte=today)            
        return queryset