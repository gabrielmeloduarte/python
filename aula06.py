def corrigir_telefone():
    print("Valida e corrige número de telefone")
    
    # Lê o telefone do usuário
    telefone = input("Telefone: ").strip()
    
    # Remove o traço (se existir) e mantém apenas os dígitos
    digitos = telefone.replace("-", "")
    
    # Verifica se ficou apenas com números
    if not digitos.isdigit():
        print("Erro: Por favor, digite apenas números e traço (se quiser).")
        return
    
    # Verifica a quantidade de dígitos
    if len(digitos) == 7:
        print("Telefone possui 7 dígitos. Vou acrescentar o dígito três na frente.")
        digitos = "3" + digitos
    elif len(digitos) == 8:
        print("Telefone já possui 8 dígitos.")
    else:
        print(f"Tamanho inválido! O telefone deve ter 7 ou 8 dígitos (você digitou {len(digitos)}).")
        return
    
    # Formata com traço (4 dígitos - 4 dígitos)
    telefone_formatado = digitos[:4] + "-" + digitos[4:]
    
    # Exibe os resultados
    print(f"Telefone corrigido sem formatação: {digitos}")
    print(f"Telefone corrigido com formatação: {telefone_formatado}")

# ========================================
# Executa o programa
# ========================================
if __name__ == "__main__":
    corrigir_telefone()