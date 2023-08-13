from database import db
import functions
from functions import source

while True:
    opcao = int(input("------- BANCO INFINITY ------- \n"
                      "1 - Adicionar cliente \n"
                      "2 - Editar cliente \n"
                      "3 - Buscar cliente \n"
                      "4 - Apagar cliente \n"
                      "5 - Exibir clientes \n"
                      "6 - Sacar \n"                      
                      "7 - Depositar \n"
                      "8 - Transferir \n"
                      "9 - Sair \n"
                      "Selecione uma opção: "))

    if opcao == 1:
        functions.createClient(db)

    elif opcao == 2:
        functions.updateClient(db, source(db))

    elif opcao == 3:
        functions.readClient(db, source(db))

    elif opcao == 4:
        functions.deleteClient(db, source(db))

    elif opcao == 5:
        functions.printCliets(db)

    elif opcao == 6:
        functions.withdrawMoney(db, source(db))

    elif opcao == 7:
        functions.depositMoney(db, source(db))

    elif opcao == 8:
        functions.transferMoney(db, source(db))

    elif opcao == 9:
        break