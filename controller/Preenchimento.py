from model.TrataBase import TrataBase


class Preenchimento:
    jogadasFormatadas = []
    scoresExperimentados = []
    duplasDeNosExperimentadas = []
    # labelsParaArestasExperimentadas = {}
    labelsParaNosExperimentados = {}
    listaDeScores = {}

    def __init__(self):
        self.jogadasFormatadas, scoresDaRodada = TrataBase().iniciaTratamento()
        print("aqui: ", self.jogadasFormatadas, "\n", scoresDaRodada)
        print(len(self.jogadasFormatadas))
        # ,,,,,,,,,,,,,,,self.scoresExperimentados = ClasseTratamentoDeDados().scoresPontuados
        self.verificarDuplasDeNosExperimentadas()

    '''
    def setLabelsParaArestasExperimentadas(self, duplaDeNos, posicaoAtual, posicaoAnterior):

        self.labelsParaArestasExperimentadas[(duplaDeNos[0], duplaDeNos[1])] = posicaoAtual #posicaoAnterior + "-" + posicaoAtual

    '''

    def setLabelsParaNosExperimentados(self, numeroDoGrafo, valorLabel):
        self.labelsParaNosExperimentados[numeroDoGrafo] = valorLabel

    def adicionarScoreNaLista(self, numeroDoGrafo, valorDoScore):
        if (numeroDoGrafo not in self.listaDeScores):
            self.listaDeScores.__setitem__(numeroDoGrafo, valorDoScore)

    def verificarDuplasDeNosExperimentadas(self):
        # 2) Lista de referências com os valores que representam os nós iniciais de cada camada (linha) do cérebro
        referencias = [1, 10, 82, 586, 3610, 18730, 79210, 260650, 623530]

        # 3) Este passo é só para mencionar a já declarada lista chamada de "duplasDeNosExperimentadas" que ficará responsável por receber cada dupla de nós já experimentada após a devida transformação

        # 4) Primeiro looping
        for i in range(len(self.jogadasFormatadas)):
            # 4.1) Variável que recebe todas as posições possíveis
            posicoesDeJogo = "012345678"

            # 4.2) Variável que guardará os valores transformados de cada posição anterior a que está atualmente sendo transformada
            numeroDoGrafoAnterior = -1

            # 4.3) Variável que recebe o jogo atual i da lista do passo 1;
            jogoAtual = self.jogadasFormatadas[i]
            # ,,,,,,,,,,,,scoresDoJogoAtual = self.scoresExperimentados[i]

            # 4.4) Segundo looping
            for j in range(len(jogoAtual)):
                # 4.4.1) Variável que será responsável por guardar o resultado da transformação;
                resultadoTransformacao = None

                # 4.4.2) Variável que guarda o valor presente na posição j do jogo i da lista do passo 1;
                valor = jogoAtual.__getitem__(j)
                # ,,,,,,,,,valorDoScore = scoresDoJogoAtual[:scoresDoJogoAtual.find("/")]

                # 4.4.3) Variável que guarda a posição onde o valor do passo 4.4.2 se encontra na variável do passo 4.1;
                posicao = posicoesDeJogo.find(valor)

                # 4.4.4) Primeira condição
                if numeroDoGrafoAnterior > -1:
                    # 4.4.4.1) Aplicação da fórmula de transformação...
                    resultadoTransformacao = referencias[j] + (
                            (numeroDoGrafoAnterior - referencias[j - 1]) * (9 - j)) + posicao

                    # 4.4.4.2) Lista com os valores dos passos 4.2 e 4.4.1 respectivamente
                    duplaAtual = [numeroDoGrafoAnterior, resultadoTransformacao]

                    # 4.4.4.3) Segunda condição
                    if duplaAtual not in self.duplasDeNosExperimentadas:
                        # 4.4.4.3.1) Insere a lista do passo 4.4.4.2 na lista do passo 3;
                        self.duplasDeNosExperimentadas.append(duplaAtual)

                        # self.setLabelsParaArestasExperimentadas(duplaAtual, valor, jogoAtual.__getitem__(j-1))
                        self.setLabelsParaNosExperimentados(duplaAtual[1], valor)

                # 4.4.5)...
                else:
                    # 4.4.5.1) Aplicação da fórmula de transformação adaptada
                    resultadoTransformacao = posicao + 1
                    self.setLabelsParaNosExperimentados(resultadoTransformacao, valor)

                # ,,,,,,,,,,,,,self.adicionarScoreNaLista(resultadoTransformacao, valorDoScore)

                # 4.4.6) Substituição do valor da variável do passo 4.4.2 por um valor vazio ("") na variável do passo 4.1;
                posicoesDeJogo = posicoesDeJogo.replace(valor, "")

                # 4.4.7) Atribuir à variável do passo 4.2 o valor da variável do passo 4.4.1;
                numeroDoGrafoAnterior = resultadoTransformacao

                # ,,,,,,,,,,valorDoScore = valorDoScore[valorDoScore.find("/")+1:]