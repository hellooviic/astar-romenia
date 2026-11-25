# -*- coding: utf-8 -*-
# fase1_explorar.py — Fase 1: navegar nos dados, sem nenhuma busca ainda.
# Rode com: python fase1_explorar.py

# ----- PASSO 1: trazer os dados do arquivo mapa.py -----
from mapa import mapa_romenia, heuristica_bucareste

#print para ver o que foi importado

# ----- PASSO 2: quantas cidades existem? -----
print('Quantidade de cidades no mapa:', len(mapa_romenia))
print('Quantidade de valores de h(n):', len(heuristica_bucareste))

# ----- PASSO 3: olhar o valor guardado em uma chave -----
vizinhos_arad = mapa_romenia['Arad']
print()
print('Vizinhos de Arad:', vizinhos_arad)
print('Tipo do valor:', type(vizinhos_arad))

#print('Mapa Romenia:', mapa_romenia)

#o código abaixo mostra como acessar os vizinhos de Arad e o custo da estrada até cada um deles, usando um for para percorrer a lista de tuplas

# ----- PASSO 4: pegar uma tupla e as partes dela -----
primeira = vizinhos_arad[0]
print()
print('Primeira estrada que sai de Arad:', primeira)
print(' posição [0] -> cidade vizinha:', primeira[0])
print(' posição [1] -> custo em km :', primeira[1])

#o for abaixo percorre a lista de vizinhos de Arad, desempacotando cada tupla em duas variáveis (vizinho e custo) e imprimindo o resultado

# ----- PASSO 5: percorrer a lista com for e desempacotar -----
print()
print('Estradas que saem de Arad:')
for vizinho, custo in mapa_romenia['Arad']:
    print(' Arad ->', vizinho, '=', custo, 'km')
   
#mostra o número de vizinhos de cada cidade, percorrendo o dicionário mapa_romenia com um for    

# ----- PASSO 6: percorrer o mapa inteiro -----
print()
print('Número de estradas de cada cidade:')
for cidade in mapa_romenia:
    quantidade = len(mapa_romenia[cidade])
    print(f' {cidade:<15} {quantidade} estrada(s)')

#prints para mostrar a heurística de cada cidade, percorrendo o dicionário heuristica_bucareste com um for

# ----- PASSO 7: consultar a heurística -----
print()
print('h(Arad) =', heuristica_bucareste['Arad'], 'km em linha reta até Bucareste')
print('Para cada vizinho de Arad: custo da estrada e h(vizinho)')
for vizinho, custo in mapa_romenia['Arad']:
    h = heuristica_bucareste[vizinho]
    print(f' {vizinho:<10} estrada = {custo:>3} km h = {h:>3} km')
    


    