'''O sistema de gerenciamento de estoque de livros permite que a biblioteca cadastre, atualize,
remova, e busque livros, bem como verifique a quantidade de exemplares disponíveis de cada
livro. Os livros serão armazenados em uma lista, onde cada elemento é um dicionário que
representa um livro com informações como título, autor, gênero, quantidade em estoque e
código do livro. O sistema usará diversas funções para manipular a lista de dicionários.'''

def cadastrar_livro(lista, titulo, autor, genero, quantidade, codigo):
    lista.append({'Código': codigo, 'Título': titulo, 'Autor': autor, 'Gênero': genero, 'Quantidade': quantidade})
    
def buscar_livros(lista, codigo):
    for livro in lista:
        for c, v in livro.items():
            if c == 'Código' and v == codigo:
                return f'Livro encontrado:\nCódigo: {livro[c]}\nTítulo: {livro['Título']}\nAutor: {livro['Autor']}\nGênero: {livro['Gênero']}\nQuantidade: {livro['Quantidade']}'
            
    return 'Não encontrado'
        
def atualizar_estoque(lista, codigo, quantidade):
    pass

livros = []

cadastrar_livro(livros, "Memórias Póstumas de Brás Cubas", "Machado de Assis", "Romance", 10, 1)
cadastrar_livro(livros, "Vidas Secas", "Graciliano Ramos", "Romance Regionalista", 15, 2)
cadastrar_livro(livros, "O Avesso da Pele", "Jeferson Tenório", "Romance Contemporâneo", 8, 3)
cadastrar_livro(livros, "Rosa do Povo", "Carlos Drummond de Andrade", "Poesia", 12, 4)
cadastrar_livro(livros, "O Menino Maluquinho", "Ziraldo", "Literatura Infantil", 20, 5)

print(buscar_livros(livros, ))
