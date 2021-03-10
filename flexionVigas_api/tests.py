from rest_framework import serializers
from flexionVigas_api.cortanteVigasModule.cortanteViga import cortanteViga
from flexionVigas_api.cortanteVigasModule.cortanteVigaSerializer import cortanteVigaSerializer
from flexionVigas_api.models import VigaRectangular
from django.test import TestCase

# Create your tests here.

class TestFlexionVigas(TestCase):

    # Prueba unitaria para el chequeo de seccion doblemente reforzada
    def testVigaDoblementeReforzada1(self):
        vigaTest = VigaRectangular.objects.create(
            bw=25, hw=35, r=5, fc=210, fy=4200, Mu=13.08, phiFlexion=0.90)
        vigaTest.initialize()
        phiMn=round(vigaTest.phiMn,2)
        self.assertGreaterEqual(phiMn , vigaTest.Mu)

    def testVigaDoblementeReforzada2(self):
        vigaTest = VigaRectangular.objects.create(
            bw=30, hw=40, r=6, fc=210, fy=4220, Mu=19, phiFlexion=0.90)
        vigaTest.initialize()
        phiMn=round(vigaTest.phiMn,2)
        self.assertGreaterEqual(phiMn , vigaTest.Mu)

    def testVigaSimplementeReforzada(self):
        vigaTest = VigaRectangular.objects.create(
            bw=25, hw=30, r=6, fc=210, fy=2800, Mu=6.93, phiFlexion=0.90)
        vigaTest.initialize()
        self.assertGreaterEqual(vigaTest.asReq,14.03)

    def testChequeoVigaDoblementeReforzada1(self):
        vigaTest = VigaRectangular.objects.create(
            bw=25, hw=50, r=5, d=40, fc=210, fy=2800, phiFlexion=0.90, asReq=17.94, asReq2=4)
        phiMnDef = vigaTest.calcPhiMn2(vigaTest.asReq, vigaTest.asReq2)
        self.assertGreaterEqual(phiMnDef, 16.04)

    def testChequeoVigaDoblementeReforzada2(self):
        vigaTest = VigaRectangular.objects.create(
            bw=25, hw=35, r=5, d=30, fc=210, fy=4200, phiFlexion=0.90, asReq=20.40, asReq2=2.58)
        phiMnDef = vigaTest.calcPhiMn2(vigaTest.asReq, vigaTest.asReq2)
        self.assertGreaterEqual(phiMnDef, 16.17)

class TestCortanteViga(TestCase):
    def testSerializerObject(self):
        cortanteTest = cortanteViga(30, 50, 6, 210, 4220)
        serializer=cortanteVigaSerializer(cortanteTest)
        serializer.data
        print(serializer.data)
        # self.assertJSONEqual("{'bw': 30.0, 'hw': 50.0, 'r': 6.0, 'fc': 210.0, 'fy': 4220.0, 'd': 44.0}",serializer.data)
        # self.assertTrue(serializer.data.values)