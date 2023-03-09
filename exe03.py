tentativas = 0

while tentativas < 3:
    senha = input("Digite a senha: ")
    if senha == 'senha123':
        print("Acesso concedido!")
        break
    else:
        print("Senha incorreta. Tente novamente.")
        tentativas += 1
        
    if tentativas == 2:
        print("Faltam apenas 1 tentativa.")
    
else:
    print("Você excedeu o número máximo de tentativas.")