import rede
import algoritmos
import matplotlib.pyplot as plt

# 1. Criar a rede (Baseado na topologia do sistema)
sistema = rede.criar_sistema_exemplo()

# 2. Visualizar a rede (opcional - vai abrir uma janela)
print("Gerando visualização da rede...")
rede.desenhar_rede(sistema)

# 3. Rodar o Algoritmo do Paper
print("\n--- Iniciando Algoritmo de Consenso Descentralizado ---")
resultados_finais, historico_convergencia = algoritmos.rodar_consenso(sistema, iteracoes=30)

# 4. Mostrar Resultados
print("\n--- Resultado Final (Custo Marginal Uniforme) ---")
for agente, valor in resultados_finais.items():
    print(f"Agente {agente}: Lambda = {valor:.4f} $/MWh")

# 5. Gráfico de Convergência (Como a Figura 7 do paper)
plt.plot(historico_convergencia)
plt.xlabel('Iterações')
plt.ylabel('Valor de Lambda ($/MWh)')
plt.title('Convergência do Consenso (Agente 1)')
plt.grid(True)
plt.show()