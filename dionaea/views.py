from rest_framework.decorators import authentication_classes, permission_classes, api_view, action
from rest_framework.response import Response
from rest_framework.renderers import JSONRenderer
from rest_framework_mongoengine import viewsets

from dionaea.serializers import TrapSerializer
from dionaea.serializers import TestSerializer
from dionaea.models import Trap
from dionaea.models import Test

from rest_framework.permissions import IsAuthenticated
from rest_framework_jwt.authentication import JSONWebTokenAuthentication


# @authentication_classes((JSONWebTokenAuthentication,))
# @permission_classes((IsAuthenticated,))
class TrapViewSet(viewsets.ModelViewSet):
    lookup_field = 'shorten_key'
    queryset = Trap.objects.all().order_by('-created_at')
    serializer_class = TrapSerializer


class TestViewSet(viewsets.ModelViewSet):
    lookup_field = 'id'
    queryset = Test.objects.all()
    serializer_class = TestSerializer


@api_view(['GET'])
def trap_list(request):
    traps = Trap.objects.all()
    serializer = TrapSerializer(traps, many=True)
    print(request.META['HTTP_USER_AGENT'])
    print(request.META['REMOTE_ADDR'])

    return Response(serializer.data)


@api_view(['GET'])
def trap_detail(request, shorten_key):
    traps = Trap.objects.get(shorten_key)
    serializer = TrapSerializer(traps)

    print(request)

    return Response(serializer.data)


@permission_classes((IsAuthenticated,))
@authentication_classes((JSONWebTokenAuthentication,))
@api_view(['POST'])
def trap_post(request):
    return Response({"message": "post"})
