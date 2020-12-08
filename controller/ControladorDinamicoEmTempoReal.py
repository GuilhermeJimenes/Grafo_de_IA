from controller.Preenchimento import Preenchimento
from model.ArquivosExternos import ArquivosExternos

class ControladorDinamicoEmTempoReal(Preenchimento):
    def __init__(self):
        #dadosGrafos = super().pegarDados()
        self.ultimoJogoAnterior = self.manipularDados(self.jogadasFormatadas, self.scoresFormatados)
        self.isFirstTime = True


    def atualizarDados(self):
        isDifferent = False
        dadosGrafo = super().pegarDados()

        if(len(dadosGrafo)>0):
            if dadosGrafo[len(dadosGrafo) - 1] != self.ultimoJogoAnterior or self.isFirstTime:
                self.ultimoJogoAnterior = dadosGrafo[len(dadosGrafo)-1]
                super().separar(dadosGrafo, self.jogadasFormatadas, self.scoresFormatados)
                self.ultimasDuplasjogadas = super().verificarDuplasDeNosExperimentadas(self.jogadasFormatadas, self.scoresFormatados)
                isDifferent = True
                self.isFirstTime = False

        return isDifferent