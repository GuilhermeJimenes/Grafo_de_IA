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

tamanho = len(duplas)

i = 0

while i < tamanho:
    if duplas[i][0] < 10:
        duplas.insert(i, [raiz, duplas[i][0]])
        tamanho = len(duplas)
        i = i + 1
    i = i + 1


# CONSTRUCAO ESTÁTICA DO GRAFO
G.add_edges_from(duplas)

pos = hierarchy_pos(G, raiz)


nx.draw(G, pos=pos, with_labels=False, node_size=45, edge_color="darkblue")

nx.draw_networkx_labels(G, pos, labels, font_size=8, font_color="black", font_weight="bold")

# ScrollableWindow(fig, pos, preenchimento.listaDeScores)

plt.show()

print("...")
