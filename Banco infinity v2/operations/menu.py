from .deposit import depositMoney
from .transfer import transferMoney
from .withdraw import withdrawMoney
from actions.search import source

def operationsMenu(data: dict) -> None:
    print("___Menu de operações___\n",
          "1 - Saque\n",
          "2 - Depósito\n",
          "3 - Transferência\n",
          "4 - Sair")
    
    while True:
        option = int(input("Selecione uma operação: "))
        if option == 1:
            withdrawMoney(data, source(data))
        elif option == 2:
            depositMoney(data, source(data))
        elif option == 3:
            transferMoney(data, source(data))
        elif option == 4:
            break
        else:
            continue
