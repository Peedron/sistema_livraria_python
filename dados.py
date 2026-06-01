# criando classe 
class Livro:
    # definindo os atributos da classe
    def __init__(self, titulo,codigo_livro,editora,area,ano,valor,quantidade_estoque,filial):
        self.titulo = titulo
        self.codigo = codigo_livro
        self.editora = editora
        self.area = area
        self.ano = ano
        self.valor = valor
        self.quantidade_estoque = quantidade_estoque
        self.filial = filial
    
    # método para mostrar as informações dos livros
    def info_livros(self):
        print(f"Título: {self.titulo}")
        print(f"Código: {self.codigo}")
        print(f"Editora: {self.editora}")
        print(f"Categoria: {self.area}")
        print(f"Ano: {self.ano}")
        
        for filial in lista_filiais:
            # estrutura de decisão para imprimir as informações da filial correspondente
            if self.filial == filial.codigo:
                print(f"Valor: R${self.valor:.2f}>>>>Filial {filial.nome}, estoque: {self.quantidade_estoque} unidades\n")
            else:
                continue

# declarando lista
lista_livros=list()

# nova classe do sistema
class Filial:
    # definindo os atributos da classe
    def __init__(self,codigo_filial,nome,endereco,contato,livros_estoque):
        self.codigo = '#FL' + codigo_filial
        self.nome = nome
        self.endereco = endereco
        self.contato = contato
        self.livros_estoque = livros_estoque
    
    def exibe_estoque(self):
        for filial in lista_filiais:
            print(f"Livros da filial {filial.nome}:\n")
            for livro in lista_livros_filial:
                print(f"{livro.titulo}\n")
    
# declarando lista de filiais
lista_filiais=list()
# lista de livros de cada filial
lista_livros_filial=list()

# função para validar o estoque de livros de cada filial
def conferir_estoque(quantidade):
    with open('livros_cadastrados.txt', 'r') as arquivo:
        primeira_linha = arquivo.readlines() # ignorando a primeira linha
        for linha in arquivo:
            dados = linha.strip().split(';')
            for filial in lista_filiais:
                if dados[7] == filial.codigo:
                    quantidade += int(dados[6])
                else:
                    continue
    
    return quantidade

# adicionando filiais
lista_filiais.append(Filial(codigo_filial='01',
            nome="Zona Norte",
            endereco="Voluntários da Pátria - 1354",
            contato="5040-3010",
            livros_estoque=conferir_estoque(0)))
lista_filiais.append(Filial(codigo_filial="02",
                                nome="Menino Deus",
                                endereco="Getúlio Vargas - 501",
                                contato="4120-6709",
                                livros_estoque=conferir_estoque(0)))
lista_filiais.append(Filial(codigo_filial="03",
                                nome="Centro",
                                endereco="Duque de Caxias - 890",
                                contato="9001-2530",
                                livros_estoque=conferir_estoque(0)))
