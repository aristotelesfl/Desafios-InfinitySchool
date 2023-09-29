from actions.search import source

def transferMoney(db: dict, id: int) -> None:
    print(f"Usuário: {db[id]['name']}\n",
        f"Seu saldo atual é de R${db[id]['balance']}")
    id_Destiny = source(db)
    if id_Destiny == id:
        print("Operação negada!")
    else:
        value = float(input(f"Digite o valor a ser trasferido para {db[id_Destiny]['name']}: "))
        if value > db[id]['balance']:
            print("Saldo insuficiente!")
        else:
            db[id]['balance'] -= value
            db[id_Destiny]['balance'] += value
            print("Operação realizada com sucesso!\n",
                f"Seu novo saldo é de R${db[id]['balance']}",
                f"Saldo de {db[id_Destiny]['name']} é de {db[id_Destiny]['balance']}")