# Dados dos carros (você pode alterar conforme quiser)
modelos = ["fusca", "gol", "uno", "vectra", "peugeot"]
consumo = [7, 10, 12.5, 9, 14.5]  # km por litro

preco_gasolina = 2.25
distancia = 1000  # quilômetros

print("Comparativo de Consumo de Combustível")
print()

# Exibe os dados iniciais
for i in range(5):
    print(f"Veículo {i+1}")
    print(f"Nome: {modelos[i]}")
    print(f"Km por litro: {consumo[i]}")
    print()

print("Relatório Final")

# Calcula litros necessários e custo para 1000 km
litros_por_carro = []
custo_por_carro = []

for i in range(5):
    litros = distancia / consumo[i]
    custo = litros * preco_gasolina
    litros_por_carro.append(litros)
    custo_por_carro.append(custo)
    
    # Formatação exata como no exemplo
    print(f"{i+1} - {modelos[i]:<10} - {consumo[i]:>5} - {litros:>6.1f} litros - R$ {custo:.2f}")

# Encontra o carro mais econômico (maior km/l)
indice_mais_economico = consumo.index(max(consumo))
carro_mais_economico = modelos[indice_mais_economico]

print(f"O menor consumo é do {carro_mais_economico}.")