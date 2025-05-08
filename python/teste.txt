import networkx as nx
#import matplotlib.pyplot as plt


# --- AULA PRÁTICA 20/06/2023 ---
# ---  INÍCIO ---

# Criar um grafo vazio


# Adicionar os vértices


# Adicionar arestas


# Listar vértices
print('Lista de vértices')


# Percorrer a lista de vértices
print('Percorrendo a lista')


# Listar arestas
print('Lista de arestas')


# Percorrer a lista de arestas
print('Percorrendo a lista')


# Imprimir lista de graus
print('Graus de G')


# Acessando o grau de um vértice especifico (e)


# Plotando o grafo como imagem
print('Plotando o grafo G na tela como sendo uma imagem')




# --- AULA PRÁTICA 20/06/2023 ---
# ---  FIM ---


# --- ATIVIDADES A SEREM FEITAS ---
# ---  INÍCIO ---

# (Questão 1): 
# Em sala de aula vimos que para um grafo G = (V,E), tal que V = {v1, v2, ..., vn} (|V| = n) e 
# E = {e1, e2, ..., en} (|E| = m), tem-se: Soma(d(vi)) = 2m para i = 1 até n
# sendo d(v) denotando o grau (degree) do vértice v. Por convênção, denominamos esse terorema de TEOREMA 3.1.
# Com isso, pede-se que seja criada uma função em PYTHON que receba como parâmetro um grafo G e 
# calcule e retorne a SOMA DOS GRAUS de seus vértices usando o TEOREMA 3.1.
# Segue abaixo o protótipo da função a ser utilizada:

def somaGrausComTeorema(G):
    somaGraus = 0
    
    for v in G:
        grau = len(G[v])
        somaGraus += grau
    
    somaGraus *= 2
    
    return somaGraus


# (Questão 2):  
# Calcule e retorne a SOMA DOS GRAUS dos vértices G sem ter que usar o TEOREMA 3.1.
# Segue abaixo o protótipo da função a ser utilizada:

def somaGrausSemTeorema(G):
    somaGraus = 0
    
    contador = {}
    
    for aresta in G:
        v1, v2 = aresta
        
        contador[v1] = contador.get(v1, 0) + 1
        contador[v2] = contador.get(v2, 0) + 1
        

    for v in contador:
        somaGraus += contador[v]
    
    return somaGraus

# (Questão 3):  
# Obtenha as matrizes de adjacências do grafo G de duas formas diferentes: ESPARSA e DENSA.
# Segue abaixo os protótipos das funções a serem utilizadas:

# ATIVIDADE 3
def matrizAdjacenciaDensa(G):
    matrizAdj = []

    matrizAdj = nx.adjacency_matrix(G)

    matrizAdj = matrizAdj.todense()

    return matrizAdj

# (Questão 4):  
# Adicione um campo PESO em cada aresta do grafo G.
# Segue abaixo o protótipo da função a ser utilizada:

def grafoComPeso(G):
    #Aqui você usa API do networkx para adicionar os pesos nas arestas do grafo G criadas na linha 13
    # ATIVIDADE 4

    G["v1"]["v2"]["Peso"] = 8
    G["v2"]["v3"]["Peso"] = 1
    G["v3"]["v4"]["Peso"] = 2
    G["v4"]["v5"]["Peso"] = 6
    G["v5"]["v1"]["Peso"] = 10
    G["v2"]["v4"]["Peso"] = 4

    print("Arestas atualizadas com seus respectivos pesos")

# (Questão 5):  
# Liste cada aresta do grafo G e seus respectivos pesos.
# Segue abaixo o protótipo da função a ser utilizada:

def listarGrafoComSeusPesos(G):
    #Aqui você usará o API do networkx para listar cada aresta do grafo G e seus respectivos pesos
    print("Listando cada aresta do grafo G e seus respectivos pesos ...")
    for u, v, data in G.edges(data=True):
        peso = data['weight']
        print(f"Aresta: ({u}, {v}), Peso: {peso}")

# (Questão 6):  
# Plote na tela o grafo G como uma imagem utilizando a API do networkx e a biblioteca matplotlib.pyplot as plt
# instalada na linha 2.
# Segue abaixo os protótipos das funções a serem utilizadas:

def plotarGrafoComoImagem(G):
    print("Plotando o grafo como imagem ...")
    pos = nx.spring_layout(G)
    nx.draw(G, pos, with_labels=True, node_color='lightblue', edge_color='gray')
    labels = nx.get_edge_attributes(G, 'weight')
    nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)
    #plt.show()


# --- ATIVIDADES A SEREM FEITAS ---
# ---  FIM ---