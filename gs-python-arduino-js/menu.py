from reader import *
from log import *

class Menu:
    
    def mainMenu():
        print('opção 1: iniciar Leitura')
        print('opção 2: consulta de log')
        print('opção 3: sair')
        opcao = int(input('selecione uma opção:'))
        
        if opcao == 1:
            Reader.startRead()
            print('Leitura finalizada, cheque o csv.')
            Menu.mainMenu()
        elif opcao == 2:
            print('Exibindo todos os logs:')
            Log.printLog()
            Menu.mainMenu()
        elif opcao == 3:
            print('Saindo...')
            exit()
        else:
            print('Opção inválida')
            Menu.mainMenu()