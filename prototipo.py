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
