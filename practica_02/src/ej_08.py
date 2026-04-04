def cifrado_cesar():

    def cifrar(texto,desplazamiento):
        texto_cifrado = ""
        for char in texto:
            if char.isalpha():
                base = ord('A') if char.isupper() else ord('a')
                # Calcula el caracter correspondiente al desplazamiento
                char_cifrado = chr(
                    ((ord(char) - base + desplazamiento) % 26) + base)
                texto_cifrado += char_cifrado
            else:
                texto_cifrado += char
        return texto_cifrado
    
    texto_a_cifrar = input('Ingrese un mensaje: ')

    while True:
        clave = input('Ingrese el desplazamiento: ')
        if clave.isdigit():
            clave = int(clave)
            break
        else:
            print('Ingrese un número entero.')

    cifrado = cifrar(texto_a_cifrar,clave)
    print(f'Mensaje cifrado: {cifrado}')
    
    # Invierte la clave para hacer la operacion inversa
    descifrado = cifrar(cifrado, -clave)
    print(f'Mensaje descifrado: {descifrado}')