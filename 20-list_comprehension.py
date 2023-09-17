# 1 - Liste valores de 0 a 10 que sejam menor do que 4
# for i in range(10):
#     if(i < 4):
#         print(i)
#     elif(i > 4):
#         print("valor maior")
#     else:
#         print("valor invalido")

#compreheinsion
listNumbers = [i for i in range(10) if i < 4] 
print(listNumbers)

gamesList = ["Mario", "Sonic", "Zelda", "Mortal Kombat"]

# 2 - Jogos que possuam a letra "A"
newList = [x for x in gamesList if "M" in x]
print(newList)

# 3 - jogos que eu zerei
gamesFinished = [x for x in gamesList if x != "Zelda"]
print(gamesFinished)

