import networkx as nx
import matplotlib.pyplot as plt
from grafos.Arvore import hierarchy_pos
from grafos.ScrollWindow import ScrollableWindow
from controller.Preenchimento import Preenchimento

preenchimento = Preenchimento()

fig = plt.figure(1, figsize=(300, 6.5), dpi=100)
G = nx.Graph()
raiz = 0
G.add_edges_from([(raiz, 1), (raiz, 2), (raiz, 3), (raiz, 4), (raiz, 5), (raiz, 6), (raiz, 7), (raiz, 8), (raiz, 9)])

# Construção do Cérebro

camada = 8
produtoDasCamadas = 9
paiAtual = 1
filhoAtual = paiAtual + produtoDasCamadas
produtoDasCamadas = produtoDasCamadas * camada
proximaLinhagem = filhoAtual + produtoDasCamadas
duplasDeNosExperimentadas = preenchimento.duplasDeNosExperimentadas

while camada >= 1:
    for i in range(camada):
        if [paiAtual, filhoAtual] in duplasDeNosExperimentadas:
            G.add_edge(paiAtual, filhoAtual, color='lightgreen')
        else:
            G.add_edge(paiAtual, filhoAtual, color='lightgray')

        filhoAtual = filhoAtual + 1

    paiAtual = paiAtual + 1

    if filhoAtual == proximaLinhagem:
        camada = camada - 1
        produtoDasCamadas = produtoDasCamadas * camada
        proximaLinhagem = filhoAtual + produtoDasCamadas

cores = nx.get_edge_attributes(G, 'color').values()
print(filhoAtual - 1)  # Opcional...
pos = hierarchy_pos(G, raiz)
G.remove_node(raiz)
nx.draw(G, pos=pos, with_labels=False, node_size=2, edge_color=cores)

# Labels nos Nós (node)
labels = preenchimento.labelsParaNosExperimentados
nx.draw_networkx_labels(G, pos, labels, font_size=7, font_color="black", font_weight="bold")

'''
# Teste de Labels nas Arestas (edge)
labels = preenchimento.labelsParaArestasExperimentadas
nx.draw_networkx_edge_labels(G, pos, labels, font_size=8, font_color="red")
'''

ScrollableWindow(fig, pos, preenchimento.listaDeScores)


print("...")
