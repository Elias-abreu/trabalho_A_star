import numpy as np

#Classe para criar as vértices (nós) do grafo
class Vertice:
    def __init__(self,rotulo, distancia_objetivo):
        self.rotulo = rotulo #Irá armazenar o nome das cidades
        self.distancia_objetivo = distancia_objetivo # Receberá a estimativa para chegada ao nó objetivo
        self.adjacentes = [] #Irá armazenar os nós/vértices adjacentes (ou seja, os nós que ligam ao atual
        self.visitado = False #Irá controlar se a vertice foi visitada ou não

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
        self.custo = custo # O custo do vértice até seu adjacente recebido por parâmetro
        self.distancia_a_star = vertice.distancia_objetivo + self.custo

#Classe utilizada para iniciar o grafo, criando as cidades e conectado-as
class Grafo:
    #Criar todas as cidades (vertices)
    #Colocar o nome da cidade e o custo estimado até a cidade objetivo
    #Ver outras heurísticas
    #A primeira heurística é o tempo estimado para chegada, coloquei em minutos
    # Os testes até então vão de Pimenta Bueno a Ouro Preto
    jipa = Vertice('Ji-paraná',0)
    medice = Vertice('Presidente Médici',36) # Nome da cidade e o f(h), heuristica, aqui a estimativa de tempo até o objetivo
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
    alto_alegre_do_parecis = Vertice('Alto Alegre dos Parecis',160)

    #Conectar as cidades adjacentes com o custo estimado (inicialmente a distância)

    #Adicionar os adjacentes de Ji-Paraná
    jipa.add_adjacentes(Adjacente(opo,40))
    jipa.add_adjacentes(Adjacente(teixeiropolis,53))
    jipa.add_adjacentes(Adjacente(alvorada,80))
    jipa.add_adjacentes(Adjacente(medice,36))
    jipa.add_adjacentes(Adjacente(ministro_andreazza,88))

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

    #Adicionar adjacentes de Alvorada do Oeste
    alvorada.add_adjacentes(Adjacente(jipa,80))
    alvorada.add_adjacentes(Adjacente(urupa,30))
    alvorada.add_adjacentes(Adjacente(sao_miguel,69))

    #Adicionar adjacentes de Alvorada do Oeste
    sao_miguel.add_adjacentes(Adjacente(alvorada,69))
    sao_miguel.add_adjacentes(Adjacente(nova_brasilandia,51))
    sao_miguel.add_adjacentes(Adjacente(seringueiras,41))

    #Adicionar adjacentes de seringueiras
    seringueiras.add_adjacentes(Adjacente(sao_miguel,41))
    seringueiras.add_adjacentes(Adjacente(sao_francisco,72))

    # Adicionar adjacentes são francisco
    sao_francisco.add_adjacentes(Adjacente(seringueiras,72))
    sao_francisco.add_adjacentes(Adjacente(costa_marques,110))

    # Adicionar adjacentes de costa marques
    costa_marques.add_adjacentes(Adjacente(sao_francisco,110))

    #Adicionar adjacentes de Nova Brasilândia
    nova_brasilandia.add_adjacentes(Adjacente(sao_miguel,51))
    nova_brasilandia.add_adjacentes(Adjacente(novo_horizonte,38))

    #Adicionar adjacentes de Novo Horizonte do Oeste
    novo_horizonte.add_adjacentes(Adjacente(nova_brasilandia,38))
    novo_horizonte.add_adjacentes(Adjacente(rolim_de_moura,26))

    medice.add_adjacentes(Adjacente(jipa,36))
    medice.add_adjacentes(Adjacente(ministro_andreazza,90))
    medice.add_adjacentes(Adjacente(castanheiras,41))
    medice.add_adjacentes(Adjacente(cacoal,70))
    medice.add_adjacentes(Adjacente(rolim_de_moura,73))

    ministro_andreazza.add_adjacentes(Adjacente(jipa,88))
    ministro_andreazza.add_adjacentes(Adjacente(medice,90))
    ministro_andreazza.add_adjacentes(Adjacente(cacoal,34))
    ministro_andreazza.add_adjacentes(Adjacente(espigao_d_oeste,83))

    cacoal.add_adjacentes(Adjacente(ministro_andreazza,34))
    cacoal.add_adjacentes(Adjacente(medice,70))
    cacoal.add_adjacentes(Adjacente(espigao_d_oeste,62))
    cacoal.add_adjacentes(Adjacente(parecis,95))
    cacoal.add_adjacentes(Adjacente(rolim_de_moura,63))
    cacoal.add_adjacentes(Adjacente(pimenta_boeno,43))

    parecis.add_adjacentes(Adjacente(cacoal,95))

    espigao_d_oeste.add_adjacentes(Adjacente(ministro_andreazza,83))
    espigao_d_oeste.add_adjacentes(Adjacente(cacoal,62))
    espigao_d_oeste.add_adjacentes(Adjacente(pimenta_boeno,33))

    #Adicionar adjacentes de Pimenta Bueno, faltou vilhena e Chupiguaia, pois até então não pretendemos usar
    pimenta_boeno.add_adjacentes(Adjacente(cacoal,43))
    pimenta_boeno.add_adjacentes(Adjacente(espigao_d_oeste,33))
    pimenta_boeno.add_adjacentes(Adjacente(primavera_de_rondonia,28))
    pimenta_boeno.add_adjacentes(Adjacente(rolim_de_moura,66))

    rolim_de_moura.add_adjacentes(Adjacente(pimenta_boeno,66))
    rolim_de_moura.add_adjacentes(Adjacente(cacoal,63))
    rolim_de_moura.add_adjacentes(Adjacente(novo_horizonte,26))
    rolim_de_moura.add_adjacentes(Adjacente(santa_luzia,20))
    rolim_de_moura.add_adjacentes(Adjacente(medice,73))

    primavera_de_rondonia.add_adjacentes(Adjacente(pimenta_boeno,28))
    primavera_de_rondonia.add_adjacentes(Adjacente(sao_felipe,30))

    sao_felipe.add_adjacentes(Adjacente(primavera_de_rondonia,30))
    sao_felipe.add_adjacentes(Adjacente(santa_luzia,29))

    santa_luzia.add_adjacentes(Adjacente(sao_felipe,29))
    santa_luzia.add_adjacentes(Adjacente(rolim_de_moura,20))
    santa_luzia.add_adjacentes(Adjacente(alta_floresta,25))
    santa_luzia.add_adjacentes(Adjacente(alto_alegre_do_parecis,33))

    alto_alegre_do_parecis.add_adjacentes(Adjacente(santa_luzia,33))

    alta_floresta.add_adjacentes(Adjacente(santa_luzia,25))

