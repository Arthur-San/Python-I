gameName = 'Fifa23'
gameDescription = '''
Fifa 23 é um jogo de futebol
desenvolvido pela EA Sports
e que possibilita jogar 
localmente ou online.
                '''

gameTest = """
.enilno uo etnemlacol
 ragoj atilibissop euq e
stropS AE alep odivlovnesed
lobetuf ed ogoj mu é 32 afiF
"""

# string [início:fim] - indice na posição 0 | indice final -1

# 1 - Busque toda String a partir da primeira posição 
print(gameName[0:])

# 2 - Busque toda String a partir da última posição posição para antes dela
print(gameName[:3])

# 3 - Busque toda string do índice X até a última posição
print(gameName[2:])

"""
string [início:fim] - indice na posição 0 | indice final -1
passo - determina o incremento. Por padrão esse número é o 1 
"""

# 4 - Busque toda a string de 2 em 2 caracteres
print(gameName[::2])

# 5 - Busque toda a string nos indices ímpares
print(gameName[1::2])

# 6 - Busque toda a string nos indices pares
print(gameName[::2])

# 7 - Inverter uma string de trás para frente
print(gameDescription[::-1])

print(gameTest[::-1])








