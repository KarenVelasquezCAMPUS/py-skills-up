# Encontrar el número mayor de una lista de números en un array

numeros = [5, 10, 15, 60, 8]
numero_maximo = 0

for numero in numeros:
    if numero > numero_maximo:
        numero_maximo = numero

print(numero_maximo)

# Encontrar el número mayor de una lista de números en un array | Con funcion de py

numeros = [5, 10, 15, 60, 8]
maximo = max(numeros)
print(maximo)
