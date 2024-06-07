import sys

def algoritimo_dijkstra(grafo, origem, destino):
    # Inicialização das distâncias (arestas) com infinito, e a origem com zero
    distancias = {v: sys.maxsize for v in grafo}
    distancias[origem] = 0

    # Conjunto de vértices visitados
    visitados = set()

    # Conjunto para rastrear os vértices visitados
    vertices_visitados_caminho = {}

    while visitados != set(grafo.keys()):
        # Encontra o vértice não visitado com menor distância atual
        vertice_atual = None
        menor_distancia = sys.maxsize

        for v in grafo:
            if v not in visitados and distancias[v] < menor_distancia:
                vertice_atual = v
                menor_distancia = distancias[v]

        if vertice_atual is None:
            break

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
    caminho_formatado = " -> ".join(caminho)
    return distancias[destino], caminho_formatado

# Definindo a lista de adjacência do bairro com lugares
grafo_bairro = {
    'Subestação': {'Cruzamento Principal': 5, 'Subestação Secundária': 3, 'Praça Central': 10},
    'Cruzamento Principal': {'Subestação': 5, 'Casa': 8, 'Subestação Secundária': 1},
    'Casa': {'Cruzamento Principal': 8},
    'Subestação Secundária': {'Subestação': 3, 'Cruzamento Principal': 1, 'Praça Central': 2},
    'Praça Central': {'Subestação': 10, 'Subestação Secundária': 2}
}

# Definindo a lista de adjacência do bairro de forma simplificada
grafo_simplificado = {
    'A': {'B': 5, 'D': 3, 'E': 10},
    'B': {'A': 5, 'C': 8, 'D': 1},
    'C': {'B': 8},
    'D': {'A': 3, 'B': 1, 'E': 2},
    'E': {'A': 10, 'D': 2}
}

# Ponto de partida e destino para ambos os grafos
origem_bairro = 'Subestação'
destino_bairro = 'Casa'

origem_simplificado = 'A'
destino_simplificado = 'C'

# Executando o algoritmo para o grafo bairro
distancia_bairro, caminho_bairro = algoritimo_dijkstra(grafo_bairro, origem_bairro, destino_bairro)
print('\n')
print(f"Demonstração com lugares do bairro:")
print(f"O menor caminho percorrido de {origem_bairro} até {destino_bairro} é: {caminho_bairro}")
print(f"Distância: {distancia_bairro} Km")

print("\n==========================================================================================\n")

# Executando o algoritmo para o grafo simplificado
distancia_simplificado, caminho_simplificado = algoritimo_dijkstra(grafo_simplificado, origem_simplificado, destino_simplificado)
print(f"Demonstração de forma simplificada:")
print(f"O menor caminho percorrido de {origem_simplificado} até {destino_simplificado} é: {caminho_simplificado}")
print(f"Distância: {distancia_simplificado} Km")
