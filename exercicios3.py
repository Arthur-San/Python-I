## Cálculo da Distância

# Escreva um programa que pergunte a distância que um passageiro deseja percorrer em km.
# Calcule o preço da passagem, cobrando R$ 0,50 por km para viagens de até de 200 km, e R$
# 0,35 para viagens mais longas.

# distancia = float(input('Qual a distância? (em KM): '))

# if distancia <= 200.00:
#     passagem = distancia * 0.5
# elif distancia >200.00:
#     passagem = distancia * 0.35
# else:
#     print('Valor inválido')
    

# print(f"A passagem ficou: R$ {passagem}")
    
## Aumento salário funcionário

# Escreva um programa que pergunte o salário do funcionário e calcule o valor do aumento. Para
# salários superiores a R$ 1.250,00, calcule um aumento de 10%. Para os inferiores ou iguais, de
# 15%.

salario = float(input('Qual o seu salário? '))

if salario > 1250.00:
    salario += salario * 0.10
    print(f"Novo salário: R$ {salario:.2f} - 10% de aumento")
elif salario <= 1250.00:
    salario += salario * 0.15
    print(f"Novo salário: R$ {salario:.2f} - 15% de aumento")
else:
    print('valor inválido')




