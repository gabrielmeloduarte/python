def valor_pagamento(valor_prestacao, dias_atraso):
    """
    Calcula o valor a ser pago de uma prestação com base nos dias de atraso.
    - Sem atraso: valor normal
    - Com atraso: valor + 3% de multa + 0.1% de juros por dia atrasado
    """
    if dias_atraso == 0:
        return valor_prestacao
    else:
        multa = valor_prestacao * 0.03
        juros = valor_prestacao * 0.001 * dias_atraso
        return valor_prestacao + multa + juros


def main():
    print("Sistema de Pagamento de Prestações")
    print("=" * 40)
    
    total_pago = 0.0
    quantidade = 0
    
    while True:
        try:
            valor = float(input("\nDigite o valor da prestação (ou 0 para sair): R$ "))
            
            if valor == 0:
                break
                
            if valor < 0:
                print("Valor inválido! Digite um número positivo.")
                continue
                
            dias = int(input("Digite o número de dias em atraso: "))
            
            if dias < 0:
                print("Dias em atraso não podem ser negativos!")
                continue
                
            # Calcula o valor final
            valor_final = valor_pagamento(valor, dias)
            
            # Exibe o resultado
            print(f"Valor a ser pago: R$ {valor_final:.2f}")
            
            # Acumula para o relatório
            total_pago += valor_final
            quantidade += 1
            
        except ValueError:
            print("Entrada inválida! Digite apenas números.")
    
    # Relatório final
    print("\n" + "=" * 40)
    print("RELATÓRIO DO DIA")
    print("=" * 40)
    if quantidade > 0:
        print(f"Quantidade de prestações pagas: {quantidade}")
        print(f"Valor total recebido no dia: R$ {total_pago:.2f}")
    else:
        print("Nenhuma prestação foi registrada hoje.")
    print("Programa encerrado. Até logo!")


# ========================================
# Executar o programa
# ========================================
if __name__ == "__main__":
    main()