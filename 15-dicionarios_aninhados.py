import pprint

line = '='
print(line*30)

gamesDicts = {
    "resident evil 4" : {
        "yearLauch" : 2003,
        "classification" : 9.3,
        "genre" : ["Ação", "aventura"]
    },

    "Zelda" : {
        "yearLauch" : 1998,
        "classification" : 8.9,
        "genre" : ["puzzle", "aventura"]
    },

    "GTA San Andreas" : {
        "yearLauch" : 2011,
        "classification" : 9.7,
        "genre" : ["Máfia", "Roly Play"]
    }

}

pp = pprint.PrettyPrinter(depth=4)
pp.pprint(gamesDicts)

# 1 - Buscar informação dentro de um dicionário aninhado
print(line*30)
print(gamesDicts["Zelda"]["genre"])

# 2 - adicionar novo dicionario
gamesDicts["Bomba petch"] = {
        "yearLauch" : 2025,
        "classification" : 10,
        "genre" : ["Futebol", "Bomba"]
    }

# 3 - Adicionar novo item em um dicionário
print(line*30)
gamesDicts["Bomba petch"]["genre"] = 1
print(gamesDicts["Bomba petch"])
print(type(gamesDicts["Bomba petch"])) 

# 4 - excluir um dicionario
print(line*30)
del gamesDicts["GTA San Andreas"]
pp.pprint(gamesDicts)
