# suma básica con py
valor1 = 7
valor2 = 4

resultado = valor1 + valor2
print(resultado)

# resta básica con py
valor1 = 7
valor2 = 4

resultado = valor1 - valor2
print(resultado)

# multiplcación básica con py
valor1 = 7
valor2 = 4

resultado = valor1 * valor2
print(resultado)

# división básica con py
valor1 = 7
valor2 = 4

resultado = valor1 / valor2
print(resultado)

# Calculadora con py
num1 = int(input("Ingrese un número: "))
operador = input("Ingrese un operador: ")
num2 = int(input("Ingrese otro número: "))

if operador == "+":
  resultado = num1 + num2
elif operador == "-":
  resultado = num1 - num2
elif operador == "*":
  resultado = num1 * num2
elif operador == "/":
  resultado = num1 / num2

print(resultado)
