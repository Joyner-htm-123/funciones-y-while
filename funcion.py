A = [2,7,11,20,31,40,52,70]

continuar = "s"

while continuar == "s":
    izq = 0
    der = len(A) - 1

    encontro = False
    entrada_valida = False

    # Validar número
    while not entrada_valida:
        try:
            n = int(input("Ingresa un numero: "))
            entrada_valida = True
        except:
            print("Error: debes ingresar un número válido.")

    # Búsqueda binaria
    while izq <= der and not encontro:
        cen = (izq + der)//2
        
        if A[cen] == n:
            encontro = True
        elif A[cen] < n:
            izq = cen + 1
        else:
            der = cen - 1

    if encontro:
        print("Encontrado en la posición:", cen)
    else:
        print("No se encontró el numero.")
    
    # Validar continuar
    opcion_valida = False
    while not opcion_valida:
        continuar = input("¿Deseas buscar otro número? (s/n): ").lower()
        
        if continuar == "s" or continuar == "n":
            opcion_valida = True
        else:
            print("Error: solo puedes escribir 's' o 'n'.")

print("Programa finalizado.")
