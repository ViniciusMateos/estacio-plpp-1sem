#Criar um sistema simples de gerenciamento de uma biblioteca que contém vários livros usando o conceito de agregação. Você deve criar duas classes: Livro e Biblioteca.

#A classe Livro deve ter os seguintes atributos:
    # título (str);
    # autor (str);
    # isbn (str).

#A classe Biblioteca deve ter:

    # Um nome (str);
    # Uma lista de livros.

#A classe Biblioteca deve ter métodos para:

    # Adicionar um livro à biblioteca;
    # Remover um livro da biblioteca;
    # Listar todos os livros na biblioteca.


#############################

# Acompanhe o passo a passo.

# Defina a classe Livro:
# Construtor que inicializa os atributos título, autor e isbn.
# Defina a classe Biblioteca:
# Construtor que inicializa o nome da biblioteca e uma lista vazia de livros;
# Método para adicionar um livro (adicionar_livro);
# Método para remover um livro (remover_livro);
# Método para listar todos os livros (listar_livros).


class Livro:
    def __init__(self, titulo, autor, isbn):
        self.titulo = titulo
        self.autor = autor
        self.isbn = isbn

class Biblioteca:
    def __init__(self, nome):
        self.nome = nome
        self.livros = []

    def adicionar_livro(self, livro):
        self.livros.append(livro)
        print(f'Livro "{livro.titulo}" adicionado à biblioteca "{self.nome}".')

    def remover_livro(self, isbn):
        for livro in self.livros:
            if livro.isbn == isbn:
                self.livros.remove(livro)
                print(f'Livro "{livro.titulo}" removido da biblioteca "{self.nome}".')
                return
        print(f'Livro com ISBN {isbn} não encontrado na biblioteca "{self.nome}".')

    def listar_livros(self):
        if not self.livros:
            print(f'A biblioteca "{self.nome}" não tem livros.')
        else:
            print(f'Livros na biblioteca "{self.nome}":')
            for livro in self.livros:
                print(f'- {livro.titulo} por {livro.autor} (ISBN: {livro.isbn})')

# Testando as classes

# Criando alguns livros
livro1 = Livro('O Senhor dos Anéis', 'J.R.R. Tolkien', '1234567890')
livro2 = Livro('1984', 'George Orwell', '0987654321')
livro3 = Livro('O Apanhador no Campo de Centeio', 'J.D. Salinger', '1122334455')

# Criando uma biblioteca
biblioteca = Biblioteca('Biblioteca Central')

# Adicionando livros à biblioteca
biblioteca.adicionar_livro(livro1)
biblioteca.adicionar_livro(livro2)
biblioteca.adicionar_livro(livro3)

# Listando todos os livros na biblioteca
biblioteca.listar_livros()

# Removendo um livro da biblioteca
biblioteca.remover_livro('0987654321')

# Listando todos os livros na biblioteca após a remoção
biblioteca.listar_livros()