from dionaea.models import Trap
from rest_framework_mongoengine import serializers

import hashlib
import os


class TrapSerializer(serializers.DocumentSerializer):
    class Meta:
        model = Trap
        fields = '__all__'

    def create(self, validated_data):
        salt = os.environ['DJANGO_SECRET_KEY']
        key = hashlib.sha256(f"{validated_data['target_url']}{salt}".encode('utf-8'))
        validated_data['shorten_key'] = key.hexdigest()

        return Trap.objects.create(**validated_data)
