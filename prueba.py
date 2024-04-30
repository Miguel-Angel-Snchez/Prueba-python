def calcular_promedio(lista):
    suma = 0
    for num in lista:
        suma += num
    promedio = suma / len(lista)
    return promedio  # Error de ortografía en 'return'

numeros = [1, 2, 3, 4, 5]
print("El promedio es:", calcular_promedio(numeros))  # Error de llamada a función (typo en el nombre de la función)

if 10 > 5:  # Error de estilo: No se usa paréntesis alrededor de la condición
    print("Diez es mayor que cinco")

variable_no_usada = 10  # Error de estilo: Variable definida pero nunca usada
