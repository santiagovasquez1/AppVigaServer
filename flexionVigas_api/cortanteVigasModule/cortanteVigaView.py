from flexionVigas_api.cortanteVigasModule.cortanteVigaSerializer import cortanteVigaSerializer
from flexionVigas_api.cortanteVigasModule.cortanteViga import cortanteViga
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

class cortanteVigaView(APIView):
    def post(self, request):
        data = request.data
        cortante=cortanteViga(float(data["bw"]),float(data["hw"]),float(data["r"]),float(data["fc"]),float(data["fy"]))
        serializer=cortanteVigaSerializer(cortante)
        # if serializer.is_valid():
        #     return Response(serializer.data,status=status.HTTP_200_OK)
        return Response(serializer.data,status=status.HTTP_200_OK)