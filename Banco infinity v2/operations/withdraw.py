
def withdrawMoney(db: dict, id: int) -> None:
    print(f"Usuário: {db[id]['name']}\n",
        f"Seu saldo atual é de R${db[id]['balance']}")
    value = float(input('Digite o valor a ser sacado: '))
    if value > db[id]['balance']:
        print('Saldo insuficiente!')
    else:
        db[id]['balance'] -= value
        print("Saque realizado com sucesso!\n",
            f"Seu novo saldo é de R${db[id]['balance']}")
        