# Programa para calcular o tempo aproximado de download
print("="*50)
print("     CALCULADORA DE TEMPO DE DOWNLOAD")
print("="*50)

# Entrada de dados
tamanho_mb = float(input("Digite o tamanho do arquivo (em MB): "))
velocidade_mbps = float(input("Digite a velocidade da internet (em Mbps): "))

# Cálculo
# 1 Mbps = 0.125 MB/s (porque 1 byte = 8 bits)
velocidade_mb_por_segundo = velocidade_mbps * 0.125

# Tempo em segundos
tempo_segundos = tamanho_mb / velocidade_mb_por_segundo

# Conversões para minutos e segundos (formato mais legível)
tempo_minutos = tempo_segundos // 60
tempo_sobra_segundos = tempo_segundos % 60

# Resultado
print("\n" + "="*50)
print("           RESULTADO")
print("="*50)
print(f"Tamanho do arquivo: {tamanho_mb:.2f} MB")
print(f"Velocidade da conexão: {velocidade_mbps:.2f} Mbps")
print(f"Tempo estimado de download: {tempo_minutos:.0f} minutos e {tempo_sobra_segundos:.1f} segundos")

# Versão alternativa só em minutos (com decimais)
tempo_total_minutos = tempo_segundos / 60
print(f"\nOu aproximadamente: {tempo_total_minutos:.2f} minutos")
print("="*50)