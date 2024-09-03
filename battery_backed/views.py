from rest_framework import viewsets
from .models import BatteryLiveStatus
from .serializers import BatteryLiveSerializer,BatteryLiveAggregatedByDaySerializer,BatteryLiveAggregatedByHourSerializer
from django.db.models import Case, When, Value, F, FloatField



class StateViewSet(viewsets.ModelViewSet):
    
    queryset = BatteryLiveStatus.objects.all()   

    def get_serializer_class(self):
        # Determine if you're dealing with raw data or aggregated data
        date_range = self.request.query_params.get('date_range', None)
        if date_range == 'year':
            return BatteryLiveAggregatedByDaySerializer  # Use the serializer for yearly aggregation (by day)
        elif date_range == 'month':
            return BatteryLiveAggregatedByHourSerializer  # Use the serializer for monthly aggregation (by hour)
        return BatteryLiveSerializer  # Use the raw data serializer for other cases


    def get_queryset(self):
        queryset = super().get_queryset()

        # Applying filters based on query parameters
        date_range = self.request.query_params.get('date_range', None)     
        dev_id = self.request.query_params.get('devId', None)

        if date_range:
            if date_range == 'today':
                queryset = BatteryLiveStatus.today.all()
            elif date_range == 'month':
                queryset = BatteryLiveStatus.month.all()
            else:
                queryset = BatteryLiveStatus.year.all()

        if dev_id:
            queryset = queryset.filter(devId=dev_id)

        # Adjust state_of_charge to be within 0-100 range in a single database operation
        queryset = queryset.annotate(
            adjusted_soc=Case(
                When(state_of_charge__lte=0, then=Value(0)),
                When(state_of_charge__gte=100, then=Value(100)),
                default=F('state_of_charge'),
                output_field=FloatField()
            )
        )

        return queryset
