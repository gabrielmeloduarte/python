def leet_speak(texto):
    # Mapeamento de letras para versões leet (várias opções por letra)
    leet_dict = {
        'a': ['4', '@', '/\\', '^'],
        'b': ['8', '|3', 'ß'],
        'c': ['(', '[', '<'],
        'd': ['|)', '[)'],
        'e': ['3'],
        'f': ['|=', 'ph'],
        'g': ['6', '9'],
        'h': ['#', '|-|', '}{'],
        'i': ['1', '!', '|', ']['],
        'j': [']', '¿'],
        'k': ['|<', '|{'],
        'l': ['1', '£', '|'],
        'm': ['|\\/|', '^/^^\\'],
        'n': ['|\\|', '/\\/'],
        'o': ['0', '()', '[]'],
        'p': ['|*', '|o'],
        'q': ['9', '(_,)'],
        'r': ['|2', '12'],
        's': ['5', '$', 'z'],
        't': ['7', '+', '-|-'],
        'u': ['|_|', 'v'],
        'v': ['\\/', '√'],
        'w': ['\\/\\/', 'uu', 'vv'],
        'x': ['%', '><', '}{'],
        'y': ["'/", 'j'],
        'z': ['2', 'z']
    }

    texto = texto.lower()
    resultado = []

    for letra in texto:
        if letra in leet_dict:
            # Escolhe uma substituição aleatória para variar o leet
            import random
            substituta = random.choice(leet_dict[letra])
            resultado.append(substituta)
        elif letra.isspace():
            resultado.append(' ')  # mantém espaços
        else:
            resultado.append(letra)  # mantém símbolos, números, etc.

    return ''.join(resultado)

# === PROGRAMA PRINCIPAL ===
print("=" * 50)
print("   L33T 5P34K G3N3R4T0R - H4CK3R M0D3 0N")
print("=" * 50)

while True:
    texto = input("\nDigite o texto para converter para Leet Speak (ou 'sair' para encerrar):\n> ")
    
    if texto.strip().lower() == 'sair':
        print("F4r3w3ll, h4x0r!")
        break
    
    if texto.strip() == "":
        print("Digite algo, seu n00b!")
        continue

    leet_texto = leet_speak(texto)
    print("\nResultado Leet:")
    print(f"→ {leet_texto}")
    print("-" * 50)