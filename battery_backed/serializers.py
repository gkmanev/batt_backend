from rest_framework import serializers
from .models import StateOfCharge


class BatterySocSerializer(serializers.ModelSerializer):
    timestamp = serializers.SerializerMethodField()
    class Meta:
        model = StateOfCharge
        fields = '__all__'
    
    def get_timestamp(self, obj):
        # Return the timestamp formatted to minute resolution
        return obj.timestamp.strftime('%Y-%m-%d %H:%M')
