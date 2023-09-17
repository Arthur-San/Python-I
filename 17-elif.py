valor1 = float(input('digite o valor 1: '))
valor2 = float(input('digite o valor 2: '))
operation = input('Digite a operação que deseja realizar (+ - * /)\n ')

if operation == "+":
    result = valor1 + valor2

elif operation == "-":
    result = valor1 - valor2

elif operation == "*":
    result = valor1 * valor2

elif operation == "/":
    result = valor1 / valor2

else:
    print('operação inválida')
    result = 0

print(f"O resultado é: {result:.2f}")
