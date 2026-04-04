def validacion_de_email():
    valid_email = False
    email = input("Ingrese un email: ")
    if email.count('@') == 1:
        if not email.startswith('@') and not email.endswith('.'):
            if not email.startswith('.') and not email.endswith('@'):
                email = email.split('@')
                if len(email[0]) >= 1 and email[1].count('.') >= 1:
                    domain = email[1].split('.')
                    # Revisa la parte del dominio después del último punto
                    if len(domain[-1]) >= 2:
                        valid_email= True
    if valid_email: 
        print('El email es válido.')
    else:
        print('El email no es válido.')