# Algoritmo genético

O objetivo deste trabalho é implementar um algoritmo genético que otimize os problemas escolhidos.

<b>Disciplina:</b> Computação Evolutiva

<b>Professor:</b> Dante Augusto Barone

<b>Alunos:</b>
- Augusto Boranga
- Matheus Pereira

## Problemas escolhidos

- Shubert's function
- Drop wave

## Implementação

Fizemos a implementação tanto das funções de otimização quanto do algoritmo genético em Python, devido à sua adequação ao meio acadêmico.

Para executar o algoritmo para a função de Shubert, basta rodar `python genetic_algorithm.py shubert` pela linha de comando.

Similarmente, `python genetic_algorithm.py drop_wave` executa o algoritmo para a função de Drop Wave.

### Geração de filhos

A cada iteração do algoritmo, mantemos uma parte da população e removemos outra parte. Preenchemos o espaço dos elementos removidos com filhos dos elementos mantidos.

Para gerar cada um destes filhos, seguimos o seguinte processo:

- São escolhidos 2 pais aleatórios dentre os elementos da população;
- É feita uma média dos atributos (x1 e x2) dos pais escolhidos. Estes valores médios são atribuídos ao filho.

O filho é, então, adicionado à população.

### Mutação

O algoritmo percorre a população. Cada elemento possui chance de 30 % de sofrer a mutação explicada a seguir:

- É escolhido um atributo (x1 ou x2) aleatoriamente;
- É somado a ela um valor aleatório entre -1 e 1;
- O valor do atributo alterado é arredondado caso passe do valor máximo ou fique abaixo do mínimo (intervalo [-5.12, 5.12]).

## Resultados

Os resultados obtidos para cada problema foram:

### Shubert

Obtivemos -165.02102791413492 com os valores:

- x1 = 0.42097338324679423
- x2 = 0.4080882644212212

O resultado ótimo é -185. Atingimos aproximadamente 85 % do valor esperado. Consideramos satisfatório.

### Drop Wave

Obtivemos -0.9362453278079418 com os valores:

- x1 = 0.13408399394180204
- x2 = 0.5026387476441556

O resultado ótimo é -1. Atingimos aproximadamente 93 % do valor esperado. Consideramos satisfatório.
