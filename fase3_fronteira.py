# -*- coding: utf-8 -*-
# fase3_fronteira.py — Fase 3: o nó de busca e a fronteira, feitos à mão.
# Rode com: python fase3_fronteira.py

# ----- PASSO 1: importar os dados -----
from mapa import mapa_romenia, heuristica_bucareste

# esse código define a cidade inicial da busca, que é Arad.
# como ainda não percorremos nenhuma estrada, o custo g começa em zero.
# o valor h representa a estimativa da distância que falta até Bucareste.

# ----- PASSO 2: montar o nó inicial e a fronteira -----
# Um nó é uma tupla com 4 posições: (f, g, cidade, caminho)
inicio = 'Arad'
g = 0
h = heuristica_bucareste[inicio]
no_inicial = (g + h, g, inicio, [inicio])

# a fronteira é uma lista que guarda os nós que ainda podem ser explorados.

fronteira = [no_inicial]
print('Fronteira no começo:', fronteira)

# esse comando remove o primeiro nó da fronteira e o armazena na variável no.
# em seguida, cada informação da tupla é separada em uma variável.

# ----- PASSO 3: tirar o primeiro nó da fronteira -----
no = fronteira.pop(0)
f_atual, g_atual, cidade_atual, caminho = no
print()
print('Nó retirado:', no)
print(' f =', f_atual, '| g =', g_atual, '| cidade =', cidade_atual,
      '| caminho =', caminho)
print('Fronteira agora:', fronteira)

# esse laço percorre todas as cidades vizinhas da cidade atual.

# ----- PASSO 4: gerar os filhos (vizinhos) do nó retirado -----
for vizinho, custo_estrada in mapa_romenia[cidade_atual]:
    novo_g = g_atual + custo_estrada
    novo_h = heuristica_bucareste[vizinho]
    novo_f = novo_g + novo_h
    novo_caminho = caminho + [vizinho]
    fronteira.append((novo_f, novo_g, vizinho, novo_caminho))

print()
print('Fronteira depois de expandir Arad (ordem de inserção):')
for item in fronteira:
    print(' ', item)

# print adicional para visualizar os nós que foram adicionados à fronteira.
# nesse momento, são os três vizinhos de Arad.
print()
print('Fronteira depois de expandir Arad (ordem de inserção):')
for item in fronteira:
    print(' ', item)

# ----- PASSO 5: ordenar a fronteira pelo f -----
fronteira.sort(key=lambda no: no[0])
print()
print('Fronteira ordenada pelo f (posição 0 da tupla):')
for item in fronteira:
    print(' ', item)


# ----- PASSO 6: o próximo nó a ser expandido -----
proximo = fronteira.pop(0)
print()
print('Próximo nó a expandir:', proximo[2], 'com f =', proximo[0])

