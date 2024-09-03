from rest_framework import serializers
from .models import BatteryLiveStatus


# class BatteryLiveSerializer(serializers.ModelSerializer):
#     timestamp = serializers.SerializerMethodField()
#     class Meta:
#         model = BatteryLiveStatus
#         fields = '__all__'
    
#     def get_timestamp(self, obj):
#         # Return the timestamp formatted to minute resolution
#         return obj.timestamp.strftime('%Y-%m-%d %H:%M')


class BatteryLiveSerializer(serializers.ModelSerializer):
    timestamp = serializers.ReadOnlyField()

    class Meta:
        model = BatteryLiveStatus
        fields = ('devId','timestamp','state_of_charge','flow_last_min','invertor_power')




# class BatteryLiveAggregatedByDaySerializer(serializers.Serializer):
#     day = serializers.DateField()
#     avg_state_of_charge = serializers.FloatField()
#     avg_flow_last_min = serializers.FloatField()
#     avg_invertor_power = serializers.FloatField()

# class BatteryLiveAggregatedByHourSerializer(serializers.Serializer):
#     hour = serializers.DateTimeField()  # Adjusted to DateTimeField since we're aggregating by hour
#     avg_state_of_charge = serializers.FloatField()
#     avg_flow_last_min = serializers.FloatField()
#     avg_invertor_power = serializers.FloatField()
