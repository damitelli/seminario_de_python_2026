def simulación_de_competencia_de_cocina_y_ranking():
    rounds = [
        {
            'theme': 'Entrada',
            'scores': {
                'Valentina': {'judge_1': 8, 'judge_2': 7, 'judge_3': 9},
                'Mateo': {'judge_1': 7, 'judge_2': 8, 'judge_3': 7},
                'Camila': {'judge_1': 9, 'judge_2': 9, 'judge_3': 8},
                'Santiago': {'judge_1': 6, 'judge_2': 7, 'judge_3': 6},
                'Lucía': {'judge_1': 8, 'judge_2': 8, 'judge_3': 8},
            }
        },
        {
            'theme': 'Plato principal',
            'scores': {
                'Valentina': {'judge_1': 9, 'judge_2': 9, 'judge_3': 8},
                'Mateo': {'judge_1': 8, 'judge_2': 7, 'judge_3': 9},
                'Camila': {'judge_1': 7, 'judge_2': 6, 'judge_3': 7},
                'Santiago': {'judge_1': 9, 'judge_2': 8, 'judge_3': 8},
                'Lucía': {'judge_1': 7, 'judge_2': 8, 'judge_3': 7},
            }
        },
        {
            'theme': 'Postre',
            'scores': {
                'Valentina': {'judge_1': 7, 'judge_2': 8, 'judge_3': 7},
                'Mateo': {'judge_1': 9, 'judge_2': 9, 'judge_3': 8},
                'Camila': {'judge_1': 8, 'judge_2': 7, 'judge_3': 9},
                'Santiago': {'judge_1': 7, 'judge_2': 7, 'judge_3': 6},
                'Lucía': {'judge_1': 9, 'judge_2': 9, 'judge_3': 9},
            }
        },
        {
            'theme': 'Cocina internacional',
            'scores': {
                'Valentina': {'judge_1': 8, 'judge_2': 9, 'judge_3': 9},
                'Mateo': {'judge_1': 7, 'judge_2': 6, 'judge_3': 7},
                'Camila': {'judge_1': 9, 'judge_2': 8, 'judge_3': 8},
                'Santiago': {'judge_1': 8, 'judge_2': 9, 'judge_3': 7},
                'Lucía': {'judge_1': 7, 'judge_2': 7, 'judge_3': 8},
            }
        },
        {
            'theme': 'Final libre',
            'scores': {
                'Valentina': {'judge_1': 9, 'judge_2': 8, 'judge_3': 9},
                'Mateo': {'judge_1': 8, 'judge_2': 9, 'judge_3': 8},
                'Camila': {'judge_1': 7, 'judge_2': 7, 'judge_3': 7},
                'Santiago': {'judge_1': 9, 'judge_2': 9, 'judge_3': 9},
                'Lucía': {'judge_1': 8, 'judge_2': 8, 'judge_3': 7},
            }
        }
    ]

    tabla = {}

    # Obtiene el nombre de los participantes
    participantes = rounds[0]['scores'].keys()

    # Crea la tabla de los partipantes
    for participante in participantes:
        tabla[participante] = {
            "Puntaje" : 0, 
            "Rondas ganadas": 0,
            "Mejor ronda": 0}

    # Cuenta rondas e itera sobre lista de rondas
    num_rounds = 1
    for num_rounds, round in enumerate(rounds, num_rounds):
        print(f"\nRonda {num_rounds} - {round['theme']}")

        # Calcula totales usando diccionario por compresion
        total = {
            cook: sum(score.values())
            for cook, score in round['scores'].items()
        }

        for cook, score in total.items():
            tabla[cook]["Puntaje"] += score
            tabla[cook]["Mejor ronda"] = max(tabla[cook]["Mejor ronda"], score)

        # La funcion lambda determina donde estan los valores a comparar
        winner, score = max(total.items(), key=lambda x: x[1])
        tabla[winner]["Rondas ganadas"] += 1

        print(f"Ganador: {winner} ({score})")

        # Ordena la tabla por puntaje
        sorted_t = sorted(tabla.items(),
                          key=lambda x: x[1]['Puntaje'],
                          reverse=True)
        print()
        print("Tabla de posiciones:")
        for cook, score in sorted_t:
            print(f"{cook + ":":<12} {score['Puntaje']}")


    print("\nTabla de posiciones final:\n")
    print(f"Cocinero{" "*8}Puntaje{" "*4}Rondas ganadas{" "*4}Mejor ronda{
          " "*4}Promedio\n")
    print(f"{"-"*68}")

    for cook, data in sorted_t:
        promedio = data['Puntaje'] / num_rounds
        d1 = f"{cook :<15} {data["Puntaje"]:<10} {data["Rondas ganadas"]:<17}"
        d2 = f"{data["Mejor ronda"]:<14} {promedio:.1f}"
        print (d1, d2)
    print("-"*68)