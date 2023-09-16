gameMK = {
    "name": "Mortal kombat",
    "lancamento": 2022,
    "preco": 90.50,
    "classificacao": 8.5
    }

print(gameMK)
print(len(gameMK))
print(type(gameMK))

# 1 - reccuperar um elemento do dicionário
print(gameMK["name"])
print(gameMK.get("name"))

# 2 - Buscar apenas as chaves do dicionário
print(gameMK.keys() )

# 3 - Buscar apenas as valores do dicionário
print(gameMK.values() )

# 4 - Buscar itens do dicionario com chave e valor
print(gameMK.items())

# 5 - Adicionar itens no dicionario
gameMK ["players"] = 2
print(gameMK)

# 6 - atualizar itens no dicionario
gameMK.update({"players" : 1})
print(gameMK)

# 7 - Remover itens no dicionario
gameMK.pop("players")
print(gameMK)

