# Exemplo de uso da função input em Python

# 1. Recebendo uma entrada de texto
nome = input("Digite seu nome: ")
print(f"Olá, {nome}!")

# 2. Recebendo entrada numérica
idade = int(input("Digite sua idade: "))
print(f"Você tem {idade} anos.")

# 3. Recebendo entrada de flutuante
altura = float(input("Digite sua altura em metros: "))
print(f"Sua altura é {altura:.2f} metros.")

# 4. Recebendo entrada sem prompt
entrada = input()
print(f"Você digitou: {entrada}")

# 5. Avaliando expressões
expressao = eval(input("Digite uma expressão matemática: "))
print(f"O resultado da expressão é: {expressao}")

# 6. Lidando com múltiplas entradas
valores = input("Digite vários valores separados por espaço: ")
lista_valores = valores.split()
print("Valores separados:")
for valor in lista_valores:
    print(valor)
