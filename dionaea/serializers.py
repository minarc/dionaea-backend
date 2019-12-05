from dionaea.models import Trap
from rest_framework_mongoengine import serializers

import hashlib


class TrapSerializer(serializers.DocumentSerializer):
    class Meta:
        model = Trap
        fields = '__all__'

    def create(self, validated_data):
        salt = "4[pSLc9;8Z76+ghe;(8nrkWXj~$"
        key = hashlib.sha256(f"{validated_data['target_url']}{salt}".encode('utf-8'))
        validated_data['shorten_key'] = key.hexdigest()

        return Trap.objects.create(**validated_data)
