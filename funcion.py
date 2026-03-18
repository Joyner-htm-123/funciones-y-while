A = [2,7,11,20,31,40,52,70]
izq = 0
der = len(A) - 1

n = int(input("Ingresa un numero: "))
encontro = False

while izq <= der:
    cen = (izq + der)//2
    
    if A[cen] == n:
        encontro = True
        break
    
    elif A[cen] < n:
        izq = cen + 1
    else:
        der = cen - 1

if encontro:
    print("Encontrado en la posición:", cen)
else:
    print("No se encontró el numero.") 