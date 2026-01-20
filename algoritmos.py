import numpy as np

# Simulação do Algoritmo de Consenso (Eq. 3 e 15 do paper)
def rodar_consenso(grafo, iteracoes=20):
    # 1. Inicialização: Cada área começa com um Custo Marginal (Lambda) diferente
    # No paper, isso vem das equações de custo. Aqui, vamos chutar valores iniciais.
    lambdas = {node: np.random.uniform(10, 50) for node in grafo.nodes()}
    
    historico = [] # Para guardar os dados e fazer gráfico depois
    
    print(f"Valores Iniciais (Lambda): {lambdas}")

    # 2. Loop de Iteração (O tempo 't' no paper)
    for t in range(iteracoes):
        # Guardamos uma cópia para não usar valores atualizados na mesma rodada
        novos_lambdas = lambdas.copy()
        
        # Para cada agente (área) no sistema
        for i in grafo.nodes():
            vizinhos = list(grafo.neighbors(i))
            
            if not vizinhos:
                continue
            
            # A Lógica do Consenso:
            # O novo valor é influenciado pela média dos vizinhos
            # x_i[t+1] = soma(d_ij * x_j[t])
            
            soma_vizinhos = sum(lambdas[vizinho] for vizinho in vizinhos)
            
            # Média simples entre o próprio valor e os vizinhos
            # (No paper usam a matriz Laplaciana, aqui simplificamos pela média)
            novo_valor = (soma_vizinhos + lambdas[i]) / (len(vizinhos) + 1)
            
            novos_lambdas[i] = novo_valor
        
        # Atualiza o estado do sistema
        lambdas = novos_lambdas
        # Guarda o valor do Agente 1 para ver a convergência no gráfico
        historico.append(lambdas[1]) 

    return lambdas, historico