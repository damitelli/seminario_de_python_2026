def duracion_de_una_playlist():
    playlist = [
    {"title": "Bohemian Rhapsody", "duration": "5:55"},
    {"title": "Hotel California", "duration": "6:30"},
    {"title": "Stairway to Heaven", "duration": "8:02"},
    {"title": "Imagine", "duration": "3:07"},
    {"title": "Smells Like Teen Spirit", "duration": "5:01"},
    {"title": "Billie Jean", "duration": "4:54"},
    {"title": "Hey Jude", "duration": "7:11"},
    {"title": "Like a Rolling Stone", "duration": "6:13"},
    ]
    
    minutes = 0
    seconds = 0

    d_max = -1
    d_min = 999
    s_max = {}
    s_min = {}

    for song in playlist:
        duration = song["duration"].split(':')
        minutes += int(duration[0])

        if seconds > 60:
            seconds = (seconds - 60) + int(duration[1])
            minutes += 1
        else: 
            seconds += int(duration[1])

        d_to_check = (int(duration[0]) * 60) + int(duration[1])

        if d_to_check > d_max:
            d_max = d_to_check
            s_max = song
        elif d_to_check < d_min:
            d_min = d_to_check
            s_min = song

    print(f"Duración total: {minutes}m {seconds}s")
    print(f'Canción más larga: {s_max["title"]} ({s_max["duration"]})')
    print(f'Canción más corta: {s_min["title"]} ({s_min["duration"]})')