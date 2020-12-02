from model.TrataBase import TrataBase
from model.ArquivosExternos import ArquivosExternos
from model.TrataBase import TrataBase

'''
tratamento = ClasseTratamentoDeDados()
jogosExperimentados = tratamento.getJogos()
scores = tratamento.scoresExperimentados

print("")
print("Jogos:", jogosExperimentados, "\n")
print("Scores:", scores)
print("\n", "-"*107, "\n")
'''

baseDeDados = ArquivosExternos()

arvore = baseDeDados.pega('InteligenteDados')

tratamento = TrataBase().iniciaTratamento()

#print("=>", tratamento[0])

listaDePartidas = tratamento[0]

listaDeScores = tratamento[1]


print(tratamento)



#print(st)
#print(st2)



'''
tratamento = TrataDados().percorreArvore(arvore)


#print(arvore)


#tratamento = TrataDados().ordenaNohs(tratamento)

#tratamento = ClasseTratamentoDeDados()

for i in range(len(tratamento)):
   print(i,")", tratamento[i]['estado'], tratamento[i]['jogadas'], " "*10, tratamento[i]['score'], "\n")



print(tratamento)

print(tratamento[2]['jogadas'], " ", tratamento[2]['score'], tratamento[2]['score'].count(float("inf")))

#print(ClasseTratamentoDeDados().jogosExperimentados)
'''









'''
for i in range(len(vetor)):
    print(vetor)
    print(i, ") ", vetor[i], sep="")

    if len(vetor[i][2]) == 0:
        print("-"*107)

    print("")
'''

# vetor[2][2] = vetor[2][2][1:]

# print(vetor[2][2])
