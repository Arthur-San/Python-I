# Exemplo de concatenação de strings em Python

# 1. Concatenando strings usando o operador '+'
primeiro_nome = "João"
sobrenome = "Silva"
nome_completo = primeiro_nome + " " + sobrenome
print("1. Usando o operador '+':")
print("Nome completo:", nome_completo)

# 2. Concatenando strings com espaços em branco
cidade = "Nova York"
estado = "Nova York"
endereco = cidade + ", " + estado
print("\n2. Concatenando com espaços em branco:")
print("Endereço:", endereco)

# 3. Concatenando strings com números
idade = 30
mensagem = "Eu tenho " + str(idade) + " anos."
print("\n3. Concatenando com números:")
print(mensagem)

# 4. Concatenando strings com variáveis formatadas (Python 3.6+)
produto = "computador"
preco = 1200.50
descricao = f"O {produto} custa R${preco:.2f}."
print("\n4. Concatenando com variáveis formatadas:")
print(descricao)

# 5. Concatenando strings usando o método join()
frutas = ["maçã", "banana", "laranja"]
lista_de_frutas = ", ".join(frutas)
print("\n5. Usando o método join():")
print("Frutas:", lista_de_frutas)

# 6. Concatenando várias strings com operador '+'
mensagem_longa = "Esta é uma mensagem muito longa que será " + \
                 "concatenada usando o operador '+' em várias linhas."
print("\n6. Concatenando várias strings com operador '+':")
print(mensagem_longa)
