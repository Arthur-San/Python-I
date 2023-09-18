

## Conta letras maiúsculas e minúsculas
# Escreva uma função Python que receba uma string e conte o número de letras maiúsculas e minúsculas desta string.
linha = '='
print(linha*30)
print("Conta letras maiúsculas e minúsculas:\n")
def contarCaractMaiusc(str1):
    print(f"Caracter: {str1}")
    qtdCarac = 0

    for x in str1:
        if x.isupper():
            qtdCarac += 1
    print(qtdCarac)

contarCaractMaiusc("ArtHur É Um TesTe")
print(linha*30)

## Lista números pares e ímpares de uma lista
# Escreva uma função Python para imprimir os números pares e ímpares em duas listas separadas para cada uma.
print("Lista números pares e ímpares de uma lista:\n")
numbers = [20, 30, 2, 1, 7, 6, 9, 0, 5]

pares = []
impares = []

def verificarNumero(numbers):
    for x in numbers:
        if x %2==0:
            pares.insert(x, x)
        else:
            impares.insert(x, x)
    print('Pares: ',pares)
    print('impares: ',impares)

verificarNumero(numbers)




