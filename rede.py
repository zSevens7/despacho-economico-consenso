import networkx as nx
import matplotlib.pyplot as plt

def criar_sistema_exemplo():
    # Cria um grafo vazio
    G = nx.Graph()
    
    # Adicionando 5 áreas (agentes) como no exemplo simplificado
    # Imagine que são 5 áreas conectadas por linhas de transmissão
    conexoes = [(1, 2), (2, 3), (3, 4), (4, 5), (2, 5)]
    G.add_edges_from(conexoes)
    
    return G

def desenhar_rede(G):
    # Função para visualizar o sistema
    plt.figure(figsize=(6, 4))
    pos = nx.spring_layout(G) # Define posições automáticas
    nx.draw(G, pos, with_labels=True, node_color='skyblue', node_size=1500, font_weight='bold')
    plt.title("Topologia do Sistema de Potência (Agentes)")
    plt.show()