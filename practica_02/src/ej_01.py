def estadisticas_de_un_texto():
    text = """Beautiful is better than ugly.
    Explicit is better than implicit.
    Simple is better than complex.
    Complex is better than complicated.
    Flat is better than nested.
    Sparse is better than dense.
    Readability counts.
    Special cases aren't special enough to break the rules.
    Although practicality beats purity.
    Errors should never pass silently.
    Unless explicitly silenced.
    In the face of ambiguity, refuse the temptation to guess.
    There should be one-- and preferably only one --obvious way to do it.
    Although that way may not be obvious at first unless you're Dutch.
    Now is better than never.
    Although never is often better than *right* now.
    If the implementation is hard to explain, it's a bad idea.
    If the implementation is easy to explain, it may be a good idea.
    Namespaces are one honking great idea -- let's do more of those!"""

    lines = text.splitlines()
    words = text.split()
    tot_lines = len(lines)
    tot_words = len(words)
    promedio = round(tot_words / tot_lines, 2)

    print(f"Total de lineas:  {tot_lines}")
    print(f"Total de palabras:  {tot_words}")
    print(f"Promedio de palabras por línea:  {promedio}")

    print(f"Líneas por encima del promedio ({promedio} palabras): ")
    for line in lines:
        line_words = len(line.split())
        if (line_words > promedio):
            print(f' - "{line}" ({line_words} palabras)')