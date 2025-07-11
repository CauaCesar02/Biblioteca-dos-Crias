total_livros = []
livros_bibliotica = {}

funcionarios_da_biblioteca = []
funcionario_biblioteca = {"nome_funcionario": "Judicleide", "matricula_funcionario": 1234}
funcionarios_da_biblioteca.append(funcionario_biblioteca)

usuarios_biblioteca = []
usuarios_cadastrados = {'nome_usuario': "Gustavo", 'numero_usuario': 69912345678 ,'cpf_usuario': 12345678910 }
usuarios_biblioteca.append(usuarios_cadastrados)

livros_disponivel = []
livro_indisponivel = []
livros_reservados = []



class Bibliotecaria:
    def __init__(self, nome_funcionario, matricula_funcionario):
        self.nome_funcionario = nome_funcionario
        self.matricula_funcionario = matricula_funcionario

    def cadastrar_usuario (matricula_funcionario):
        usuarios_cadastrados = input('Digite o nome do novo usuario: ')
        usuarios_cadastrados = input('Digite o CPF do novo usuario: ')
        usuarios_cadastrados = input('Digite o numero do novo usuario: ')
        usuarios_biblioteca.append(usuarios_cadastrados)
        print(usuarios_biblioteca)
        
    def atualizar_usuaria (matricula_funcionario):
        usuario = input("Digite o nome do usuario: ")
        for u in range(len(usuarios_biblioteca)):
            if usuario == usuarios_biblioteca(u):
                usuarios_biblioteca.clear(usuario)
                usuarios_cadastrados = input('Digite o novo nome do usuario: ')
                usuarios_cadastrados = input('Digite o novo CPF do usuario: ')
                usuarios_cadastrados = input('Digite o novo numero do usuario: ')
                usuarios_biblioteca.append(usuarios_cadastrados)
                print(usuarios_biblioteca)
            else:
                print(f"O usuario {usuario} não esta cadastrado. ")
        pass

class Usuario:
    def __init__(self, nome_usuario, numero_usuario, cpf_usuario):
        self.nome = nome_usuario
        self.cpf = cpf_usuario
        self.numero = numero_usuario

    def reservar_livro(self, livro):
        l = input(f'Verificar se tem o livro desejado na biblioteca: ')
        for l in range(0, len(total_livros)):
            if total_livros[l] == livro:
                print(total_livros[l])
            else:
                print("Infelizmente não temos esse livro. ")
            for l in range(0, len(livros_disponivel)):
                if livro == livros_disponivel[l]:
                    livros_reservados.append(livro)
            pass

Bibliotecaria.atualizar_usuaria(1234)