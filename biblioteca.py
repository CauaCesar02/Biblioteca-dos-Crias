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

class Livro:
    def __init__(self, titulo, autor, ano_publicado, editora, status):
        self.titulo = titulo
        self.autor = autor
        self.ano_publicado = ano_publicado
        self.editora = editora
        self.status = status

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
            
class Cliente:
    def __init__(self, nome_cliente, numero_cliente, cpf_cliente, livro_reservado):
        self.nome = nome_cliente
        self.cpf = cpf_cliente
        self.numero = numero_cliente
        self.livro_reservado = livro_reservado 

    def cancelar_reserva(self, livro):
        for i in range(0, len(livros_disponivel)):
            if livro == livros_disponivel[i]:
                livros_reservados.append(livro)

    def devolver_livros(self, livro):
         for i in range(0, len(livro_indisponivel)):
            if livro == livro_indisponivel[livro]:
                livros_reservados.remove(i)
            '''for i in range(0,len(livros_emprestado)):
                if len(livros_emprestado) == "":
                    del livros_emprestado'''
            pass

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

    def atualizar_usuaria (matricula_funcionario, nome_usuario):
        usuarios_cadastrados = input(f'Atualize o nome do usuario {nome_usuario}: ')
        usuarios_cadastrados = input(f'Atualize o CPF do usuario {nome_usuario}: ')
        usuarios_cadastrados = input(f'Atualize o numero do usuario {nome_usuario}: ')
        usuarios_biblioteca.append(usuarios_cadastrados)
        print(usuarios_biblioteca)
        pass
    
    def adicionar_livro(self, livro):
        total_livros.append(livro)
        pass

    def cancelar_reservar_livro(self, livro):
        livros_reservados.remove(livro)
        print(livros_reservados)
        pass

    def buscar_livro(self, titulo):
        if titulo == total_livros[titulo]:
            print(titulo)
        else:
            print("Titulo não cadastrado. ")
        pass

    def livro_disponivel(self, livro, titulo):
        for i in range(0, len(livros_disponivel)):
            if livro == livros_disponivel[i]:
                print(f"O Livro {titulo} Está Disponivel. ")
            else:
                print(f"O Livro {titulo} Está Indisponivel. ")
        pass

    def livro_indisponivel(self, livro, titulo):
        for i in range(0, len(livros_disponivel)):
            if livro == livros_disponivel[i]:
                print(f"O Livro {titulo} Está Disponivel. ")
            else:
                print(f"O Livro {titulo} Está Indisponivel. ")
        pass




livro = Livro('IT: A coisa', 'Stheve King', 'disponivel')
livros_disponivel.append(livro)
usuario = Usuario("Igor Matias", 'IT: A coisa')

Livro.devolver_livro('IT: A coisa', 'Stheve King')
Livro.disponivel('IT: A coisa', 'Stheve King', 'IT: A coisa')

for i in livros_disponivel:
    print(f'Título: {livro.titulo}, Autor: {livro.autor}, Status: {livro.status}')



