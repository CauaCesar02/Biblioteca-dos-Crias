class Livro:
    def __init__(self, id, titulo, autor, isbn, editora, anoPublicacao, disponivel):
        self._id: str = id
        self._titulo: str = titulo
        self._autor: str = autor
        self._isbn: str = isbn
        self._editora: str = editora
        self._anoPublicacao: int = anoPublicacao
        self._disponivel: bool = disponivel
    
    @property
    def id(self):
        return self._id
    
    @id.setter
    def id(self, valor):
        self._id = valor

    @property
    def titulo(self):
        return self._titulo
    
    @titulo.setter
    def titulo(self, valor):
        self._titulo = valor
    
    @property
    def autor(self):
        return self._autor
    
    @autor.setter
    def autor(self, valor):
        self._autor = valor

    @property
    def isbn(self):
        return self._isbn
    
    @isbn.setter
    def isbn(self, valor):
        self._isbn = valor

    @property
    def editora(self):
        return self._editora
    
    @editora.setter
    def editora(self, valor):
        self._editora = valor

    @property
    def anoPublicacao(self):
        return self._anoPublicacao
    
    @anoPublicacao.setter
    def anoPublicacao(self, valor):
        self._anoPublicacao = valor

    @property
    def disponivel(self):
        return self._disponivel
    
    @disponivel.setter
    def disponivel(self, valor):
        self._disponivel = valor


def cadastrar_livro(lista_livros: list[Livro]) -> bool:
    print("CADASTRO DE LIVRO")
    try:
        id = str(len(lista_livros))
        titulo = input("Título: ")
        autor = input("Autor: ")
        isbn = input("ISBN: ")
        editora = input("Editora: ")
        anoPublicacao = int(input("Ano de Publicação: "))
        disponivel = input("Disponível [S/n]?")
        disponivel = disponivel.upper()[0] == "S"

        lista_livros.append(Livro(id, titulo, autor, isbn, editora, anoPublicacao, disponivel))
        print("Livro Cadastrado")
        return True
    except Exception as e:
        print("Erro ao cadastrar livro.")
        print(e)
        return False


def atualizar_livro(lista_livros: list[Livro]) -> bool:
    print("ATUALIZAÇÃO DE LIVRO")
    try:
        id = int(input("Digite o ID do livro a ser atualizado: "))
    except ValueError:
        print("Não foi possível reconhecer o número inteiro")
        return False
    except Exception:
        print(Exception)
        return False

    if id >= len(lista_livros):
        print("Não foi encontrado o índice especificado. Tente atualizar os índices.")
        return False
    
    livro: Livro = lista_livros[id]
    try:
        novo_titulo = input(f"Título [{livro.titulo}]: ")
        if novo_titulo != "":
            livro.titulo = novo_titulo

        novo_autor = input(f"Autor [{livro.autor}]: ")
        if novo_autor != "":
            livro.autor = novo_autor

        novo_isbn = input(f"ISBN [{livro.isbn}]: ")
        if novo_isbn != "":
            livro.isbn = novo_isbn

        nova_editora = input(f"Editora [{livro.editora}]: ")
        if nova_editora != "":
            livro.editora = nova_editora

        novo_anoPublicacao = input(f"Ano de Publicação [{livro.anoPublicacao}]: ")
        if novo_anoPublicacao != "":
            livro.anoPublicacao = int(novo_anoPublicacao)

        disponivel = input(f"Disponível [S/n]? ")
        if disponivel != "":
            livro.disponivel = disponivel.upper()[0] == "S"

        lista_livros[id] = livro

        print("LIVRO ATUALIZADO")
        return True
    except Exception as e:
        print("Erro ao atualizar o livro.")
        print(e)
        return False

def mostrar_livro(livro: Livro):
    print(f"ID: {livro.id}")
    print(f"\tTítulo: {livro.titulo}")
    print(f"\tAutor: {livro.autor}")
    print(f"\tISBN: {livro.isbn}")
    print(f"\tEditora: {livro.editora}")
    print(f"\tAno de Publicacao: {livro.anoPublicacao}")
    disponivel = "SIM" if livro.disponivel else "NÃO"
    print(f"\tDisponível: {disponivel}")

