# Despacho Econômico Multi-Área Descentralizado (Simulação em Python)

Este repositório contém uma implementação prática e computacional dos algoritmos propostos no artigo científico **"Decentralized Multi-Area Economic Dispatch in Power Systems Using the Consensus Algorithm"**.

O projeto simula um sistema de potência dividido em múltiplas áreas, onde agentes inteligentes negociam de forma descentralizada para encontrar o custo ótimo de geração de energia, sem a necessidade de um coordenador central único.

## 📄 Referência Científica
Baseado no trabalho de:
* [cite_start]**Artigo:** Decentralized Multi-Area Economic Dispatch in Power Systems Using the Consensus Algorithm [cite: 4]
* [cite_start]**Autores:** Ying-Yi Hong & Hao Zeng (Chung Yuan Christian University, Taiwan) [cite: 5, 6]
* [cite_start]**Publicação:** Energies 2024, 17, 3609 [cite: 18]

## 🚀 Funcionalidades do Projeto

Esta simulação reproduz os conceitos fundamentais do estudo utilizando Python:

1.  [cite_start]**Modelagem de Grafos (NetworkX):** Representação da topologia da rede elétrica e das conexões de comunicação entre as áreas[cite: 100].
2.  [cite_start]**Busca em Largura (BFS):** Implementação do algoritmo *Breadth-First Search* para identificar o "Agente Líder" de cada área de forma otimizada, reduzindo o tempo de convergência[cite: 12, 87].
3.  [cite_start]**Algoritmo de Consenso:** Simulação do loop de iteração onde os agentes atualizam seus Custos Incrementais ($\lambda$) baseados na média ponderada dos vizinhos, até atingirem o consenso (equilíbrio)[cite: 10, 114].
4.  **Dashboard de Resultados:** Geração de gráficos visuais demonstrando a topologia e a curva de convergência dos agentes.

## 🛠️ Tecnologias Utilizadas

* **Python 3.x**
* **NetworkX:** Para criação e manipulação da estrutura de grafos (nós e arestas).
* **NumPy:** Para cálculos matriciais e simulação numérica.
* **Matplotlib:** Para plotagem dos gráficos de convergência e visualização da rede.

## 📂 Estrutura do Código

* `rede.py`: Define a estrutura física do sistema (criação dos agentes e conexões).
* `algoritmos.py`: Contém a lógica matemática (BFS e Loop de Consenso).
* `main.py`: Script principal de execução.
* `dashboard.py`: Script para gerar o painel visual com topologia, gráfico de convergência e tabela de resultados.

## 📊 Como Executar

1.  Clone este repositório:
    ```bash
    git clone [https://github.com/SEU-USUARIO/despacho-economico-consenso.git](https://github.com/SEU-USUARIO/despacho-economico-consenso.git)
    ```
2.  Instale as dependências:
    ```bash
    pip install networkx numpy matplotlib
    ```
3.  Execute a simulação visual:
    ```bash
    python dashboard.py
    ```

## 📈 Resultados Esperados

Ao rodar a simulação, o sistema demonstra que, independentemente dos custos iniciais aleatórios de cada gerador, o algoritmo força todos os agentes a convergirem para um único **Custo Marginal ($\lambda$)**. [cite_start]Isso valida a robustez da abordagem descentralizada proposta por Hong & Zeng[cite: 14].

---
*Projeto desenvolvido como parte do Seminário de Engenharia Elétrica.*
