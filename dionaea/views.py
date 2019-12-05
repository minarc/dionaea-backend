from rest_framework.decorators import authentication_classes, permission_classes, api_view, action
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_mongoengine import viewsets

from dionaea.serializers import TrapSerializer
from dionaea.models import Trap

from rest_framework.permissions import IsAuthenticated
from rest_framework_jwt.authentication import JSONWebTokenAuthentication


# @authentication_classes((JSONWebTokenAuthentication,))
# @permission_classes((IsAuthenticated,))
class TrapViewSet(viewsets.ModelViewSet):
    lookup_field = 'shorten_key'
    queryset = Trap.objects.all().order_by('-created_at')
    serializer_class = TrapSerializer


@api_view(['GET'])
def trap(request):
    return Response({"message": "get"})


@permission_classes((IsAuthenticated,))
@authentication_classes((JSONWebTokenAuthentication,))
@api_view(['POST'])
def trap_post(request):
    return Response({"message": "post"})
