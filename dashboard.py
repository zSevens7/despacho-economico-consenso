import matplotlib.pyplot as plt
import networkx as nx
import numpy as np
import rede
import algoritmos

# --- Configuração Visual para Slides ---
plt.style.use('default') # Garante fundo branco limpo
plt.rcParams['font.family'] = 'sans-serif'
plt.rcParams['font.size'] = 10

def gerar_dashboard():
    # 1. Preparar os Dados
    G = rede.criar_sistema_exemplo()
    # Guardamos os valores iniciais (simulando novamente para pegar o estado inicial exato)
    lambdas_iniciais = {node: np.random.uniform(20, 40) for node in G.nodes()}
    
    # Rodamos o algoritmo (usando a lógica do arquivo algoritmos.py, mas adaptada aqui para garantir os dados)
    # Nota: Estamos re-executando a lógica aqui brevemente para ter controle total das variáveis no gráfico
    lambdas_finais = lambdas_iniciais.copy()
    historico = []
    
    for t in range(30): # 30 iterações
        novos_lambdas = lambdas_finais.copy()
        for i in G.nodes():
            vizinhos = list(G.neighbors(i))
            soma = sum(lambdas_finais[v] for v in vizinhos)
            novos_lambdas[i] = (soma + lambdas_finais[i]) / (len(vizinhos) + 1)
        lambdas_finais = novos_lambdas
        historico.append(lambdas_finais[1]) # Monitorando Agente 1

    # --- 2. Criar o Layout do Dashboard (Grid) ---
    fig = plt.figure(figsize=(14, 8))
    fig.suptitle("Simulação de Consenso Descentralizado (Multi-Agentes)", fontsize=16, weight='bold')

    # Layout: 2 linhas, 2 colunas
    # Posição 1: Topo Esquerda (Rede)
    ax1 = plt.subplot2grid((2, 2), (0, 0))
    pos = nx.spring_layout(G, seed=42) # Seed fixa para o desenho não mudar
    nx.draw(G, pos, ax=ax1, with_labels=True, 
            node_color='#4A90E2', node_size=2000, 
            font_color='white', font_weight='bold', edge_color='gray')
    ax1.set_title("1. Topologia da Rede (Agentes)", fontsize=12, pad=10)
    ax1.set_axis_off() # Remove bordas quadradas feias

    # Posição 2: Topo Direita (Gráfico de Convergência)
    ax2 = plt.subplot2grid((2, 2), (0, 1))
    ax2.plot(historico, color='#E74C3C', linewidth=2.5, marker='o', markersize=4, markevery=3)
    ax2.set_title("2. Convergência do Custo Incremental ($\lambda$)", fontsize=12)
    ax2.set_xlabel("Iterações (Tempo)")
    ax2.set_ylabel("Custo Marginal ($/MWh)")
    ax2.grid(True, linestyle='--', alpha=0.7)
    
    # Adicionar anotação do valor final no gráfico
    valor_final = historico[-1]
    ax2.annotate(f'Consenso: {valor_final:.2f}', 
                 xy=(29, valor_final), xytext=(15, valor_final - 2),
                 arrowprops=dict(facecolor='black', shrink=0.05))

    # Posição 3: Parte de Baixo (Tabela de Resultados)
    ax3 = plt.subplot2grid((2, 2), (1, 0), colspan=2)
    ax3.axis('off')
    ax3.set_title("3. Resultados Numéricos: Otimização", fontsize=12, y=0.9)

    # Dados da Tabela
    colunas = ("Agente (Área)", "Lambda Inicial ($)", "Lambda Final ($)", "Status")
    linhas = []
    for i in sorted(G.nodes()):
        inicial = lambdas_iniciais[i]
        final = lambdas_finais[i]
        linhas.append([f"Área {i}", f"{inicial:.2f}", f"{final:.4f}", "Otimizado"])

    # Desenhar Tabela
    tabela = ax3.table(cellText=linhas, colLabels=colunas, loc='center', cellLoc='center')
    tabela.auto_set_font_size(False)
    tabela.set_fontsize(11)
    tabela.scale(1, 1.8) # Deixa a tabela mais alta e legível

    # Ajustes finais
    plt.tight_layout(rect=[0, 0.03, 1, 0.95]) # Ajusta margens para não cortar o título
    
    print("Gerando Dashboard final para o slide...")
    plt.show()

if __name__ == "__main__":
    gerar_dashboard()