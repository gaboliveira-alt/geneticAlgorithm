# Genetic Algorithm - BF2 & CB3

Implementação de um **Algoritmo Genético com codificação real** para minimizar duas funções benchmark clássicas de otimização global:

- **bf2/** → Função Bohachevsky 2  
- **cb3/** → Função Three-Hump Camel (Camel Back-3)

**Objetivo**  
Avaliar o desempenho do GA (taxa de sucesso e número médio de avaliações de fitness - NFE) em problemas multimodais 2D, utilizando:
- Seleção por ranking
- Crossover aritmético
- Mutação uniforme
- Elitismo

Cada pasta contém uma versão completa e independente do algoritmo adaptada ao problema (limites de busca, taxa de mutação e função de fitness específicas).

Para executar:
```bash
python bf2/main.py     # ou
python cb3/main.py