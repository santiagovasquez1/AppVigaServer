from flexionVigas_api.cortanteVigasModule.IViga import IViga
import math


class cortanteViga(IViga):
    phiCortante: float
    d: float
    phiVc: float

    def __init__(self, bw, hw, r, fc, fy):
        super().__init__(bw, hw, r, fc, fy)
        self.d = self.hw-self.r
        self.phiCortante = 0.75
        self.phiVc = self.calcPhiCortante()

    def calcPhiCortante(self):
        return 0.53*self.bw*self.d*self.phiCortante*math.sqrt(self.fc)/1000
