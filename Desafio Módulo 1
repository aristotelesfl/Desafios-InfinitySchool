#importa biblioteca random
import random
#cria dois vetores onde serão armazenados os usuários e seus telefones
user = []
phone = []
#cria loop infinito para armazenar usuários
while True:
    #variável para armazenar usuário momentaneamente
    usuario = input("Digite o usuario: ")
    #adiciona o usuário ao final do vetor "user"
    user.append(usuario)
    #armazena e adiciona telefone ao final do vetor "phone"
    phone.append(input("Digite o telefone: "))
    #verifica se usuário é "fim", caso verdadeiro encerra o loop, caso falso continua até que seja atribuído um usuário "fim"
    if usuario.lower() == "fim":
        break
#sorteia um número de 0 até o total de usuários cadastrados - 1
sorteio = random.randint(0, len(user)-1)
#printa o usuário vencedor a partir do número sorteado indicando a posição do vencedor no vetor "user"
print(f"O usuario premiado foi: {user[sorteio]}\nTelefone: {phone[sorteio]}")
