def calcular_percentual(votos_jogador, total_votos):
    if total_votos == 0:
        return 0.0
    return (votos_jogador / total_votos) * 100

# Dicionário para armazenar os votos (camisa → quantidade)
votos = {i: 0 for i in range(1, 24)}  # inicializa jogadores 1 a 23 com 0 votos

print("Enquete: Quem foi o melhor jogador?\n")

while True:
    try:
        num = int(input("Número do jogador (0=fim): "))
    except ValueError:
        print("Por favor, digite um número válido!")
        continue

    if num == 0:
        break
    if num < 1 or num > 23:
        print("Informe um valor entre 1 e 23 ou 0 para sair!")
        continue
    
    votos[num] += 1

# Calcula o total de votos válidos
total_votos = sum(votos.values())

# Encontra o melhor jogador
melhor_jogador = 0
max_votos = 0
for jogador, qtd in votos.items():
    if qtd > max_votos:
        max_votos = qtd
        melhor_jogador = jogador

# Exibe o resultado na tela
print("\nResultado da votação:\n")
print(f"Foram computados {total_votos} votos.\n")
print(f"{'Jogador':<8} {'Votos':<12} %")

jogadores_com_voto = [(j, v) for j, v in votos.items() if v > 0]

for jogador, qtd in sorted(jogadores_com_voto):
    percentual = calcular_percentual(qtd, total_votos)
    print(f"{jogador:<8} {qtd:<12} {percentual:.1f}%")

if total_votos > 0:
    percentual_melhor = calcular_percentual(max_votos, total_votos)
    print(f"\nO melhor jogador foi o número {melhor_jogador}, com {max_votos} votos, "
          f"correspondendo a {percentual_melhor:.1f}% do total de votos.")
else:
    print("\nNenhum voto foi computado.")

# Grava o resultado em um arquivo texto
with open("resultado_enquete.txt", "w", encoding="utf-8") as arquivo:
    arquivo.write("Resultado da votação:\n\n")
    arquivo.write(f"Foram computados {total_votos} votos.\n\n")
    arquivo.write(f"{'Jogador':<8} {'Votos':<12} %\n")
    
    for jogador, qtd in sorted(jogadores_com_voto):
        percentual = calcular_percentual(qtd, total_votos)
        arquivo.write(f"{jogador:<8} {qtd:<12} {percentual:.1f}%\n")
    
    if total_votos > 0:
        percentual_melhor = calcular_percentual(max_votos, total_votos)
        arquivo.write(f"\nO melhor jogador foi o número {melhor_jogador}, com {max_votos} votos, "
                     f"correspondendo a {percentual_melhor:.1f}% do total de votos.\n")
    else:
        arquivo.write("\nNenhum voto foi computado.\n")

print("\nResultado salvo no arquivo 'resultado_enquete.txt'")