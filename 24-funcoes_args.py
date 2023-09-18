"""
*args - utilizamos ele quando não temos certeza de quantos argumentos queremos ter numa função
- Os argumentos são passados como uma tupla

**kwargs - Além dos valores podemos passar também as respectivas chaves para cada argumento
- Os argumentos são passados como dicionário
"""

# 1 - soma de numeros
def sum(*num):
    sum_total = 0
    for x in num:
        print(x)
        sum_total += x
    print(f"Soma é: {sum_total}")

sum(7, 9) 
# sum(7, 9, 10) 
# sum(7, 9, 10, 20) 

linha = '='
print(linha*30)

def presentation(**data):
    for key, value in data.items():
        print(f"{key} - {value}")



print("###CURSO###")
print(linha*30)

presentation(name="Python", category="Backend", level="Iniciante") 
print(linha*30)

presentation(name="Python", category="IA", level="Avançado")
print(linha*30)

presentation(name="Dashboard", category="Data Science", level="Intermediário")
print(linha*30)

