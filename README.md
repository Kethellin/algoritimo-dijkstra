# Algoritmo de Dijkstra para Encontrar o Caminho Mais Curto

Este projeto implementa o algoritmo de Dijkstra para encontrar o caminho mais curto em um grafo. O cenário específico modelado é a entrega de energia para uma casa em um novo bairro.

## Estrutura do Projeto

- `main.py`: Contém a implementação do algoritmo de Dijkstra e a definição do grafo representando o bairro.

## Descrição do Problema

O problema consiste em encontrar o caminho mais curto da subestação de energia até uma casa em um novo bairro. O bairro é modelado como um grafo onde:

- **Vértices**: Representam interseções de ruas e pontos importantes (como subestação, cruzamentos e a casa).
- **Arestas**: Representam as ruas que conectam essas interseções, com pesos associados que podem representar a distância ou custo de instalação do cabeamento.

## Modelagem

### Grafo com lugares do bairro

```python
grafo_bairro = {
    'Subestação': {'Cruzamento Principal': 5, 'Subestação Secundária': 3, 'Praça Central': 10},
    'Cruzamento Principal': {'Subestação': 5, 'Casa': 8, 'Subestação Secundária': 1},
    'Casa': {'Cruzamento Principal': 8},
    'Subestação Secundária': {'Subestação': 3, 'Cruzamento Principal': 1, 'Praça Central': 2},
    'Praça Central': {'Subestação': 10, 'Subestação Secundária': 2}
}
