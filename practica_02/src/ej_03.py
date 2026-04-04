import re
import textwrap

def filtro_de_spoilers():
    review = """La película sigue a un grupo de astronautas que
    viajan a Marte
    en una misión de rescate. El capitán Torres lidera al equipo
    a través
    de tormentas solares y fallos en el sistema de navegación. Al
    llegar
    a Marte descubren que la base está abandonada y los
    suministros
    destruidos. Torres decide sacrificar la nave nodriza para
    salvar
    al equipo y logran volver a la Tierra en una cápsula de
    emergencia.
    El final revela que Torres sobrevivió gracias a un pasaje
    secreto."""

    clean_review = " ".join(review.split())

    spoilers = input("Ingrese las palabras spoiler (seperadas por coma): ")
    spoilers = spoilers.lower().split(',')

    # Crea un patron de palabras para comparar. "|" se usa como disjuncion
    # re.escape convierte comandos en texto
    spoiler_patron = "|".join(re.escape(spoiler) for spoiler in spoilers)

    # La función lambda crea tantos "*" como letras tenga la palabra encontrada
    # Uso de re.sub con flag re.IGNORECASE para ignorar mayusculas
    spoiler_free = re.sub(
        spoiler_patron, lambda m: "*" * len(m.group()), clean_review,
        flags=re.IGNORECASE)

    ready_text = textwrap.fill(spoiler_free, width=70)
    print(ready_text)