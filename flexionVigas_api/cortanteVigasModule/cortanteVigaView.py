from rest_framework.decorators import action
from flexionVigas_api.cortanteVigasModule.cortanteVigaSerializer import cortanteVigaSerializer
from flexionVigas_api.cortanteVigasModule.cortanteViga import cortanteViga
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import mixins, serializers, status, viewsets


class cortanteVigaView(viewsets.GenericViewSet, mixins.RetrieveModelMixin):
    serializer_class = cortanteVigaSerializer

    def createModel(self, data):
        cortante = cortanteViga(float(data["bw"]), float(data["hw"]), float(data["r"]), float(
            data["fc"]), float(data["fy"]), float(data["phiCortante"]), float(data["vu"]), float(data["asCortante"]), float(data["separacionAs"]))
        return cortante

    @action(detail=True, methods=['post'])
    def disenioSeccion(self, request):
        data = request.data
        cortante = self.createModel(data)

        if cortante.separacionAs > 0:
            cortante.asCortante = cortante.calcAs(cortante.separacionAs)
        elif cortante.asCortante > 0:
            cortante.separacionAs = cortante.calcSep(cortante.asCortante)
        else:
            return Response("almenos un campo entre separacion y as debe ser diferente de 0", status=status.HTTP_400_BAD_REQUEST)

        serializer = cortanteVigaSerializer(cortante)
        return Response(serializer.data, status=status.HTTP_200_OK)

    @action(detail=True, methods=['post'])
    def chequeoSeccion(self, request):
        data = request.data
        cortante = self.createModel(data)
        if cortante.separacionAs > 0 and cortante.asCortante > 0:
            cortante.phiVs = cortante.calcPhiVs(
                cortante.separacionAs, cortante.asCortante)
            serializer = cortanteVigaSerializer(cortante)
            return Response(serializer.data, status=status.HTTP_200_OK)

        return Response("Faltan datos", status=status.HTTP_400_BAD_REQUEST)
