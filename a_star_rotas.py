import networkx as nx
import numpy as np
import matplotlib.pyplot as plt

todos_adjacentes = []

#Classe para criar as vértices (nós) do grafo
class Vertice:
    #Rotulo recebe o nome do nó, distancia_objetivo é o valor estimado até o objetivo
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
    medice = Vertice('Presidente Médici',40) # Nome da cidade e o f(h), heuristica, aqui a estimativa de tempo até o objetivo
    opo = Vertice('Ouro Preto do Oeste',45)
    teixeiropolis = Vertice('Teixeirópolis',55)
    alvorada = Vertice('Alvorada D. Oeste',90)
    ministro_andreazza = Vertice('Ministro Andreazza',120)
    castanheiras = Vertice('Castanheiras',100)
    cacoal = Vertice('Cacoal',115)
    rolim_de_moura = Vertice('Rolim de Moura',115)
    espigao_d_oeste = Vertice('Espigão D. Oeste',185)
    pimenta_boeno = Vertice('Pimenta Bueno',165)
    urupa = Vertice('Urupá',85)
    novo_horizonte = Vertice('Novo Horizonte do Oeste',130)
    nova_brasilandia = Vertice('Nova Brasilândia D. Oeste',150)
    sao_miguel = Vertice('São Miguel do Guaporé',160)
    seringueiras = Vertice('Seringueiras',190)
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
    alto_alegre_do_parecis = Vertice('Alto Alegre dos Parecis',180)
    jaru = Vertice('Jaru',90)
    ariquemes = Vertice('Ariquemes',170)

    gov_jorge_teixeira = Vertice('Governador Jorge Teixeira', 120)
    cacaulandia = Vertice('Cacaulândia', 150)
    theobrama = Vertice('Theobrama', 110)
    vale_do_anari = Vertice('Vale do Anari', 161)
    machadinho_d_oeste = Vertice('Machadinho D`Oeste', 216)
    cujubim = Vertice('Cujubim', 250)  ### duas rotas
    rio_crespo = Vertice('Rio Crespo', 194)
    alto_paraiso = Vertice('Alto Paraíso', 210)
    monte_negro = Vertice('Monte Negro', 212)
    campo_novo_de_rondonia = Vertice('Campo Novo de Rondônia', 265)
    buritis = Vertice('Buritis', 288)
    itapua_do_oeste = Vertice('Itapuã do Oeste', 229)
    candeias_do_jamari = Vertice('Candeias do Jamari', 296)
    porto_velho = Vertice('Porto Velho', 324)
    nova_mamore = Vertice('Nova Mamoré', 495)  ###duas rotas
    guajara_mirim = Vertice('Guajará-Mirim', 536)  ###duas rotas

    vilhena = Vertice('Vilhena', 285)
    chupinguaia = Vertice('Chupinguaia', 268)  ###duas rotas
    colorado_do_oeste = Vertice('Colorado do Oeste', 338)
    cabixi = Vertice('Cabixi', 378)
    cerejeiras = Vertice('Cerejeiras', 374)
    corumbiara = Vertice('Corumbiara', 366)  ###duas rotas
    pimenteiras_do_oeste = Vertice('Pimenteiras do Oeste', 418)

    #Conectar as cidades adjacentes com o custo estimado (inicialmente a distância)

    #Adicionar os adjacentes de Ji-Paraná
    jipa.add_adjacentes(Adjacente(opo,40))
    jipa.add_adjacentes(Adjacente(teixeiropolis,53))
    jipa.add_adjacentes(Adjacente(alvorada,79))
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
    teixeiropolis.add_adjacentes(Adjacente(jipa,53))
    teixeiropolis.add_adjacentes((Adjacente(urupa,31)))

    #Adicionar adjacentes de Alvorada do Oeste
    alvorada.add_adjacentes(Adjacente(jipa,79))
    alvorada.add_adjacentes(Adjacente(urupa,30))
    alvorada.add_adjacentes(Adjacente(sao_miguel,68))
    alvorada.add_adjacentes(Adjacente(castanheiras, 66))

    #Adicionar adjacentes de Alvorada do Oeste
    sao_miguel.add_adjacentes(Adjacente(alvorada,68))
    sao_miguel.add_adjacentes(Adjacente(nova_brasilandia,51))
    sao_miguel.add_adjacentes(Adjacente(seringueiras,41))

    #Adicionar adjacentes de seringueiras
    seringueiras.add_adjacentes(Adjacente(sao_miguel,41))
    seringueiras.add_adjacentes(Adjacente(sao_francisco,73))

    # Adicionar adjacentes são francisco
    sao_francisco.add_adjacentes(Adjacente(seringueiras,73))
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
    cacoal.add_adjacentes(Adjacente(espigao_d_oeste,57))
    cacoal.add_adjacentes(Adjacente(rolim_de_moura,63))
    cacoal.add_adjacentes(Adjacente(pimenta_boeno,43))


    espigao_d_oeste.add_adjacentes(Adjacente(ministro_andreazza,83))
    espigao_d_oeste.add_adjacentes(Adjacente(cacoal,62))
    espigao_d_oeste.add_adjacentes(Adjacente(pimenta_boeno,33))

    #Adicionar adjacentes de Pimenta Bueno, faltou vilhena e Chupiguaia, pois até então não pretendemos usar
    pimenta_boeno.add_adjacentes(Adjacente(cacoal,43))
    pimenta_boeno.add_adjacentes(Adjacente(espigao_d_oeste,33))
    pimenta_boeno.add_adjacentes(Adjacente(primavera_de_rondonia,28))
    pimenta_boeno.add_adjacentes(Adjacente(rolim_de_moura,66))
    pimenta_boeno.add_adjacentes(Adjacente(vilhena, 186))  ###linha adicionada para Vilhena e Chupiguaia
    pimenta_boeno.add_adjacentes(Adjacente(chupinguaia, 151))

    rolim_de_moura.add_adjacentes(Adjacente(pimenta_boeno,66))
    rolim_de_moura.add_adjacentes(Adjacente(cacoal,63))
    rolim_de_moura.add_adjacentes(Adjacente(novo_horizonte,26))
    rolim_de_moura.add_adjacentes(Adjacente(santa_luzia,20))
    rolim_de_moura.add_adjacentes(Adjacente(medice,73))
    rolim_de_moura.add_adjacentes(Adjacente(castanheiras,56))

    castanheiras.add_adjacentes(Adjacente(rolim_de_moura,56))
    castanheiras.add_adjacentes(Adjacente(medice,41))
    castanheiras.add_adjacentes(Adjacente(alvorada,66))

    primavera_de_rondonia.add_adjacentes(Adjacente(pimenta_boeno,28))
    primavera_de_rondonia.add_adjacentes(Adjacente(sao_felipe,30))

    sao_felipe.add_adjacentes(Adjacente(primavera_de_rondonia,28))
    sao_felipe.add_adjacentes(Adjacente(santa_luzia,29))

    santa_luzia.add_adjacentes(Adjacente(sao_felipe,29))
    santa_luzia.add_adjacentes(Adjacente(rolim_de_moura,20))
    santa_luzia.add_adjacentes(Adjacente(alta_floresta,25))
    santa_luzia.add_adjacentes(Adjacente(alto_alegre_do_parecis,33))

    alto_alegre_do_parecis.add_adjacentes(Adjacente(santa_luzia,33))

    alta_floresta.add_adjacentes(Adjacente(santa_luzia,25))

    #Adjacentes de Jaru
    jaru.add_adjacentes(Adjacente(opo,40))
    jaru.add_adjacentes(Adjacente(ariquemes, 80))

    ariquemes.add_adjacentes(Adjacente(jaru,80))

    gov_jorge_teixeira.add_adjacentes(Adjacente(jaru, 42))

    # Adicionar os adjacentes de Cacaulândia (cidades - Jaru)
    cacaulandia.add_adjacentes(Adjacente(jaru, 83))

    # Adicionar os adjacentes de Theobrama (cidades - Jaru, Vale do Anari)
    theobrama.add_adjacentes(Adjacente(jaru, 33))
    theobrama.add_adjacentes(Adjacente(vale_do_anari, 55))

    # Adicionar os adjacentes de Vale do Anari (cidades - Theobrama, Machadinho D`Oeste)
    vale_do_anari.add_adjacentes(Adjacente(theobrama, 55))
    vale_do_anari.add_adjacentes(Adjacente(machadinho_d_oeste, 63))

    # Adicionar os adjacentes de Machadinho D`Oeste (cidades - Vale do Anari, Cujubim)
    machadinho_d_oeste.add_adjacentes(Adjacente(vale_do_anari, 63))
    machadinho_d_oeste.add_adjacentes(Adjacente(cujubim, 80))
    machadinho_d_oeste.add_adjacentes(Adjacente(ariquemes, 149))


    # Adicionar os adjacentes de Cujubim (cidades - Machadinho D`Oeste, Rio Crespo)
    cujubim.add_adjacentes(Adjacente (machadinho_d_oeste, 80))
    cujubim.add_adjacentes(Adjacente (rio_crespo, 74))

    # Adicionar os adjacentes de Rio Crespo (cidades - Cujubim, Ariquemes)
    rio_crespo.add_adjacentes(Adjacente(cujubim, 74))
    rio_crespo.add_adjacentes(Adjacente(ariquemes, 52))

    # Adicionar os adjacentes de  Ariquemes (cidades - Jaru, Machadinho D`Oeste, Rio Crespo, Itapuã do Oeste, Alto Paraíso,Monte Negro)
    ariquemes.add_adjacentes(Adjacente(jaru, 96))
    ariquemes.add_adjacentes(Adjacente(machadinho_d_oeste, 149))
    #** * Olhar estarota ** *
    ariquemes.add_adjacentes(Adjacente(rio_crespo, 52))
    ariquemes.add_adjacentes(Adjacente(itapua_do_oeste, 92))
    ariquemes.add_adjacentes(Adjacente(alto_paraiso, 59))
    ariquemes.add_adjacentes(Adjacente(monte_negro, 54))

    # Adicionar os adjacentes de Alto Paraíso (cidade - Ariquemes)
    alto_paraiso.add_adjacentes(Adjacente(ariquemes, 59))

    # Adicionar os adjacentes de  Itapuã D`Oeste (cidades - Ariquemes, Candeias do Jamari)
    itapua_do_oeste.add_adjacentes(Adjacente(ariquemes, 92))
    itapua_do_oeste.add_adjacentes(Adjacente(candeias_do_jamari, 89))

    # Adicionar os adjacentes de Candeias do Jamari (cidades - Itapuã D`Oeste, Porto Velho)
    candeias_do_jamari.add_adjacentes(Adjacente(itapua_do_oeste, 89))
    candeias_do_jamari.add_adjacentes(Adjacente(porto_velho, 24))

    # Adicionar os adjacentes de Porto Velho (cidades - Candeias do Jamari, Nova Marmoré)
    porto_velho.add_adjacentes(Adjacente(candeias_do_jamari, 24))
    porto_velho.add_adjacentes(Adjacente(nova_mamore, 281))

    # Adicionar os adjacentes de  Nova Marmoré(cidades - Porto Velho,Buritis e Guajará-Mirim)
    nova_mamore.add_adjacentes(Adjacente(porto_velho, 281))
    nova_mamore.add_adjacentes(Adjacente(guajara_mirim, 48))
    nova_mamore.add_adjacentes(Adjacente(buritis, 178))

    # Adicionar os adjacentes de Guajará-Mirim (cidade - Nova Mamoré)
    guajara_mirim.add_adjacentes(Adjacente(nova_mamore, 48))

    # Adicionar os adjacentes de Buritis (cidades - Nova Mamoré, Campo Novo de Rondônia, Monte Negro)
    buritis.add_adjacentes(Adjacente(nova_mamore, 178))
    buritis.add_adjacentes(Adjacente(campo_novo_de_rondonia, 58))  ## duas rotas
    buritis.add_adjacentes(Adjacente(monte_negro, 75))

    # Adicionar os adjacentes de Campo Novo de Rondônia (cidades - Buritis, Monte Negro)
    campo_novo_de_rondonia.add_adjacentes(Adjacente(buritis, 58))
    campo_novo_de_rondonia.add_adjacentes(Adjacente(monte_negro, 75))

    # Adicionar os adjacentes de Monte Negro (cidades Buritis, Ariquemes, Campo Novo de Rondônia)
    monte_negro.add_adjacentes(Adjacente(buritis, 75))
    monte_negro.add_adjacentes(Adjacente(ariquemes, 54))
    monte_negro.add_adjacentes(Adjacente(campo_novo_de_rondonia, 75))

    # Adicionar os adjacentes de Vilhena (cidades Pimenta Bueno,Chupinguaia, Colorado D`Oeste)
    vilhena.add_adjacentes(Adjacente(pimenta_boeno, 186))
    vilhena.add_adjacentes(Adjacente(chupinguaia, 157))
    vilhena.add_adjacentes(Adjacente(colorado_do_oeste, 86))

    # Adicionar os adjacentes de Chupinguaia (cidades - Pimenta Bueno, Vilhena, Colorado D`Oeste)
    chupinguaia.add_adjacentes(Adjacente(pimenta_boeno, 151))
    chupinguaia.add_adjacentes(Adjacente(vilhena, 157))
    chupinguaia.add_adjacentes(Adjacente(colorado_do_oeste, 110))

    # Adicionar os adjacentes de Colorado D`Oeste (cidades - Vilhena, Chupinguaia, Cabixi, Cerejeiras)
    colorado_do_oeste.add_adjacentes(Adjacente(vilhena, 86))
    colorado_do_oeste.add_adjacentes(Adjacente(chupinguaia, 110))
    colorado_do_oeste.add_adjacentes(Adjacente(cabixi, 46))
    colorado_do_oeste.add_adjacentes(Adjacente(cerejeiras, 39))

    # Adicionar os adjacentes de Cabixi (cidade - Colorado D`Oeste)
    cabixi.add_adjacentes(Adjacente(colorado_do_oeste, 46))

    # Adicionar os adjacentes de Cerejeiras (cidades - Colorado D`Oeste, Corumbiara e Pimenta D`Oeste)
    cerejeiras.add_adjacentes(Adjacente(colorado_do_oeste, 39))
    cerejeiras.add_adjacentes(Adjacente(corumbiara, 38))
    cerejeiras.add_adjacentes(Adjacente(pimenteiras_do_oeste, 53))

    # Adicionar os adjacentes de Corumbiara (cidade - Cerejeiras)
    corumbiara.add_adjacentes(Adjacente(cerejeiras, 38))

    # Adicionar os adjacentes de Pimenteiras D`Oesteeste (cidade - Cerejeiras)
    pimenteiras_do_oeste.add_adjacentes(Adjacente(cerejeiras, 53))

