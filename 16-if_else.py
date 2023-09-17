name = input('digite o nome do jogo: \n')
yearLauch = int(input('digite o ano do lançamento: \n'))
classification = float(input('digite a nota de classficacao: '))

if classification > 8.0:
    print(f"O jogo {name} é bom, recomendo")
else:
    print(f"O jogo {name} Não é bom")
