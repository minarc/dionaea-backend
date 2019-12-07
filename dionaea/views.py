from rest_framework import status
from rest_framework.decorators import authentication_classes, permission_classes, api_view, action
from rest_framework.response import Response
from rest_framework_mongoengine import viewsets

from dionaea.serializers import TrapSerializer, PreySerializer, MakerSerializer, TestSerializer
from dionaea.models import Trap, Prey, Maker, Test

from rest_framework.permissions import IsAuthenticated
from rest_framework_jwt.authentication import JSONWebTokenAuthentication


# @authentication_classes((JSONWebTokenAuthentication,))
# @permission_classes((IsAuthenticated,))
class TrapViewSet(viewsets.ModelViewSet):
    lookup_field = 'shorten_key'
    queryset = Trap.objects.all().order_by('-created_at')
    serializer_class = TrapSerializer

    def retrieve(self, request, *args, **kwargs):
        queryset = Trap.objects.filter(shorten_key=kwargs['shorten_key'])
        serializer = self.get_serializer(queryset, many=True)

        if serializer.data:
            target_url = serializer.data[0]['target_url']
            return Response(status=status.HTTP_301_MOVED_PERMANENTLY, headers={'Location': target_url})
        else:
            return Response(status=status.HTTP_404_NOT_FOUND)


class PreyViewSet(viewsets.ModelViewSet):
    lookup_field = 'shorten_key'
    queryset = Prey.objects.all()
    serializer_class = PreySerializer

    def retrieve(self, request, *args, **kwargs):
        queryset = Prey.objects.filter(shorten_key=kwargs['shorten_key'])
        serializer = self.get_serializer(queryset, many=True)

        if serializer.data:
            return Response(data=serializer.data)
        else:
            return Response(status=status.HTTP_404_NOT_FOUND)


class MakerViewSet(viewsets.ModelViewSet):
    queryset = Maker.objects.all()
    serializer_class = MakerSerializer

    @action(detail=True, methods=['POST'])
    def traps(self, request, *args, **kwargs):
        serializer = MakerSerializer(self.get_object())
        serializer.data['trap'] = {'test': 'test'}

        serializer = MakerSerializer(data=serializer.data)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)

        return Response(status=status.HTTP_201_CREATED)
