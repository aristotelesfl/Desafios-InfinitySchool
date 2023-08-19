from random import randint
import pandas as pd

def createClient(db: dict) -> None:
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

def updateClient(db: dict, id: int) -> None:
    name = input("Digite o nome do cliente: ")
    balance = float(input("Digite o saldo do cliente: "))
    db[id]['name'] = name
    db[id]['balance'] = balance
    print('Dados alterados com sucesso!')

def readClient(db: dict, id: int) -> None:
    print(f"Nome do cliente: {db[id]['name']}")
    print(f"Saldo: {db[id]['balance']}")

def printCliets(db: dict) -> None:
    for id in db.keys():
        print(f"Número da conta: {id}\n",
              f"Nome: {db[id]['name']}\n",
              f"Saldo R${db[id]['balance']}")

def deleteClient(db: dict, id: int) -> None:
    del db[id]
    print('Conta excluída com sucesso!')