import networkx as nx
import matplotlib.pyplot as plt
from grafos.Arvore import hierarchy_pos
from grafos.ScrollWindow import ScrollableWindow
from controller.Preenchimento import Preenchimento

fig = plt.figure(1, figsize=(100, 6.5))  #(15, 6.5)
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


nx.draw(G, pos=pos, with_labels=False, node_size=5, edge_color="green") #node_size = 230

nx.draw_networkx_labels(G, pos, labels, font_size=9, font_color="black", font_weight="bold")  # fontsize = 10

'''
# Teste de Labels nas Arestas (edge)
labels = preenchimento.labelsParaArestasExperimentadas
print(preenchimento.labelsParaArestasExperimentadas)
print(duplas)
nx.draw_networkx_edge_labels(G, pos, labels, font_size=8, font_color="red")
'''


ScrollableWindow(fig, pos, preenchimento.listaDeScores)

'''
preenchimento.mostrarScores(plt, pos)

plt.xlim([-0.005, 1.015])

plt.show()
'''

print("...")
