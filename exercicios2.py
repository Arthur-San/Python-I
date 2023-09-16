gameName = 'fifa 23'
gameDescription = '''
Fifa 23 é um jogo de futebol
desenvolvido pela EA Sports,
e que possibilita jogar 
localmente ou online.
                '''

## Substituindo caractere repetido

# Escreva um programa Python para obter uma string de uma determinada string em que todas as ocorrências de seu primeiro caractere foram alteradas para '$', exceto o próprio primeiro caractere

# Ex:
# fifa 23 → **fi#a 23**
# restart→ resta#t

name = input('digite o nome do jogo: ')

character = name[0].lower()
print(f'caracter selecionado: {character}')
new = name.replace(character, "$")
new = character + new[1:]
print(new)



# Geração de Strings

st1 = 'cab' #zyb
st2 = 'zyx' #cax

new_st1 = st2[:2] + st1[2:]
new_st2 = st1[:2] + st2[2:]
print('novo st1: ', new_st1)
print('novo st2: ', new_st2)
