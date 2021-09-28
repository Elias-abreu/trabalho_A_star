
#Classe para criar as vértices (nós) do grafo
class Vertice:
    def __init__(self,rotulo):
        self.rotulo = rotulo #Irá armazenar o nome das cidades
        self.adjacentes = [] #Irá armazenar os nós/vértices adjacentes (ou seja, os nós que ligam ao atual

    #Utilizado para adicionar adjacente
    def add_adjacentes(self,adjacente):
        self.adjacentes.append(adjacente)

    #Utilizado para mostrar todos os adjacentes de um nó
    def show_adjacentes(self):
        for i in self.adjacentes:
            print(i.vertice.rotulo,i.custo)

#Classe utilizada para criar as cidades que ligam
class Adjacente:
    def __init__(self,vertice,custo):
        self.vertice = vertice
        self.custo = custo

#Classe utilizada para iniciar o grafo, criando as cidades e conectado-as
class grafo:
    #Criar todas as cidades (vertices)
    jipa = Vertice('Ji-paraná')
    medice = Vertice('Presidente Médici')
    opo = Vertice('Ouro Preto do Oeste')
    teixeiropolis = Vertice('Teixeirópolis')
    alvorada = Vertice('Alvorada D Oeste')
    ministro_andreazza = Vertice('Ministro Andreazza')
