# importa valor infinito
import sys

def algoritimo_dijkstra(grafo, origem, destino): 

    # Inicialização das distâncias (arestas) com infinito, e a origem com zero
    distancias = {v: sys.maxsize for v in grafo}
    distancias[origem] = 0

    # Conjunto de vértices visitados
    visitados = set()

    # Conjunto para rastrear os vértices visitados
    vertices_visitados_caminho = {}

    while visitados != set(distancias):
        # Encontra o vértice não visitado com menor distância atual
        vertice_atual   = None
        menor_distancia = sys.maxsize

        for v in grafo:
            if v not in visitados and distancias[v] < menor_distancia:
                vertice_atual   = v
                menor_distancia = distancias[v]

        # Marca o vértice atual como visitado
        visitados.add(vertice_atual)

        # Atualiza as distâncias dos vértices vizinhos
        for vizinho, peso in grafo[vertice_atual].items():
            if distancias[vertice_atual] + peso < distancias[vizinho]:
                # Atualiza a distância do vértice vizinho 
                distancias[vizinho] = distancias[vertice_atual] + peso
                # Atualiza o vértice visitado para o menor caminho
                vertices_visitados_caminho[vizinho] = vertice_atual
    
    # Recuperando o caminho percorrido
    caminho = [destino]
    while caminho[-1] != origem:
        caminho.append(vertices_visitados_caminho[caminho[-1]])
    caminho.reverse()

    # "->".join() coloca a string entre as iterações
    print(f"O menor caminho percorrido de {origem} até {destino} é:", " -> ".join(caminho))

    # Retorna os km do caminho mais curto
    return distancias[destino]

# Definindo a lista de adjacência
grafo = {
  'A': {'B': 5, 'D': 3, 'E': 10},
  'B': {'A': 5, 'C': 8, 'D': 1},
  'C': {'B': 8},
  'D': {'A': 3, 'B': 1, 'E': 2},
  'E': {'A': 10, 'D': 2}
}

# Ponto de partida
origem  = 'A'
destino = 'C'

print(f"Distância: {algoritimo_dijkstra(grafo, origem, destino)} Km")