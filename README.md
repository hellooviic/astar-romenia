# Astar Romenia

**Disciplina:** Engenharia de Software  
**Projeto:** Busca A* De Arad a Bucareste  
**Aluna:** Nafitaly Vitória da Silva 
**Referência:** Russell e Norvig, Inteligência Artificial, 3ª edição, capítulo 3.

## 1. Sobre o projeto

Este projeto implementa o algoritmo de busca A* (A-Star) utilizando Python para encontrar o caminho de menor custo entre as cidades de Arad e Bucareste, na Romênia.

A implementação utiliza um mapa rodoviário com as distâncias entre as cidades e uma heurística baseada na distância em linha reta até Bucareste.

O desenvolvimento é realizado em seis fases, seguindo o roteiro proposto na disciplina de Engenharia de Software.

## 2. Objetivo

Aplicar conceitos de Inteligência Artificial e estruturas de dados em Python, desenvolvendo uma solução capaz de encontrar o caminho de menor custo entre duas cidades utilizando o algoritmo A*.

O algoritmo utiliza a função:

**f(n) = g(n) + h(n)**

- **g(n):** custo real percorrido desde Arad até a cidade atual.
- **h(n):** estimativa da distância restante até Bucareste.
- **f(n):** custo total estimado do caminho.

A cada iteração, o algoritmo seleciona o nó com o menor valor de f(n).

## 3. Tecnologias utilizadas

- Python 3
- Visual Studio Code
- Git
- GitHub

## 4. Estrutura do projeto

| Arquivo | Descrição |
|---|---|
| `mapa.py` | Armazena o mapa da Romênia e a heurística. |
| `fase1_explorar.py` | Exploração dos dados do mapa. |
| `fase2_caminhos.py` | Cálculo dos custos e valores g, h e f. |
| `fase3_fronteira.py` | Representação dos nós e da fronteira de busca. |
| `fase4_expandir.py` | Expansão dos nós e controle dos explorados. |
| `fase5_busca.py` | Implementação do laço principal da busca A*. |
| `a_estrela.py` | Implementação completa do algoritmo A*. |

## 5. Etapas do desenvolvimento

O projeto foi dividido em seis fases:

1. **Fase 1 — Navegar nos dados:** compreender e explorar as estruturas de dados do mapa.
2. **Fase 2 — Funções e custos:** trabalhar com funções, custos de caminho e valores g, h e f.
3. **Fase 3 — Nó e fronteira:** representar os nós e organizar a fronteira de busca.
4. **Fase 4 — Expansão:** implementar a expansão dos nós e o conjunto de cidades exploradas.
5. **Fase 5 — Busca A*:** desenvolver o laço principal do algoritmo.
6. **Fase 6 — Programa completo:** integrar as etapas em um único programa executável.

Cada fase possui um arquivo próprio e deve ser registrada no GitHub por meio de commits.

## 6. Como executar

É necessário ter o Python 3 instalado.

Clone o repositório:

```bash
git clone https://github.com/hellooviic/astar-romenia.git
```

Entre na pasta do projeto:

```bash
cd astar-romenia
```

Execute o programa:

```bash
python a_estrela.py
```

## 7. Resultado esperado

O algoritmo deve encontrar o caminho de menor custo entre Arad e Bucareste:

**Arad → Sibiu → Rimnicu Vilcea → Pitesti → Bucharest**

- Distância total: **418 km**
- Quantidade de passos: **4**

O resultado deve corresponder ao apresentado na Figura 3.24 do livro de Russell e Norvig.

## 8. Versionamento

O desenvolvimento é acompanhado pelo Git e armazenado em um repositório público no GitHub.

O projeto deve conter pelo menos sete commits, incluindo um para cada fase, além da versão final identificada pela tag `v1.0`.

## 9. Referência bibliográfica

RUSSELL, S.; NORVIG, P. *Inteligência Artificial*. 3. ed. Rio de Janeiro: Elsevier, 2013. Capítulo 3: Resolução de problemas por meio de busca.

