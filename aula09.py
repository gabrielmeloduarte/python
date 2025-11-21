import random

def embaralha_palavra(palavra):
    """
    Recebe uma string e retorna outra com os caracteres embaralhados aleatoriamente.
    Todos os caracteres são convertidos para MAIÚSCULA.
    
    Exemplo: 'python' → 'NPTHYO', 'PyThOn' → 'TONYHP'
    """
    # Converte tudo para maiúscula (ou use .lower() se preferir minúscula)
    palavra = palavra.upper()
    
    # Converte a string em lista (pois strings são imutáveis)
    letras = list(palavra)
    
    # Embaralha a lista
    random.shuffle(letras)
    
    # Junta de volta em uma string e retorna
    return ''.join(letras)


# ========================================
# TESTE DA FUNÇÃO
# ========================================
if __name__ == "__main__":
    print("Embaralhador de Palavras")
    print("-" * 30)
    
    while True:
        entrada = input("\nDigite uma palavra (ou 'sair' para encerrar): ").strip()
        
        if entrada.lower() in ["sair", "exit", "quit", ""]:
            print("Até logo!")
            break
            
        if not entrada.isalpha():
            print("Por favor, digite apenas letras!")
            continue
        
        resultado = embaralha_palavra(entrada)
        print(f"Palavra original: {entrada.upper()}")
        print(f"Palavra embaralhada: {resultado}")
        print(f"→ Cada vez que você digitar a mesma palavra, o resultado será diferente!")