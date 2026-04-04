import random

def sorteo_amigo_invisible():
    while True:
        participantes = input("Ingrese una lista de participantes separados por coma: ")
        # Crea lista de nombre, eliminando espacios y nombres vacios
        participantes = list(name.strip() for name in participantes.split(",") if name.strip())
        # Crea una lista de un set previniendo duplicados y formateando nombres
        participantes = list({name.lower().capitalize() for name in participantes})
        if len(participantes) > 2:
            break
        else: 
            print('Debe haber al menos tres participantes.')

    random.shuffle(participantes)
    asignaciones = {}

    for indice, participante in enumerate(participantes):
        # Impide que se asigne a sí mismo
        asignaciones[participante] = participantes[(indice + 1) % len(participantes)]

    for key, value in asignaciones.items():
        print(f'{" "*2} {key} --> {value}')