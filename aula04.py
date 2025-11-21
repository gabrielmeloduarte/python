from itertools import permutations

def exibir_quadrado(vetor):
    """Exibe o quadrado mágico formatado"""
    print("┌───┬───┬───┐")
    for i in range(3):
        print("│", end="")
        for j in range(3):
            print(f" {vetor[i*3 + j]:1} ", end="│")
        if i < 2:
            print("\n├───┼───┼───┤")
        else:
            print("\n└───┴───┴───┘")

def eh_quadrado_magico(vetor):
    """Verifica se o vetor 1D forma um quadrado mágico 3x3"""
    # Soma mágica para números de 1 a 9 → sempre 15
    soma_magica = 15

    # Linhas
    for i in range(3):
        if vetor[i*3] + vetor[i*3+1] + vetor[i*3+2] != soma_magica:
            return False

    # Colunas
    for j in range(3):
        if vetor[j] + vetor[j+3] + vetor[j+6] != soma_magica:
            return False

    # Diagonal principal
    if vetor[0] + vetor[4] + vetor[8] != soma_magica:
        return False

    # Diagonal secundária
    if vetor[2] + vetor[4] + vetor[6] != soma_magica:
        return False

    return True

def encontrar_todos_quadrados_magicos():
    numeros = list(range(1, 10))  # [1, 2, 3, ..., 9]
    encontrados = 0

    print("Procurando todos os quadrados mágicos 3x3 com números de 1 a 9...\n")
    
    for perm in permutations(numeros):
        if eh_quadrado_magico(perm):
            encontrados += 1
            print(f"Quadrado Mágico #{encontrados}:")
            exibir_quadrado(perm)
            print()  # linha em branco entre quadrados

    print(f"\nTotal de quadrados mágicos encontrados: {encontrados}")
    print("Observação: Todos são rotações ou reflexões do quadrado mágico único de ordem 3.")

# Executa o programa
encontrar_todos_quadrados_magicos()