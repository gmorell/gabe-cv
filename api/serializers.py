from rest_framework import serializers

class NightShiftSerializer(serializers.Serializer):
    enabled = serializers.BooleanField(default=False)