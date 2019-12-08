from dionaea.models import Maker, Prey, Trap
from rest_framework_mongoengine import serializers

import requests
import json
import nanoid


class MakerSerializer(serializers.DocumentSerializer):
    class Meta:
        model = Maker
        fields = '__all__'


class TrapSerializer(serializers.DocumentSerializer):
    class Meta:
        model = Trap
        fields = '__all__'

    def create(self, validated_data):
        validated_data['shorten_key'] = nanoid.generate(size=8)

        return Trap.objects.create(**validated_data)


class PreySerializer(serializers.DocumentSerializer):
    class Meta:
        model = Prey
        fields = '__all__'

    def create(self, validated_data):
        url = f"https://freegeoip.app/json/{validated_data['ip_address']}"
        response = requests.request("GET", url)
        response = json.loads(response.content)

        validated_data['geo_point'] = [response['latitude'], response['longitude']]
        validated_data['region_name'] = response['region_name']
        validated_data['city'] = response['city']

        return Prey.objects.create(**validated_data)
