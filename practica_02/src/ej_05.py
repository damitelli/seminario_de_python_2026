def calculadora_costo_de_envio():
    tarifas = {
        "local":    {"hasta_1": 500,  "1_a_5": 1000, "mas_5": 2000},
        "regional": {"hasta_1": 1000, "1_a_5": 2500, "mas_5": 5000},
        "nacional": {"hasta_1": 2000, "1_a_5": 4500, "mas_5": 8000}
    }

    peso = float(input("Ingrese el peso del paquete (kg): "))
    while peso < 0:
         peso = float(input("Ingrese un peso mayor a 0: "))

    zona = input("Ingrese la zona del zona (local/regional/nacional):").lower().strip()
    while not zona in tarifas:
         zona = input(
             "Zona no válida. " \
             "Las zonas disponibles son: local, regional, nacional. :"
             ).lower().strip()
    
    if peso < 1:
        rango = "hasta_1"
    elif peso > 5:
        rango = "mas_5"
    else:
        rango = "1_a_5"

    print(f"Costo de envío: {tarifas[zona][rango]}")
            