def source(db: dict) -> int:
    while True:
        id = int(input('Digite o número da conta: '))
        if id in db.keys():
            return id
        else:
            print('Conta não encontrada!')
            continue
