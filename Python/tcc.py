cadastro = dict()

def validation(user):
    if user in cadastro:
        return True
    else:
        return False

def login(user, code):
    if user in cadastro:
        return True if user[value] == code else False
    else:
        return False

def cadastro():
    while True:
        user = (str(input('Insira o nome do usuario:')))
        code = str(input('Insira o codigo: '))
        codeVali = str(input('Insira novamente o codigo: '))
        cadastro[user] = code if code == codeVali else 404
        if cadastro[user] == 404:
            while True:
                codeVali = str(input('Insira novamente o codigo: '))
                cadastro[user] = code if code == codeVali else 404
                if cadastro[user] != 404:
                    break
def init():
    option = int(input('''O que deseja fazer ? 
    [1] - Cadastrar um usuario
    [2] - Validar um usuario
    '''))
    if option == 1:
        print('Esse é o menun de Cadastro: ')
        cadastro()
    elif option == 2:
        print('Esse é o menu de validação: ')
        user = str(input('Insira o usuário: '))
        validation(user)  

init()