class Grafo_linha_reta:
    lista_cidades = []
    #Criar todas as cidades (vertices)
    #Colocar o nome da cidade e o custo estimado até a cidade objetivo
    #Ver outras heurísticas
    #A primeira heurística é o tempo estimado para chegada, coloquei em minutos
    # Os testes até então vão de Pimenta Bueno a Ouro Preto
    jipa = Vertice('Ji-paraná',0)
    medice = Vertice('Presidente Médici',33.6) # Nome da cidade e o f(h), heuristica, aqui a estimativa de tempo até o objetivo
    opo = Vertice('Ouro Preto do Oeste',36.6)
    teixeiropolis = Vertice('Teixeirópolis',32.99)
    alvorada = Vertice('Alvorada D. Oeste',63.94)
    ministro_andreazza = Vertice('Ministro Andreazza',60.3)
    castanheiras = Vertice('Castanheiras',61.69)
    cacoal = Vertice('Cacoal',83.18)
    rolim_de_moura = Vertice('Rolim de Moura',96.84)
    espigao_d_oeste = Vertice('Espigão D. Oeste',126.20)
    pimenta_boeno = Vertice('Pimenta Bueno',123.46)
    urupa = Vertice('Urupá',52.25)
    novo_horizonte = Vertice('Novo Horizonte do Oeste',92.79)
    nova_brasilandia = Vertice('Nova Brasilândia D. Oeste',102.17)
    sao_miguel = Vertice('São Miguel do Guaporé',122.83)
    seringueiras = Vertice('Seringueiras',153.53)
    sao_francisco = Vertice('São Francisco do Guaporé',219.53)
    costa_marques = Vertice('Costa Marques',302.20)
    santa_luzia = Vertice('Santa Luzia D. Oeste',116.62)
    primavera_de_rondonia = Vertice('Primavera de Rondônia',127.35)
    sao_felipe = Vertice('São Felipe D. Oeste',124.85)
    alta_floresta = Vertice('Alta Floresta D. Oeste',117.57)
    vale_do_paraiso = Vertice('Vale do Paraíso',52.97)
    nova_uniao = Vertice('Nova União',65.48)
    mirante_da_serra = Vertice('Mirante da Serra',80.07)
    alto_alegre_do_parecis = Vertice('Alto Alegre dos Parecis',87.40)
    jaru = Vertice('Jaru', 74.88)
    ariquemes = Vertice('Ariquemes',159.18)

    lista_cidades.append(jipa)
    lista_cidades.append(opo)
    lista_cidades.append(medice)
    lista_cidades.append(teixeiropolis)
    lista_cidades.append(alvorada)
    lista_cidades.append(ministro_andreazza)
    lista_cidades.append(vale_do_paraiso)
    lista_cidades.append(nova_uniao)
    lista_cidades.append(ministro_andreazza)
    lista_cidades.append(castanheiras)
    lista_cidades.append(cacoal)
    lista_cidades.append(rolim_de_moura)
    lista_cidades.append(espigao_d_oeste)
    lista_cidades.append(pimenta_boeno)
    lista_cidades.append(urupa)
    lista_cidades.append(santa_luzia)
    lista_cidades.append(primavera_de_rondonia)
    lista_cidades.append(sao_felipe)
    lista_cidades.append(alta_floresta)
    lista_cidades.append(vale_do_paraiso)
    lista_cidades.append(alto_alegre_do_parecis)
    lista_cidades.append(jaru)
    lista_cidades.append(ariquemes)
    lista_cidades.append(novo_horizonte)
    lista_cidades.append(nova_brasilandia)
    lista_cidades.append(sao_miguel)
    lista_cidades.append(sao_francisco)
    lista_cidades.append(seringueiras)


    #Conectar as cidades adjacentes com o custo estimado (inicialmente a distância)

    #Adicionar os adjacentes de Ji-Paraná
    jipa.add_adjacentes(Adjacente(opo,40))
    jipa.add_adjacentes(Adjacente(teixeiropolis,53))
    jipa.add_adjacentes(Adjacente(alvorada,79))
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
    teixeiropolis.add_adjacentes(Adjacente(jipa,53))
    teixeiropolis.add_adjacentes((Adjacente(urupa,31)))

    #Adicionar adjacentes de Alvorada do Oeste
    alvorada.add_adjacentes(Adjacente(jipa,79))
    alvorada.add_adjacentes(Adjacente(urupa,30))
    alvorada.add_adjacentes(Adjacente(sao_miguel,68))
    alvorada.add_adjacentes(Adjacente(castanheiras, 66))

    #Adicionar adjacentes de Alvorada do Oeste
    sao_miguel.add_adjacentes(Adjacente(alvorada,68))
    sao_miguel.add_adjacentes(Adjacente(nova_brasilandia,51))
    sao_miguel.add_adjacentes(Adjacente(seringueiras,41))

    #Adicionar adjacentes de seringueiras
    seringueiras.add_adjacentes(Adjacente(sao_miguel,41))
    seringueiras.add_adjacentes(Adjacente(sao_francisco,73))

    # Adicionar adjacentes são francisco
    sao_francisco.add_adjacentes(Adjacente(seringueiras,73))
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
    cacoal.add_adjacentes(Adjacente(espigao_d_oeste,57))
    cacoal.add_adjacentes(Adjacente(rolim_de_moura,63))
    cacoal.add_adjacentes(Adjacente(pimenta_boeno,43))


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
    rolim_de_moura.add_adjacentes(Adjacente(castanheiras,56))

    castanheiras.add_adjacentes(Adjacente(rolim_de_moura,56))
    castanheiras.add_adjacentes(Adjacente(medice,41))
    castanheiras.add_adjacentes(Adjacente(alvorada,66))

    primavera_de_rondonia.add_adjacentes(Adjacente(pimenta_boeno,28))
    primavera_de_rondonia.add_adjacentes(Adjacente(sao_felipe,30))

    sao_felipe.add_adjacentes(Adjacente(primavera_de_rondonia,28))
    sao_felipe.add_adjacentes(Adjacente(santa_luzia,29))

    santa_luzia.add_adjacentes(Adjacente(sao_felipe,29))
    santa_luzia.add_adjacentes(Adjacente(rolim_de_moura,20))
    santa_luzia.add_adjacentes(Adjacente(alta_floresta,25))
    santa_luzia.add_adjacentes(Adjacente(alto_alegre_do_parecis,33))

    alto_alegre_do_parecis.add_adjacentes(Adjacente(santa_luzia,33))

    alta_floresta.add_adjacentes(Adjacente(santa_luzia,25))

    #Adjacentes de Jaru
    jaru.add_adjacentes(Adjacente(opo,40))
    jaru.add_adjacentes(Adjacente(ariquemes, 80))

    ariquemes.add_adjacentes(Adjacente(jaru,80))



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
        global todos_adjacentes
        print("----------------")
        print("Atual: {},  Distância Objetivo: {}".format(atual.rotulo, atual.distancia_objetivo))
        #Compara se o atual é objetivo, se sim marca como encontrado
        if(atual == self.objetivo):
            #todos_adjacentes.append(atual)
            self.escontrado = True
            print("--- Chegou ao destino ---")
        else:
            ordenaxao = Vetor_Ordenado(atual.adjacentes)
            ordenaxao.ordenar_menor()
            todos_adjacentes.append(atual)
            for adj in ordenaxao.lista:
                if(adj.vertice.visitado == False):
                    adj.vertice.visitado == True
            ordenaxao.imprimir_adjacentes_ordenados()
            self.buscar(ordenaxao.lista[0].vertice)


