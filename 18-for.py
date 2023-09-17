gameList = ["fifa", "God of war", "Read dead 2", "uncharted", 90.50]

line = '='


# 1 - iterando valores de uma lista
# for game in gameList:
#     print(game)

# 2 - Quando a condição for atendida, o loop será encerrado 
for game in gameList:
    if game == "Read dead 2":
        break
    print(game)

print(line*30)

# 3 - Quando a condição for atendida, o loop vai para a próxima iteração
for game in gameList:
    if game == "Read dead 2":
        continue
    print(game)

print(line*30)

# 4 - avaliação de jogo
# for i in range(5):
#     print('ttsssss pitonnnnn')
gameName = input('digite o nome do jogo\n')
gameRating = int(input('Quantsa avaliações deseja fazer no jogo?\n'))

sum = 0
for i in range(gameRating):
    note = float(input('Digite a nota para o jogo: '))
    sum += note
print(f"Média de avaliação do jogo {gameName} é {sum/gameRating:.2f}")
