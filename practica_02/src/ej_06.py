def analisis_de_hasthtag():
    posts = [
        "Arrancando el lunes con energía #Motivación #NuevaSemana",
        "Terminé mi primer proyecto en Python #Python #Programación #OrgullosoDeMi", 
        "No puedo creer el final de la serie #SinSpoilers #SerieAdicta",
        "Nuevo video en el canal sobre #InteligenciaArtificial y #Python",
        "Entrenamiento de hoy completado #Fitness #Motivación #NoPainNoGain",
        "Leyendo sobre #InteligenciaArtificial y el futuro del trabajo #Tecnología",
        "Arranqué a estudiar #Programación por mi cuenta #Python #Autodidacta",
        "Finde de lluvia, maratón de series #SerieAdicta #Relax",
        "Workshop de #InteligenciaArtificial en la universidad #Tecnología #Programación"
    ]
    
    Hashtags = {}
    for post in posts:
        line = post.split()
        for word in line:
            if word.startswith("#"):
                Hashtags[word] = Hashtags.get(word, 0) + 1
    sorted_Hashtag = sorted(Hashtags.items(),
                            key=lambda item: item[1],
                            reverse=True)

    print('Hashtags trending (más de una aparición):')
    for key,value in sorted_Hashtag:
        if value > 1:
            print(f'{" "*2} {key}: {value}')
    print(f'Total de hashtags únicos: {len(sorted_Hashtag)}')