class Desenhar_grafico:

    def gerar_grafo(self):
        global todos_adjacentes
        g = nx.Graph()
        g1 = nx.Graph()
        e = []
        red_edges = []
        for i in todos_adjacentes:
            o = Vetor_Ordenado(i.adjacentes)
            k = [i.rotulo, o.lista[0].vertice.rotulo,o.lista[0].custo]
            red_edges.append(k)
            for j in o.lista:
                kkk = [i.rotulo, j.vertice.rotulo, j.custo]
                e.append(kkk)
        g.add_weighted_edges_from(e)
        pos = nx.spring_layout(g)
        g1.add_weighted_edges_from(red_edges)
        nx.draw(g, pos, with_labels=True, font_weight='bold')
        nx.draw(g1, pos, with_labels=True, font_weight='bold',node_color='green')
        edge_weight = nx.get_edge_attributes(g, 'weight')
        nx.draw_networkx_edge_labels(g, pos, edge_labels=edge_weight)
        plt.show()

    def imprimir_grafo(self):
        global todos_adjacentes
        G1 = nx.Graph()
        G = nx.Graph()
        for i in todos_adjacentes:
            G1.add_node(i.rotulo+" "+str(i.distancia_objetivo))
            G.add_node(i.rotulo+" "+str(i.distancia_objetivo))
            o = Vetor_Ordenado(i.adjacentes)
            o.ordenar_menor()
            G1.add_edge(i.rotulo+" "+str(i.distancia_objetivo), o.lista[0].vertice.rotulo+" "+str(o.lista[0].vertice.distancia_objetivo), weight=o.lista[0].custo)
            for j in o.lista:
                G.add_node(j.vertice.rotulo+" "+str(j.vertice.distancia_objetivo))
                G.add_edge(i.rotulo+" "+str(i.distancia_objetivo), j.vertice.rotulo+" "+str(j.vertice.distancia_objetivo), weight= j.custo)

        G1.add_node("Ji-paraná 0")
        edges = G.edges()
        edges = G1.edges()
        pos = nx.spring_layout(G,k=1)
        #pos = nx.graphviz_layout(G, prog='dot')
        nx.draw(G, pos, with_labels=True,font_size=8)
        nx.draw(G1, pos, with_labels=True,node_color='red',edge_color='red',width=3, font_size=8)
        edge_weight = nx.get_edge_attributes(G, 'weight')
        nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_weight)
        plt.show()

    def gerar_grafo_todo(self,lista):
        g = nx.Graph()
        e = []
        for i in lista:
            for j in i.adjacentes:
                kkk = [i.rotulo, j.vertice.rotulo, j.custo]
                e.append(kkk)
        g.add_weighted_edges_from(e)
        pos = nx.spring_layout(g)
        nx.draw(g, pos, with_labels=True, font_weight='bold',font_size=8)
        edge_weight = nx.get_edge_attributes(g, 'weight')
        nx.draw_networkx_edge_labels(g, pos, edge_labels=edge_weight)
        plt.show()

grafo = Grafo()

#des = Desenhar_grafico()
#des.gerar_grafo_todo(grafo.lista_cidades)

#for i in grafo.lista_cidades:
    #for j in i.adjacentes:
        #print(j.vertice.rotulo)
#print(grafo.ariquemes.show_adjacentes())
#print(grafo.jipa.adjacentes[0].vertice.rotulo," Tempo estimado até Jipa (Minutos): ",grafo.jipa.adjacentes[0].vertice.distancia_objetivo,"  Distância (KM): ",grafo.jipa.adjacentes[0].custo, "  Distância A*: ",grafo.jipa.adjacentes[0].distancia_a_star)

#lista = grafo.cacoal.adjacentes
#o = Vetor_Ordenado(lista)
#o.ordenar_menor()
#o.imprimir_adjacentes_ordenados()

busca = A_Star(grafo.jipa)
inicio = grafo.porto_velho
busca.buscar(inicio)


d = Desenhar_grafico()
d.imprimir_grafo()
#d.gerar_grafo_todo(grafo.lista_cidades)