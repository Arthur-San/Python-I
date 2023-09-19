# ## Gerenciamento de Jogadores e Times

# Escreva um programa em python que realize o gerenciamento de jogadores. Ele deve atender aos seguintes requisitos:

# - Adicionar um time
# - Remover um time
# - Listar times
# - Adicionar jogador em um time
# - Remover jogador de um time
# - Listar jogadores de um time

# 1. A opção de listar os times deve mostrar o índice, o nome e a quantidade de jogadores do time.
# 2. A opção de adicionar um time deve pedir um nome para o time que será cadastrado.
# 3. A opção de remover um time deve pedir o índice específico do time que foi cadastrado para fazer a sua exclusão.
# 4. A opção de adicionar um jogador em um time deve pedir um índice do time que foi cadastrado e associar com o nome do jogador que será adicionado.
# 5. A opção de remover um jogador em um time deve pedir um índice do time que foi cadastrado e utilizar esse índice para remover o jogador que fora cadastrado no time.
# 6. A opção de listar os jogadores de um time deve ser informado o índice de um time e listar os jogadores que foram associados a ele.

# Este é o exercício de revisão do módulo, então aproveite para utilizar todos os recursos vistos até agora, como os funções, condições, loop, listas, etc.

import pprint
pp = pprint.PrettyPrinter(depth=4)

linha = '=' #FRUFRU de deixar o menu mais bonito :D

#LIST dos times 
times = {}

cont = 0
indiceJog = 0

#variável para validar qual função será executada!
option = -1

def adicionaTime(times):
    global cont  # Declarado cont como global para que possa ser atualizado

    nomeTime = input('Qual o nome do time?\n')

    times[nomeTime] = {
        "indice" : cont,
        "jogadores" : []
    }
    

    print(f"Time {nomeTime.upper()} adicionado!")

    cont += 1  # Atualiza o valor de cont globalmente

def removerTime(times):
    while removerTime != 0:
        print("Qual time deseja remover? ")
        pp.pprint(f"Times cadastrados: {times}")
        timeRemover = input()

        if timeRemover in times:
            del times[timeRemover]
            print(f"Time ->{timeRemover.upper()}<- removido!")
            break
        else:
            print('Time não existe!\nVerifique novamente os times cadastrados!\n')
            print(linha*30)

    
        
    print(linha*30)

def listarTimes(times):

    print(times)

def adicionarJogador(times):
    global indiceJog
    print('Em qual time deseja adicionar? \n', times)
    selecionaTime = input()

    nomeJogador = input('Qual o nome do jogador?')
    
    times[selecionaTime]["jogadores"] = {
        indiceJog : "indice",
        "nome" : nomeJogador
    }

    indiceJog += 1






while option != '0':
    print(linha*15 , " MENU ", linha*15)
    print("""
Escolha uma opção
          
1 - Adicionar Time
2 - Remover Time
3 - Listar Times
4 - Adicionar Jogador          
0 - Sair
          """)
    
    option = input('->')
    
    if option == '1':
        adicionaTime(times)
    
    elif option == '2':
        removerTime(times)
    
    elif option == '3':
        listarTimes(times)
    
    elif option == '4':
        adicionarJogador(times)
    
    elif option == '0':
        print("programa encerrado!")

    #valores difentes dos informados será redirecionado para escolher um existente 
    else: 
        print('Valor inválido! Tente novamente!')
        option = -1
