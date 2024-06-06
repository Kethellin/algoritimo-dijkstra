# Pega numero infinito
import sys

def algoritimo_dijkstra(grafo, origem, destino):

    # Inicialização das distâncias com infinito, exceto a origem que é zero
    distancias = {v: sys.maxsize for v in grafo}
    distancias[origem] = 0

    # Conjunto de vértices visitados
    visitados = set()

    while visitados != set(distancias):
        # Encontra o vértice não visitado com menor distância atual
        vertice_atual = None
        menor_distancia = sys.maxsize

        for v in grafo:
            if v not in visitados and distancias[v] < menor_distancia:
                # print(f"antigo: {vertice_atual}")
                vertice_atual = v
                # print(f"novo: {vertice_atual}")
                # print(f"antigo d: {menor_distancia}")
                menor_distancia = distancias[v]
                # print(f"novo d: {menor_distancia}")

        print(f"vertice atual: {vertice_atual} menor {menor_distancia} distancia: {distancias[v]}")
        # Marca o vértice atual como visitado
        visitados.add(vertice_atual)

        # Atualiza as distâncias dos vértices vizinhos
        for vizinho, peso in grafo[vertice_atual].items():
            if distancias[vertice_atual] + peso < distancias[vizinho]:
                distancias[vizinho] = distancias[vertice_atual] + peso
    
    # Retorna as distâncias do destino
    return distancias[destino]

# Definindo a lista de adjacencia
grafo = {
  'A': {'B': 5, 'D': 3, 'E': 10},
  'B': {'A': 5, 'C': 8, 'D': 1},
  'C': {'B': 8},
  'D': {'A': 3, 'B': 1, 'E': 2},
  'E': {'A': 10, 'D': 2}
}

# Ponto de partida
origem  = 'A'
destino = 'B'

print(algoritimo_dijkstra(grafo, origem, destino))