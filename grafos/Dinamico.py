import networkx as nx
import matplotlib.pyplot as plt
from grafos.Arvore import hierarchy_pos
from grafos.ScrollWindow import ScrollableWindow
from controller.Preenchimento import Preenchimento

fig = plt.figure(1, figsize=(15, 6.5))
G = nx.Graph()
raiz = 0

preenchimento = Preenchimento()

duplas = preenchimento.duplasDeNosExperimentadas

labels = preenchimento.labelsParaNosExperimentados

scores = preenchimento.listaDeScores

tamanho = len(duplas)

i = 0

while i < tamanho:
    if duplas[i][0] < 10:
        duplas.insert(i, [raiz, duplas[i][0]])
        tamanho = len(duplas)
        i = i + 1
    i = i + 1

labelsExistentes = {}

scoresExistentes = {}


def mostrarScoresDinamicamente():
    for numeroDoGrafo in scoresExistentes:
        plt.annotate(scoresExistentes[numeroDoGrafo], xy=pos[numeroDoGrafo], xytext=(-2, 6),
                     textcoords="offset points", color="red", fontweight="bold", fontsize=8)


# O LOOPING ABAIXO DESENHA DINAMICAMENTE TANTO OS NÓS QUANTO AS ARESTAS E OS SCORES...

for i in range(len(duplas)):
    plt.clf()
    G.add_edge(duplas[i][0], duplas[i][1])
    pos = hierarchy_pos(G, raiz)
    nx.draw(G, pos=pos, with_labels=False, node_size=5, edge_color="green")

    if duplas[i][0] in labels:
        labelsExistentes.__setitem__(duplas[i][0], labels[duplas[i][0]])
        scoresExistentes.__setitem__(duplas[i][0], scores[duplas[i][0]])

    if duplas[i][1] in labels:
        labelsExistentes.__setitem__(duplas[i][1], labels[duplas[i][1]])
        scoresExistentes.__setitem__(duplas[i][1], scores[duplas[i][1]])

    nx.draw_networkx_labels(G, pos, labelsExistentes, font_size=10, font_color="black", font_weight="bold")

    mostrarScoresDinamicamente()

    plt.pause(0.5)


print("...")
