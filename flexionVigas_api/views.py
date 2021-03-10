from typing import Dict
from warnings import catch_warnings
from rest_framework import renderers, response
from rest_framework.generics import get_object_or_404
from .serializer import VigaSerializer
from .models import VigaRectangular
from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response

# Create your views here.


class VigaView(viewsets.ModelViewSet):
    serializer_class = VigaSerializer
    queryset = VigaRectangular.objects.all()

    def create(self, request, *args, **kwargs):
        viga_data = request.data
        new_viga = VigaRectangular.objects.create(
            bw=float(viga_data["bw"]), hw=float(viga_data["hw"]), r=float(viga_data["r"]), fc=float(viga_data["fc"]), fy=float(viga_data["fy"]),
            Mu=float(viga_data["Mu"]), phiFlexion=float(viga_data["phiFlexion"]))

        new_viga.initialize()
        new_viga.save()

        serializer = VigaSerializer(new_viga)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def retrieve(self, request, *args, **kwargs):
        print(self)
        return super().retrieve(request, *args, **kwargs)

    @action(detail=True)
    def myGet(self, request, pk=None):
        viga = get_object_or_404(self.queryset, pk=pk)
        serializer = VigaSerializer(viga)
        return Response(serializer.data, status.HTTP_200_OK)

    @action(detail=True, methods=['post'])
    def updateFlexion(self, request, pk=None):
        viga_data: Dict = request.data
        vigai = get_object_or_404(self.queryset, pk=pk)

        vigai.bw = float(viga_data["bw"])
        vigai.hw = float(viga_data["hw"])
        vigai.r = float(viga_data["r"])
        vigai.fc = float(viga_data["fc"])
        vigai.fy = float(viga_data["fy"])
        vigai.Mu = float(viga_data["Mu"])
        vigai.phiFlexion = float(viga_data["phiFlexion"])

        vigai.initialize()
        vigai.save()
        VigaRectangular.objects.update()

        serializer = VigaSerializer(vigai)
        return Response(serializer.data, status.HTTP_200_OK)

    @action(detail=True, methods=['post'])
    def chequeoVigaFlexion(self, request, pk=None):
        viga_data: Dict = request.data
        vigai: VigaRectangular

        try:
            vigai = get_object_or_404(self.queryset, pk=pk)
            vigai.bw = float(viga_data["bw"])
            vigai.hw = float(viga_data["hw"])
            vigai.r = float(viga_data["r"])
            vigai.fc = float(viga_data["fc"])
            vigai.fy = float(viga_data["fy"])
            vigai.phiFlexion = float(viga_data["phiFlexion"])
        except:
            vigai = VigaRectangular.objects.create(
                bw=float(viga_data["bw"]), hw=float(viga_data["hw"]), r=float(viga_data["r"]), fc=float(viga_data["fc"]), fy=float(viga_data["fy"]), phiFlexion=float(viga_data["phiFlexion"]))

        vigai.asReq = float(viga_data["asReq"])
        vigai.asReq2 = float(viga_data["asReq2"])
        vigai.d = vigai.hw-vigai.r
        vigai.asTemp = vigai.calcAsTemp()
        vigai.asMin = vigai.calcAsMin()
        vigai.cuantiaTemp = vigai.calcCuantia(vigai.asTemp, vigai.hw)
        vigai.cuantiaMin = vigai.calcCuantia(vigai.asMin, vigai.d)
        vigai.cuantiaMax = vigai.calcCuantiaMax()
        vigai.asMax = vigai.calcAsMax()
        vigai.phiMnMax = vigai.calcPhiMn1(vigai.asMax, vigai.d)

        if vigai.asReq2 == 0:
            vigai.phiMn = vigai.calcPhiMn1(vigai.asReq, vigai.d)            
        else:
            vigai.phiMn = vigai.calcPhiMn2(vigai.asReq, vigai.asReq2)

        vigai.cuantiaReq=vigai.calcCuantia(vigai.asReq,vigai.d)
        vigai.save()
        VigaRectangular.objects.update()

        serializer = VigaSerializer(vigai)
        return Response(serializer.data, status.HTTP_200_OK)
