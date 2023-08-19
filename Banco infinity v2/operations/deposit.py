def depositMoney(db: dict, id: int) -> None:
    print(f"Usuário: {db[id]['name']}\n",
        f"Seu saldo atual é de R${db[id]['balance']}")
    value = float(input('Digite o valor a ser depósitado: '))
    db[id]['balance'] += value
    print("Depósito realizado com sucesso!\n",
        f"Seu novo saldo é de R${db[id]['balance']}")
