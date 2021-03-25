def descobreMatrizMenor(matriz, posicao_i, posicao_j):
    '''A menor de um elemento de uma matriz é a matriz que se 
forma quando retiramos da matriz inicial a linha e coluna na
qual este elemento pertence'''
    assert len(matriz) == len(matriz[0]) # garante que a matriz é quadraada
    matriz_menor = []
    for i in range(len(matriz)):
        vetor = [] # incializa um vetor que posteriormente será adicionado à matriz menor
        if i == posicao_i:
            continue
        for j in range(len(matriz[0])):
            if j != posicao_j:
                vetor.append(matriz[i][j]) # se i ou j não forem os passados como parâmetro, adiciona o elemento aij na vetor
        matriz_menor.append(vetor) # adiciona o vetor na matriz menor
    return matriz_menor

def determinante(matriz):
    '''Para calcular o determinante de uma matriz Anxn são necessários
    os cofatores de uma linha ou coluna específica. Para a forma
    que faremos o cálculo do determinante, utilizaremos a linha i = 0.
    det(A) = c11 . a11 + c12 . a12 + ... + c1n . a1n'''
    assert len(matriz) == len(matriz[0]) # garante que a matriz é quadraada
    if len(matriz) == 2: # base da recursão
        return (matriz[0][0] * matriz[1][1]) - (matriz[0][1] * matriz[1][0]) # cálculo utilizado para descobrir o determinante de matrizes 2x2
    else:
        determinantesMenor = [determinante(descobreMatrizMenor(matriz, 0, j)) for j in range(len(matriz[0]))] # lista dos determinantes das matrizes menores da primeira linha a matriz principal
        soma = 0
        for j in range(len(determinantesMenor)):
            cij = determinantesMenor[j] if (j + 2) % 2 == 0 else -1 * determinantesMenor[j] # determina se o cofator é positivo ou negativo, de acordo com a soma de i e j
            # obs: Como em python o primeiro elemento de uma lista é 0, adicionamos +1 na posição i e na posição j. Levando em consideração que estamos usando a linha i = 0,
            # i+j = j + 2
            soma += cij * matriz[0][j] # adiciona a multiplicação entre o cofator e o valor do elemento usado no cálculo da menor para calcular o determinante 
        return soma # o resultado da soma é o determinante da matriz desejada

if __name__ == '__main__':
    from random import randint

    def cria_linha(tamanho):
        return [randint(0,9) for _ in range(tamanho)]

    matriz_exemplo10 = []
    for i in range(10):
        matriz_exemplo10.append(cria_linha(10))

    print("Matriz 10x10:")
    for i in range(10):
        print(*matriz_exemplo10[i], sep='\t')

    print('resultado: ', determinante(matriz_exemplo10))
    print('\npara garantir os resultados acesse:')
    print('https://matrixcalc.org/pt/det.html')