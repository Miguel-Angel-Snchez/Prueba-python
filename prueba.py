def calcular_promedio(lista):
    try:
        suma = 0
        for num in lista:
            suma += num
        promedio = suma / len(lista)
        return promedio
    except ZeroDivisionError:
        print("Error por que la lista esta vacia")
        return None
    except TypeError:
        print("La lista incluye elementos no numericos")
        return None

#numeros = [1, 2, 3, 4, 5]
numeros = []
promedio = calcular_promedio(numeros)
if promedio is not None:
    print("El promedio es:", promedio)

if 10 > 5:
    print("Diez es mayor que cinco")
    print("Diez es mayor que cinco")
    print("Diez es mayor que cinco")
    print("Diez es mayor que cinco")
    print("Diez es mayor que cinco")

variable_no_usada = 10
