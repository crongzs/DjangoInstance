'''
DRF Instance
'''

from app.models import Profile

from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.status import HTTP_200_OK
from rest_framework.response import Response
from rest_framework.views import APIView


class ProfileAPIView(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'app/hello.html'


    def post(self, request):
        return Response({'user': 'ku_rong'})