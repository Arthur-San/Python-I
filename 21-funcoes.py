# 1 - função para imprimir teste
def wellcome():
    print('teste')

wellcome()

# 2 - somar dois numeros
def sum():
    return 5 + 4

print(sum())

# 3 - cadastrar um jogo 
def create_game():
    name = input('digite o nome do jogo: \n')
    yearLauch = int(input('digite o ano do lançamento: \n'))
    gamePrice = float(input('digite o preço do jogo: \n'))
    noteRating = float(input('Digite a nota de avaliação do jogo: '))

    print(f"{name} - R${gamePrice}")

create_game()



