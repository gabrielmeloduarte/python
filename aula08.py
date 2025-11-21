import random

def rolar_dados():
    """Simula o lançamento de dois dados de 6 lados"""
    dado1 = random.randint(1, 6)
    dado2 = random.randint(1, 6)
    soma = dado1 + dado2
    print(f"Dado 1: {dado1} | Dado 2: {dado2} → Soma = {soma}")
    return soma

def jogar_craps():
    print("BEM-VINDO AO JOGO DE CRAPS!")
    print("Regras rápidas:")
    print("• 7 ou 11 na primeira jogada → VITÓRIA (natural)!")
    print("• 2, 3 ou 12 na primeira jogada → PERDEU (craps)!")
    print("• Qualquer outro número vira seu 'Ponto'. Continue rolando até repetir o Ponto.")
    print("• Se tirar 7 antes de repetir o Ponto → PERDEU!\n")
    print("-" * 50)

    ponto = None  # Ainda não foi definido
    primeira_jogada = True

    while True:
        input("\nPressione ENTER para rolar os dados...")
        resultado = rolar_dados()

        if primeira_jogada:
            if resultado in (7, 11):
                print("Você tirou", resultado, "→ NATURAL!")
                print("PARABÉNS! VOCÊ GANHOU!")
                break
            elif resultado in (2, 3, 12):
                print("Você tirou", resultado, "→ CRAPS!")
                print("Que pena... VOCÊ PERDEU!")
                break
            else:
                ponto = resultado
                print(f"Você tirou {ponto} → Este é o seu PONTO!")
                print(f"Agora continue rolando até tirar {ponto} novamente.")
                print("Cuidado: se tirar 7 antes, você perde!")
                primeira_jogada = False
        else:
            # Jogadas seguintes: tentando repetir o ponto
            if resultado == ponto:
                print(f"Você tirou {resultado} → Igual ao PONTO!")
                print("PARABÉNS! VOCÊ GANHOU!")
                break
            elif resultado == 7:
                print("Você tirou 7 antes do Ponto → PERDEU!")
                break
            else:
                print(f"Você tirou {resultado}. Continue tentando tirar {ponto}...")

    print("\nFim do jogo!")

# ================================
# INICIAR O JOGO
# ================================
if __name__ == "__main__":
    while True:
        jogar_craps()
        print("\n" + "=" * 50)
        novamente = input("Deseja jogar novamente? (s/n): ").strip().lower()
        if novamente not in ["s", "sim", "y", "yes"]:
            print("Obrigado por jogar Craps! Boa sorte da próxima!")
            break
        print("\n" + "=" * 50)
        