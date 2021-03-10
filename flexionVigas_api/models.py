from django.db import models
import math
import numpy as np

# Create your models here.


class VigaRectangular(models.Model):

    bw = models.DecimalField(max_digits=5, decimal_places=2)
    hw = models.DecimalField(max_digits=5, decimal_places=2)
    r = models.DecimalField(max_digits=4, decimal_places=2)
    fc = models.DecimalField(max_digits=5, decimal_places=2)
    fy = models.DecimalField(max_digits=6, decimal_places=2)

    d = models.DecimalField(
        max_digits=5, decimal_places=2, blank=True, null=True)
    cuantiaTemp = models.DecimalField(
        max_digits=5, decimal_places=4, blank=True, null=True)
    cuantiaMin = models.DecimalField(
        max_digits=5, decimal_places=4, blank=True, null=True)
    cuantiaMax = models.DecimalField(
        max_digits=5, decimal_places=4, blank=True, null=True)
    cuantiaReq = models.DecimalField(
        max_digits=5, decimal_places=4, blank=True, null=True)

    asTemp = models.DecimalField(
        max_digits=5, decimal_places=2, blank=True, null=True)
    asMin = models.DecimalField(
        max_digits=5, decimal_places=2, blank=True, null=True)
    asMax = models.DecimalField(
        max_digits=5, decimal_places=2, blank=True, null=True)
    asReq = models.DecimalField(
        max_digits=5, decimal_places=2, blank=True, null=True)
    asReq2 = models.DecimalField(
        max_digits=5, decimal_places=2, blank=True, null=True)

    Mu = models.DecimalField(
        max_digits=6, decimal_places=2, blank=True, null=True)
    phiFlexion = models.DecimalField(
        max_digits=5, decimal_places=2, blank=True, null=True)
    phiMn = models.DecimalField(
        max_digits=6, decimal_places=2, blank=True, null=True)
    phiMnMax = models.DecimalField(
        max_digits=6, decimal_places=2, blank=True, null=True)

    def initialize(self):
        self.d = round(self.hw-self.r, 2)
        self.asTemp = round(self.calcAsTemp(), 2)
        self.asMin = round(self.calcAsMin(), 2)
        self.cuantiaTemp = round(self.calcCuantia(self.asTemp, self.hw), 4)
        self.cuantiaMin = round(self.calcCuantia(self.asMin, self.d), 4)
        self.cuantiaMax = round(self.calcCuantiaMax(), 4)
        self.asMax = round(self.calcAsMax(), 2)
        self.phiMnMax = round(self.calcPhiMn1(self.asMax, self.d), 2)
        self.calcAsDef()

    def calcCuantia(self, asReq, dw):
        return (asReq/(self.bw*dw))

    def calcAsMin(self):
        cuantiaMin1 = (0.8*np.sqrt(self.fc)/self.fy)*(self.bw*self.d)
        cuantiaMin2 = 14*self.bw*self.d/self.fy
        if cuantiaMin1 >= cuantiaMin2:
            return cuantiaMin1
        else:
            return cuantiaMin2

    def calcAsReq(self):
        if self.Mu != None and self.phiFlexion > 0:
            a = -(self.phiFlexion*np.power(self.fy, 2)/(2*0.85*self.fc*self.bw))
            b = self.phiFlexion*self.fy*self.d
            c = -self.Mu*np.power(10, 5)
            raiz = np.sqrt(np.power(b, 2)-(4*a*c))
            asReq1 = (-b+raiz)/(2*a)
            asReq2 = (-b-raiz)/(2*a)

            if min(asReq1, asReq2) > 0:
                return min(asReq1, asReq2)
            else:
                return max(asReq1, asReq2)
        else:
            return 0

    def calcAsTemp(self):
        return 0.0018*self.bw*self.hw

    def calcAsMax(self):
        return self.bw*self.d*self.cuantiaMax

    def calcPhiMn1(self, asReq, dw):
        if asReq > 0:
            aWhitney = (asReq*self.fy)/(0.85*self.fc*self.bw)
            phiMn = self.phiFlexion*asReq * \
                self.fy*(dw-(aWhitney/2))
            return phiMn/(np.power(10, 5))
        else:
            return 0

    def calcAsDef(self):
        if(self.Mu > self.phiMnMax):
            mc = (self.Mu-self.phiMnMax)*(np.power(10, 5))
            div = self.phiFlexion*self.fy*(self.d-self.r)
            self.asReq2 = round(mc/div, 2)
            self.asReq = round(self.asMax+self.asReq2, 2)
            self.cuantiaReq = round(self.cuantiaMax, 4)
            self.phiMn = round(self.calcPhiMn2(self.asReq, self.asReq2), 2)
        else:
            self.asReq = round(self.calcAsReq(), 2)
            self.asReq2 = round(0, 2)
            self.cuantiaReq = round(self.calcCuantia(self.asReq, self.d), 4)
            self.phiMn = round(self.calcPhiMn1(self.asReq, self.d), 2)

    def calcPhiMn2(self, asInferior, asSuperior):
        fs = self.calcFs(asInferior, asSuperior)
        aWhitney = (asInferior*self.fy-asSuperior*fs)/(0.85*self.fc*self.bw)
        phiMnConcreto = 0.90*0.85*aWhitney * \
            self.fc*self.bw*(self.d-(aWhitney/2))
        phiMnAceroComp = 0.90*asSuperior*fs*(self.d-self.r)
        return (phiMnConcreto+phiMnAceroComp)/(np.power(10, 5))

    def calcFs(self, asInferior, asSuperior):
        alpha = self.calcAlpha()
        limitFy = alpha*(self.fc/self.fy)*(6000/(6000-self.fy))*(self.r/self.d)
        cuantiaNet = self.calcCuantia(asInferior+asSuperior, self.d)

        if(cuantiaNet >= limitFy):
            fs = self.fy
        else:
            c = self.calcEjeNeutro()
            fs = 6000*((c-self.r)/c)
        return fs

    def calcEjeNeutro(self):
        Es = 2*np.power(10, 6)
        ess = self.fy/Es
        euc = 0.003
        return euc*self.d/(ess+euc)

    def calcAlpha(self):
        alpha = 0
        if self.fc <= 280:
            alpha = 0.7225
        else:
            alpha = 0.7225+(((self.fc-280)/70)*(-0.04))
        return alpha

    def calcCuantiaMax(self):

        alpha = self.calcAlpha()
        phiMax1 = 0
        phiMax2 = 0.025

        phiMax1 = (0.75*alpha*(self.fc/self.fy))*(6000/(6000+self.fy))

        if phiMax1 <= phiMax2:
            return phiMax1
        else:
            return phiMax2

    def __str__(self):
        return (f"Viga{self.pk}-{self.bw}X{self.hw}")

