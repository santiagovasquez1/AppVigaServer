from flexionVigas_api.cortanteVigasModule.IViga import IViga
import math


class cortanteViga(IViga):
    phiCortante: float
    d: float
    phiVc: float
    phiVs: float
    phiVn: float
    phiVsMax: float
    phiVnMax: float
    asCortante: float
    separacionAs: float
    Vu: float

    def __init__(self, bw, hw, r, fc, fy, phiCortante, vu, asCortante, separacionAs):
        super().__init__(bw, hw, r, fc, fy)
        self.Vu = vu
        self.d = self.hw-self.r
        self.phiCortante = phiCortante
        self.asCortante = asCortante
        self.separacionAs = separacionAs
        self.phiVc = self.calcPhiVc()
        self.phiVsMax = self.calcPhiVsMax()
        self.phiVnMax = self.calcPhiVnMax()

    def calcPhiVc(self):
        return 0.53*self.bw*self.d*self.phiCortante*math.sqrt(self.fc)/1000

    def calcPhiVs(self, sep, asi):
        Vs = asi*self.fy*self.d/sep
        return self.phiCortante*Vs/1000

    def calcAs(self, sep):
        if(self.phiVc > 0):
            phiVs = (self.Vu-self.phiVc)*1000
            asi = sep*phiVs/(self.phiCortante*self.fy*self.d)
            self.phiVs = self.calcPhiVs(sep, asi)
            return asi
        else:
            return 0

    def calcSep(self, asi):
        if(self.phiVc > 0):
            phiVs = (self.Vu-self.phiVc)*1000
            sep = self.phiCortante*asi*self.fy*self.d/phiVs
            self.phiVs = self.calcPhiVs(sep, asi)
            return sep
        else:
            return 0

    def calcPhiVsMax(self):
        return (self.phiCortante * 2.2*math.sqrt(self.fc)*self.bw*self.d)/1000

    def calcAvmin(self, sep):
        avmin1 = 0.2*math.sqrt(self.fc)*self.bw*sep/self.fy
        avmin2 = 3.5*self.bw*sep/self.fy
        if avmin1 > avmin2:
            return avmin1
        else:
            return avmin2

    def calcPhiVnMax(self):
        return self.phiCortante*2.65*math.sqrt(self.fc)*self.bw*self.d/1000
