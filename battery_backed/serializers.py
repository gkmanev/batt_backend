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
    timestamp = serializers.SerializerMethodField()  # Use SerializerMethodField to rename

    class Meta:
        model = BatteryLiveStatus
        fields = ('devId', 'timestamp', 'state_of_charge', 'flow_last_min', 'invertor_power')

    def get_timestamp(self, obj):
        return obj.get('truncated_timestamp')  # Access the annotated field from the dictionary



# class BatteryLiveSerializer(serializers.ModelSerializer):
#     timestamp = serializers.ReadOnlyField()
#     avg_state_of_charge = serializers.ReadOnlyField()
#     avg_flow_last_min = serializers.ReadOnlyField()
#     avg_invertor_power = serializers.ReadOnlyField()

#     class Meta:
#         model = BatteryLiveStatus
#         fields = ('devId', 'timestamp', 'avg_state_of_charge', 'avg_flow_last_min', 'avg_invertor_power')




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
