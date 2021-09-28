
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
    alvorada = Vertice('Alvorada D. Oeste')
    ministro_andreazza = Vertice('Ministro Andreazza')
    castanheiras = Vertice('Castanheiras')
    cacoal = Vertice('Cacoal')
    rolim_de_moura = Vertice('Rolim de Moura')
    espigao_d_oeste = Vertice('Espigão D. Oeste')
    parecis = Vertice('Parecis')
    pimenta_boeno = Vertice('Pimenta Boeno')
    urupa = Vertice('Urupá')
    novo_horizonte = Vertice('Novo Horizonte do Oeste')
    nova_brasilandia = Vertice('Nova Brasilândia D. Oeste')
    sao_miguel = Vertice('São Miguel do Guaporé')
    seringueiras = Vertice('Seringueiras')
    sao_francisco = Vertice('São Francisco do Guaporé')
    costa_marques = Vertice('Costa Marques')
    santa_luzia = Vertice('Santa Luzia D. Oeste')
    primavera_de_rondonia = Vertice('Primavera de Rondônia')
    sao_felipe = Vertice('São Felipe D. Oeste')
    alta_floresta = Vertice('Alta Floresta D. Oeste')
