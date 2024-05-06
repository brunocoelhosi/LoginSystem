import controller

if __name__ == "__main__":

    print('\n--------Login--------')
    while True:
        print('\n1 - Cadastrar Usuario \n2 - Realizar Login\n3- Sair')

        menu = int(input())

        if menu == 1:
            usr = controller.UsuarioController()
            nome = input('Digite o nome do Usuario\n')
            email = input('Digite o email do Usuario\n')
            senha = input('Digite a senha do Usuario\n')
            resultado = usr.cadastrarUsuario(nome,email,senha)

            if resultado == 2:
                print('nome invalido')
            elif resultado == 3:
                print('email invalido')
            elif resultado == 4:
                print('senha invalida')   
            elif resultado == 5:
                print('email ja cadastrado') 
            elif resultado == 6:
                print('erro interno do sistema') 
            elif resultado == 1:
                print('cadastro realizado com sucesso')

        elif menu == 2:
            usr = controller.LoginController()
            email = input('Digite o email:\n')
            senha = input('Digite a senha do Usuario\n')

            resultado = usr.realizarLogin(email,senha)

            if not resultado:
                print('email ou senha invalido')
            else:
                print('\nUsuario Logado com sucesso!')
                print(resultado)
        
        elif menu == 3:
            break

        else:
            0
