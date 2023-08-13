from random import randint

def source(db: dict):
    while True:
        id = int(input('Digite o número da conta: '))
        if id in db.keys():
            return id
        else:
            print('Conta não encontrada!')
            continue

def createClient(db: dict):
    id = randint(1, 10000)
    while id in db:
        id = randint(1, 10000)
        continue
    name = input("Digite o nome do cliente: ")
    balance = float(input("Digite o saldo do cliente: "))
    db[id] = {
        "name": name,
        "balance": balance
    }
    print('Cliente criado com sucesso!')

def updateClient(db, id):
    name = input("Digite o nome do cliente: ")
    balance = float(input("Digite o saldo do cliente: "))
    db[id]['name'] = name
    db[id]['balance'] = balance
    print('Dados alterados com sucesso!')

def readClient(db, id):
    print(f"Nome do cliente: {db[id]['name']}")
    print(f"Saldo: {db[id]['balance']}")

def printCliets(db):
    for id in db.keys():
        print(f"Número da conta: {id}\n",
              f"Nome: {db[id]['name']}\n",
              f"Saldo R${db[id]['balance']}")

def deleteClient(db, id):
    del db[id]
    print('Conta excluída com sucesso!')

def withdrawMoney(db, id):
    print(f"Usuário: {db[id]['name']}\n",
        f"Seu saldo atual é de R${db[id]['balance']}")
    value = float(input('Digite o valor a ser sacado: '))
    if value > db[id]['balance']:
        print('Saldo insuficiente!')
    else:
        db[id]['balance'] -= value
        print("Saque realizado com sucesso!\n",
            f"Seu novo saldo é de R${db[id]['balance']}")
        
def depositMoney(db, id):
    print(f"Usuário: {db[id]['name']}\n",
        f"Seu saldo atual é de R${db[id]['balance']}")
    value = float(input('Digite o valor a ser depósitado: '))
    db[id]['balance'] += value
    print("Depósito realizado com sucesso!\n",
        f"Seu novo saldo é de R${db[id]['balance']}")

def transferMoney(db, id):
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


