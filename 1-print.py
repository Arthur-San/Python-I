# Exemplo simples de uso da função print em Python

# 1. Imprimindo uma string simples
print("Olá, mundo!")

# 2. Imprimindo uma variável
nome = "Alice"
print("Olá,", nome)

# 3. Imprimindo várias variáveis separadas por espaço
idade = 30
cidade = "São Paulo"
print("Nome:", nome, "| Idade:", idade, "| Cidade:", cidade)

# 4. Usando formatação de string (Python 3.6+)
altura = 1.75
print(f"{nome} tem {idade} anos e mede {altura:.2f} metros de altura.")

# 5. Imprimindo em múltiplas linhas
mensagem = """Esta é uma mensagem
que ocupa várias linhas.
Você pode usar três aspas para isso."""
print(mensagem)

# 6. Redirecionando a saída para um arquivo
with open("saida.txt", "w") as arquivo:
    print("Este é um exemplo de saída redirecionada.", file=arquivo)

# 7. Especificando um separador diferente
itens = ["maçã", "banana", "laranja"]
print(*itens, sep=", ")

# 8. Especificando o final de linha
print("Isso será impresso na mesma linha.", end=" ")
print("E isso estará na mesma linha também.")
