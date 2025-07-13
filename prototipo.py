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


def atualizar_livro(lista_livros: list[Livro], id: str) -> bool:
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
    for livro in lista_livros:
        mostrar_livro(livro)


if __name__ == "__main__":
    pass