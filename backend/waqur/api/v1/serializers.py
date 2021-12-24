from rest_framework import serializers
from waqur.models import Test123


class Test123Serializer(serializers.ModelSerializer):
    class Meta:
        model = Test123
        fields = "__all__"
