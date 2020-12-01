from model.ArquivosExternos import ArquivosExternos


class TrataBase:
    def __init__(self):
        pass

    def iniciaTratamento(self):
        base, jogadaInteligente, scoreInteligente = self.__trataBase()
        jogadasFormatadas = self.__vetorParaString(jogadaInteligente)
        scoresFormatados = self.__vetorParaString(scoreInteligente)
        return jogadasFormatadas, scoresFormatados

    def __vetorParaString(self, vetor):
        elementosFormatados = []
        for elementos in vetor:
            elementosFormatados.append(str(elementos).strip('[]'))
        return elementosFormatados

    def __trataBase(self):
        base = ArquivosExternos().pega('InteligenteDados')
        print(base)
        jogadaInteligente = base.pop('jogadasInteligente')
        scoreInteligente = base.pop('scoreInteligente')
        return base, jogadaInteligente, scoreInteligente