#método responsável por ordenar os adjacentes
class VetorOrdenado:

    def __init__(self, capacidade):
        self.capacidade = capacidade
        self.ultima_posicao = -1
        # Mudança no tipo de dados
        self.valores = np.empty(self.capacidade, dtype=object)

    # Referência para o vértice e comparação com a distância A*
    def insere(self, adjacente):
        if self.ultima_posicao == self.capacidade - 1:
            print('Capacidade máxima atingida')
            return
        posicao = 0
        for i in range(self.ultima_posicao + 1):
            posicao = i
            if self.valores[i].distancia_aestrela > adjacente.distancia_aestrela:
                break
            if i == self.ultima_posicao:
                posicao = i + 1
        x = self.ultima_posicao
        while x >= posicao:
            self.valores[x + 1] = self.valores[x]
            x -= 1
        self.valores[posicao] = adjacente
        self.ultima_posicao += 1

    def imprime(self):
        if self.ultima_posicao == -1:
            print('O vetor está vazio')
        else:
            for i in range(self.ultima_posicao + 1):
                print(i, ' - ', self.valores[i].vertice.rotulo, ' - ',
                      self.valores[i].custo, ' - ',
                      self.valores[i].vertice.distancia_objetivo, ' - ',
                      self.valores[i].distancia_aestrela)

class Vetor_Ordenado:

    def __init__(self,lista):
        self.lista = lista

    def ordenar_menor(self):
        self.lista = sorted(self.lista, key=lambda a_star: a_star.distancia_a_star, reverse=False)

    def imprimir_adjacentes_ordenados(self):
        for i in self.lista:
            print(i.vertice.rotulo, " Tempo estimado até Jipa (Minutos): ", i.vertice.distancia_objetivo,
                  "  Distância (KM): ", i.custo, "  Calculo A*: ", i.distancia_a_star)

class A_Star:
    def __init__(self,objetivo):
        #Parãmentro objetivo receberá a cidade que se deseha chegar
        self.objetivo = objetivo
        self.escontrado = False #Apenas para controlar se chegou ao objetivo ou não

    def buscar(self,atual):
        print("----------------")
        print("Atual: {}".format(atual.rotulo))
        #Compara se o atual é objetivo, se sim marca como encontrado
        if(atual == self.objetivo):
            self.escontrado = True
            print("Chegou")
        else:
            ordenaxao = Vetor_Ordenado(atual.adjacentes)
            ordenaxao.ordenar_menor()
            for adj in ordenaxao.lista:
                if(adj.vertice.visitado == False):
                    adj.vertice.visitado == True
            ordenaxao.imprimir_adjacentes_ordenados()
            self.buscar(ordenaxao.lista[0].vertice)




grafo = Grafo()
#print(grafo.jipa.adjacentes[0].vertice.rotulo," Tempo estimado até Jipa (Minutos): ",grafo.jipa.adjacentes[0].vertice.distancia_objetivo,"  Distância (KM): ",grafo.jipa.adjacentes[0].custo, "  Distância A*: ",grafo.jipa.adjacentes[0].distancia_a_star)

#lista = grafo.cacoal.adjacentes
#o = Vetor_Ordenado(lista)
#o.ordenar_menor()
#o.imprimir_adjacentes_ordenados()

busca = A_Star(grafo.jipa)
busca.buscar(grafo.sao_miguel)