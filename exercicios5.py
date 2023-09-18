

## Conta letras maiúsculas e minúsculas
# Escreva uma função Python que receba uma string e conte o número de letras maiúsculas e minúsculas desta string.
linha = '='

#FORMA QUE PENSEI PRIMEIRAMENTE
# print(linha*30)
# print("Conta letras maiúsculas e minúsculas:\n")
# def contarCaractMaiusc(str1):
#     print(f"Caracter: {str1}")
#     qtdCarac = 0

#     for x in str1:
#         if x.isupper():
#             qtdCarac += 1
#     print(qtdCarac)

# contarCaractMaiusc("ArtHur É Um TesTe")

#ou FORMA QUE DA PARA FAZER COM DICIONÁRIO
print(linha*30)

def checarCaracter(texto):
    tipo = {"UpperCase": 0, "LowerCase": 0}

    for char in texto:
        if char.isupper():
            tipo['UpperCase'] += 1
        elif char.islower():
            tipo['LowerCase'] += 1

    print(f"Maiúsculas {tipo['UpperCase']}")
    print(f"Minúsculas {tipo['LowerCase']}")
    print(f"Quantidade de caracteres ao total: {tipo['LowerCase'] + tipo['UpperCase']}")

checarCaracter("Texto Testado Para fazer texto")

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
            pares.append(x)
        else:
            impares.append(x)
    print('Pares: ',pares)
    print('impares: ',impares)

verificarNumero(numbers)




