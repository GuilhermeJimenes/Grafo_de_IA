from model.ArquivosExternos import ArquivosExternos


class TrataBase:
    def __init__(self):
        pass

    def iniciaTratamento(self):
        base, jogadasDaRodada, scoreDaRodada = self.__trataBase()
        jogadasFormatadas = self.__vetorParaString(jogadasDaRodada)
        scoresFormatados = self.__vetorParaString(scoreDaRodada)
        return jogadasFormatadas, scoresFormatados

    def __vetorParaString(self, vetor):
        elementosFormatados = []
        for elementos in vetor:
            elementosFormatados.append(str(elementos).strip('[]'))
        return elementosFormatados

    def __trataBase(self):
        base = ArquivosExternos().pega('InteligenteDados')
        print(base)
        jogadasDaRodada = base.pop('jogadasDaRodada')
        scoreDaRodada = base.pop('scoreDaRodada')
        return base, jogadasDaRodada, scoreDaRodada