def listar_livros(lista_livros: list[Livro]) -> None:
    if not len(lista_livros):
        print("Nenhum livro cadastrado.")
        return
    
    for livro in lista_livros:
        mostrar_livro(livro)

def consultar_livro_titulo(lista_livros: list[Livro]):
    print("CONSULTA DE LIVRO PELO TÍTULO")
    titulo = input(f"Título: ")
    consulta: list[Livro] = []
    for livro in lista_livros:
        if titulo.lower() in livro.titulo.lower():
            consulta.append(livro)

    if not len(consulta):
        print("Livro não encontrado.")
        return
    
    print("Livro(s) encontrados:")
    listar_livros(consulta)

def excluir_livro(lista_livros: list[Livro]):
    id = input("ID do livro a ser excluído: ")
    encontrado = False
    for livro in lista_livros:
        if id == livro.id:
            encontrado = True
            mostrar_livro(livro)
            lista_livros.remove(livro)
            corrigir_indices(lista_livros)
            print("- Livro Excluído!")
    
    if not encontrado:
        print("ID não encontrado.")

def corrigir_indices(lista_livros: list[Livro]):
    for indice, livro in enumerate(lista_livros):
        if indice != int(livro.id):
            livro.id = str(indice)

def menu():
    print("Biblioteca dos Crias")
    print("1- Mostrar todos livros cadastrados")
    print("2- Cadastrar livro")
    print("3- Atualizar livro")
    print("4- Consultar livro pelo título")
    print("5- Excluir livro")
    print("0- Sair do sistema")

def popular_livros_teste(lista_livros: list[Livro]):
    livros.append(Livro(str(len(lista_livros)), 'IT: A coisa', 'Stephen King', '8560280944', 'Suma', 2014, False))
    lista_livros.append(Livro(str(len(lista_livros)), "Dom Casmurro", "Machado de Assis", "9788535910666", "Companhia das Letras", 2008, False))
    lista_livros.append(Livro(str(len(lista_livros)), "1984", "George Orwell", "9788535914848", "Companhia das Letras", 2009, False))
    lista_livros.append(Livro(str(len(lista_livros)), "O Senhor dos Anéis", "J.R.R. Tolkien", "9788595084742", "HarperCollins", 2019, False))
    lista_livros.append(Livro(str(len(lista_livros)), "Grande Sertão: Veredas", "João Guimarães Rosa", "9788583862094", "Nova Fronteira", 2016, False))
    lista_livros.append(Livro(str(len(lista_livros)), "A Revolução dos Bichos", "George Orwell", "9788535909554", "Companhia das Letras", 2007, False))
    lista_livros.append(Livro(str(len(lista_livros)), "O Nome da Rosa", "Umberto Eco", "9788535907239", "Record", 2001, False))
    lista_livros.append(Livro(str(len(lista_livros)), "Ensaio sobre a Cegueira", "José Saramago", "9788535914848", "Companhia das Letras", 1995, False))
    lista_livros.append(Livro(str(len(lista_livros)), "Cem Anos de Solidão", "Gabriel García Márquez", "9788535914849", "Record", 2003, False))
    lista_livros.append(Livro(str(len(lista_livros)), "O Pequeno Príncipe", "Antoine de Saint-Exupéry", "9788522031449", "Agir", 2009, False))
    lista_livros.append(Livro(str(len(lista_livros)), "A Metamorfose", "Franz Kafka", "9788535914847", "Companhia das Letras", 2006, False))


if __name__ == "__main__":
    livros: list[Livro] = []
    popular_livros_teste(livros)
    while True:
        print("\n\n\n")
        menu()
        opcao = int(input("Escolha uma opção: "))
        match(opcao):
            case 1:
                listar_livros(livros)
            case 2:
                cadastrar_livro(livros)
            case 3:
                atualizar_livro(livros)
            case 4:
                consultar_livro_titulo(livros)
            case 5:
                excluir_livro(livros)
            case 0:
                break
