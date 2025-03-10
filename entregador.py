partida = 'P'
pontos = ['A', 'B', 'C', 'D']
grafo = {
    'P': {'A': 5, 'B': 8, 'C': 10, 'D': 7},
    'A': {'P': 5, 'B': 6, 'C': 9, 'D': 4},
    'B': {'P': 8, 'A': 6, 'C': 3, 'D': 5},
    'C': {'P': 10, 'A': 9, 'B': 3, 'D': 2},
    'D': {'P': 7, 'A': 4, 'B': 5, 'C': 2},
}

def mostra_distancia(ponto1,ponto2,grafo):
        print(f"distancia de {ponto1} ate {ponto2} : {grafo[ponto1][ponto2]} km.")

mostra_distancia('D','B',grafo)

#terminar: calcular menor rota
