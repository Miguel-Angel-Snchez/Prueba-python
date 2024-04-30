def calcular_promedio(lista):
    try:
        suma = 0
        for num in lista:
            suma += num
        promedio = suma / len(lista)
        return promedio
    except ZeroDivisionError:
        print("Error: La lista está vacía. No se puede calcular el promedio.")
        return None
    except TypeError:
        print("Error: La lista contiene elementos no numéricos.")
        return None

numeros = [1, 2, 3, 4, 5]
promedio = calcular_promedio(numeros)
if promedio is not None:
    print("El promedio es:", promedio)

if 10 > 5:
    print("Diez es mayor que cinco")
    print("Diez es mayor que cinco")
    print("Diez es mayor que cinco")
    print("Diez es mayor que cinco")
    print("Diez es mayor que cinco")

# La siguiente línea genera un aviso en SonarQube por una variable no utilizada
variable_no_usada = 10
