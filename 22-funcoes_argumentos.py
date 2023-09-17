# 1 - Crie uma função que receba dois argumentos: o primeiro nome e o segundo nome

def fullName(str1, str2):
    print(f"Nome completo: {str1} {str2}")

fullName("Arthur","dos Santos")

# 2 - crie uma função que some dois numeros via parametros
def soma(v1, v2):
    soma = v1+v2
    print(f"A soma de {v1} + {v2} = {soma} ")

soma(1, 2)

# 3 - Argumentos default numa função
def adress(country="Brasil"):
    print(f"Eu moro no {country}")

adress()
adress('Canadá')

# 4 - Avalização do jogo
def rating_game(qtdRating):
    game_name = input("Digite o nome do jogo\n")
    sum = 0
    for i in range(qtdRating):
        note = float(input("Digite a nota para o jogo\n"))
        sum += note
    print(f"Média de avaliação do jogo {game_name} é: {sum/qtdRating:.2f}")

rating = int(input('digite quantas avaliações deseja fazer: '))
rating_game(rating)