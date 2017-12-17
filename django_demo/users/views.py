from constance import config
from rest_framework.decorators import api_view, authentication_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response


@api_view(['GET'])
@authentication_classes((AllowAny,))
def home(requset):
    data = {'answer': config.THE_ANSWER}
    return Response(data)
