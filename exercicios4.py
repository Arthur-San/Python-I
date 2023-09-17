## Contagem Regressiva
# Faça um programa para escrever a contagem regressiva do lançamento de um foguete. O programa deve imprimir 10, 9, 8, …, 1, 0 e disparar um “beep”.
import winsound

cont = 10

while cont >= 0:
    print(cont)
    cont -= 1

winsound.Beep(2500,500)

## Tabuada
# Faça um programa que calcule a tabuada de um número, com valores iniciais e finais informados pelo usuário
number = int(input('Tabuada de: '))
inicio = int(input('de: '))
fim = int(input('até: '))

x = inicio

while x <= fim:
    print(f"tabuada de {number} x {x} = {number * x}")
    x += 1