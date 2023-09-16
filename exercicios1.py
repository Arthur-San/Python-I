## Antecessor e Sucessor de um número
# Escreva um programa em Python que leia um número e represente o número antecessor e sucessor desse # número que foi lido, utilizando operadores de atribuição.

valor = int(input('Digite um valor\n'))

print(f"Antecessor: {valor - 1}\nSucessor: {valor - 2}")

## Média de 4 notas
#Escreva um programa em Python que leia quatro números e calcule a média entre esses números
nota1 = int(input("digite a nota 1:\n"))
nota2 = int(input("digite a nota 2:\n"))
nota3 = int(input("digite a nota 3:\n"))
nota4 = int(input("digite a nota 4:\n"))

soma = nota1 + nota2 + nota3 + nota4

media = soma / 4

print(f'A média das notas é: {media}')