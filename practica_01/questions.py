import random

categorias = {
    "Lenguajes": ["python"],
    "Conceptos de programación": ["programa", "variable", "funcion", "bucle"],
    "Tipos de datos": ["cadena", "entero", "lista"]
}

guessed = []
attempts = 6

print("¡Bienvenido al Ahorcado!")
print()

cat = int(input( 
'''Categorías disponibles: 
1 - "Lenguajes" 
2 - "Conceptos de programación"
3 - "Tipos de datos":

Elegí un número del 1 al 3 para comenzar: '''))

match cat:
    case 1:
        cat = "Lenguajes"
    case 2:
        cat = "Conceptos de programación"
    case 3:
        cat = "Tipos de datos"
    

word = random.choice(categorias[cat])

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