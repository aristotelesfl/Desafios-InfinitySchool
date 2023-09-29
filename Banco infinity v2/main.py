from actions.crud import *
from actions.search import source
from operations.menu import operationsMenu

while True:
    opcao = int(input("------- BANCO INFINITY ------- \n"
                      "1 - Adicionar cliente \n"
                      "2 - Editar cliente \n"
                      "3 - Buscar cliente \n"
                      "4 - Apagar cliente \n"
                      "5 - Exibir clientes \n"
                      "6 - Menu de operações \n"                      
                      "7 - Sair \n"
                      "Selecione uma opção: "))

    if opcao == 1:
        createClient(db)

    elif opcao == 2:
        updateClient(db, source(db))

    elif opcao == 3:
        readClient(db, source(db))

    elif opcao == 4:
        deleteClient(db, source(db))

    elif opcao == 5:
        printCliets(db)

    elif opcao == 6:
        operationsMenu(db)

    elif opcao == 7:
        break