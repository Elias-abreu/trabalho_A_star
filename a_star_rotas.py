
#Classe para criar as vértices (nós) do grafo
class Vertice:
    def __init__(self,rotulo, distancia_objetivo):
        self.rotulo = rotulo #Irá armazenar o nome das cidades
        self.distancia_objetivo = distancia_objetivo # Receberá a estimativa para chegada ao nó objetivo
        self.adjacentes = [] #Irá armazenar os nós/vértices adjacentes (ou seja, os nós que ligam ao atual

    #Utilizado para adicionar adjacente
    def add_adjacentes(self,adjacente):
        self.adjacentes.append(adjacente)

    #Utilizado para mostrar todos os adjacentes de um nó
    def show_adjacentes(self):
        for i in self.adjacentes:
            print(i.vertice.rotulo,i.custo)

#Classe utilizada para criar as cidades que ligam
#Recebe uma vertice adjacente e um custo
class Adjacente:
    def __init__(self,vertice,custo):
        self.vertice = vertice
        self.custo = custo

#Classe utilizada para iniciar o grafo, criando as cidades e conectado-as
class Grafo:
    #Criar todas as cidades (vertices)
    #Colocar o nome da cidade e o custo estimado até a cidade objetivo
    #Ver outras heurísticas
    #A primeira heurística é o tempo estimado para chegada, coloquei em minutos
    #Os testes até então vão de Pimenta Bueno a Ouro Preto
    jipa = Vertice('Ji-paraná',0)
    medice = Vertice('Presidente Médici',36)
    opo = Vertice('Ouro Preto do Oeste',45)
    teixeiropolis = Vertice('Teixeirópolis',55)
    alvorada = Vertice('Alvorada D. Oeste',150)
    ministro_andreazza = Vertice('Ministro Andreazza',120)
    castanheiras = Vertice('Castanheiras',95)
    cacoal = Vertice('Cacoal',110)
    rolim_de_moura = Vertice('Rolim de Moura',120)
    espigao_d_oeste = Vertice('Espigão D. Oeste',195)
    parecis = Vertice('Parecis',200)
    pimenta_boeno = Vertice('Pimenta Bueno',160)
    urupa = Vertice('Urupá',80)
    novo_horizonte = Vertice('Novo Horizonte do Oeste',130)
    nova_brasilandia = Vertice('Nova Brasilândia D. Oeste',145)
    sao_miguel = Vertice('São Miguel do Guaporé',160)
    seringueiras = Vertice('Seringueiras',185)
    sao_francisco = Vertice('São Francisco do Guaporé',240)
    costa_marques = Vertice('Costa Marques',330)
    santa_luzia = Vertice('Santa Luzia D. Oeste',140)
    primavera_de_rondonia = Vertice('Primavera de Rondônia',175)
    sao_felipe = Vertice('São Felipe D. Oeste',180)
    alta_floresta = Vertice('Alta Floresta D. Oeste',170)
    vale_do_paraiso = Vertice('Vale do Paraíso',80)
    #jaru = Vertice('Jaru',95) #retirei Jaru para ficar marcado no grafo
    nova_uniao = Vertice('Nova União',90)
    mirante_da_serra = Vertice('Mirante da Serra',110)

    #Conectar as cidades adjacentes com o custo estimado (inicialmente a distância)

    #Adicionar os adjacentes de Ji-Paraná
    jipa.add_adjacentes(Adjacente(opo,40))
    jipa.add_adjacentes(Adjacente(teixeiropolis,53))
    jipa.add_adjacentes(Adjacente(alvorada,80))
    jipa.add_adjacentes(Adjacente(medice,36))

    #adicionar os adjacentes de Ouro Preto
    opo.add_adjacentes(Adjacente(jipa,40))
    opo.add_adjacentes(Adjacente(vale_do_paraiso,37))
    #opo.add_adjacentes(Adjacente(jaru,43))
    opo.add_adjacentes(Adjacente(nova_uniao,46))

    #Adicionar adjacentes do vale do paraíso
    vale_do_paraiso.add_adjacentes(Adjacente(opo,37))

    #Adicionar adjacentes de Nova União
    nova_uniao.add_adjacentes(Adjacente(opo,46))
    nova_uniao.add_adjacentes(Adjacente(mirante_da_serra,18))

    #Adicionar adjaventes de Mirante da Serra
    mirante_da_serra.add_adjacentes(Adjacente(nova_uniao,18))
    mirante_da_serra.add_adjacentes(Adjacente(urupa,47))

    #Adicionar adjaventes de Urupá
    urupa.add_adjacentes(Adjacente(mirante_da_serra,47))
    urupa.add_adjacentes(Adjacente(teixeiropolis,31))
    urupa.add_adjacentes(Adjacente(alvorada,30))

    #Adicionar adjacentes de Teixeiropolis
    teixeiropolis.add_adjacentes(Adjacente(jipa,52))
    teixeiropolis.add_adjacentes((Adjacente(urupa,31)))

grafo = Grafo()
grafo.jipa.show_adjacentes()