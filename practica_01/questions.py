import random

ERR_MESSAGE = "\nLa entrada no es un número entero.\n"

categorias = {
    "Lenguajes": ["python"],
    "Conceptos de programación": ["programa", "variable", "funcion", "bucle"],
    "Tipos de datos": ["cadena", "entero", "lista"]
}

valid_cat = False
termino = False

puntaje_total = 0
guessed = []

print("¡Bienvenido al Ahorcado!")
print()

text_cat = '''Categorías disponibles:
1 - "Lenguajes"
2 - "Conceptos de programación"
3 - "Tipos de datos"
'''

while not valid_cat:
    try:
        print(text_cat)
        cat = int(input("Elegí un numero del 1 al 3 para comenzar: "))
        
        # Verifica la elección. Si es valida, reasigna la variable a la
        # clave del diccionario correspondiente
        if cat in range(1,4):
            match cat:
                case 1:
                    cat = "Lenguajes"
                case 2:
                    cat = "Conceptos de programación"
                case 3:
                    cat = "Tipos de datos"
            valid_cat = True
        else:
            print("\nLa entrada no pertenece a una categoría existente.\n")
            
    except ValueError:
        print(ERR_MESSAGE)
        
list_u = random.sample(categorias[cat],len(categorias[cat]))

while not termino and len(list_u) > 0:
    word = random.choice(list_u)
    list_u.remove(word)

    attempts = 6

    while attempts > 0:
        # Mostrar progreso: letras adivinadas y guiones para las que faltan
        progress = ""
        for letter in word:
            if letter in guessed:
                progress += letter + " "
            else:
                progress += "_ "
        print(progress)

        # Verificar si el jugador ya adivinó la palabra completa
        if "_" not in progress:
            print("¡Ganaste!")
            break
        
        print(f"Intentos restantes: {attempts}")
        print(f"Letras usadas: {', '.join(guessed)}")

        letter = input("Ingresá una letra: ")

        if len(letter) == 1 and letter.isalpha():
            if letter in guessed:
                print("Ya usaste esa letra.")
            elif letter in word:
                guessed.append(letter)
                print("¡Bien! Esa letra está en la palabra.")
            else:
                guessed.append(letter)
                attempts -= 1
                print("Esa letra no está en la palabra.")

            print()

        else:
            print("Entrada no válida")

    else:
        print(f"¡Perdiste! La palabra era: {word}")

    print(f"Puntaje: {attempts}")
    puntaje_total += attempts

    if len(list_u) > 0: 
        valid_choice = False
        print()

        while not valid_choice:
            try:
                print("Seguir jugando? \n \n 1 - Sí \n 2 - No \n")
                choice = int(input("Tu respuesta: "))
                
                if choice in range(1,3):
                    if choice == 1:
                        guessed.clear()
                        print("¡Siguiente ronda!")
                    else:
                        termino = True    
                    valid_choice = True

                else:
                    print("Entrada invalida")
            
            except ValueError:
                print(ERR_MESSAGE)
    else:
        termino = True
        print()
        print("¡La categoría ya no tiene palabras, el juego ha terminado!")
    print(f"Puntaje total: {puntaje_total}")      