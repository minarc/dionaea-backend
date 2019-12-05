from dionaea.models import Trap
from dionaea.models import Test
from rest_framework_mongoengine import serializers

import uuid
import os
import requests
import json


class TrapSerializer(serializers.DocumentSerializer):
    class Meta:
        model = Trap
        fields = '__all__'

    def create(self, validated_data):
        name = f"{validated_data['target_url']}{os.environ['DJANGO_SECRET_KEY']}"
        validated_data['shorten_key'] = str(uuid.uuid5(namespace=uuid.NAMESPACE_URL, name=name).hex)

        return Trap.objects.create(**validated_data)


class TestSerializer(serializers.DocumentSerializer):
    class Meta:
        model = Test
        fields = '__all__'

    def create(self, validated_data):
        url = f"https://freegeoip.app/json/{validated_data['ip_address']}"
        response = requests.request("GET", url)
        response = json.loads(response.content)

        validated_data['geo_point'] = [response['latitude'], response['longitude']]
        validated_data['region_name'] = response['region_name']
        validated_data['city'] = response['city']

        return Test.objects.create(**validated_data)
