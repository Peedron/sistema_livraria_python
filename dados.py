# criando classe 
class Livro:
    # definindo os atributos da classe
    def __init__(self, titulo,codigo,editora,area,ano,valor,quantidade_estoque,filial):
        self.titulo = titulo
        self.codigo = codigo
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

# --- INÍCIO DOS NOVOS COMPONENTES DE POO ---

class OperacoesLivraria:
    """
    SUPERCLASSE (Classe Pai): 
    Criamos esta classe para demonstrar o conceito de Herança. 
    Ela contém métodos utilitários que podem ser "herdados" por outras classes.
    Dessa forma, evitamos repetição de código.
    """
    @classmethod
    def formatar_moeda(cls, valor):
        """
        O decorador @classmethod significa que este método pertence à CLASSE como um todo,
        e não a um objeto específico (instância). 
        Por isso usamos 'cls' (representando a classe) em vez de 'self' (representando o objeto).
        """
        return f"R$ {valor:.2f}".replace('.', ',')


# A classe Filial agora herda de OperacoesLivraria. 
# Para fazer a herança em Python, colocamos a superclasse entre parênteses.
class Filial(OperacoesLivraria):
    # definindo os atributos da classe
    def __init__(self,codigo,nome,endereco,contato,livros_estoque):
        self.codigo = 'FL' + codigo
        self.nome = nome
        self.endereco = endereco
        self.contato = contato
        self.livros_estoque = livros_estoque
    
    def info_filiais(self):
        # Aqui usamos o 'self' porque estamos acessando os dados de uma filial específica
        print(f"Livros em estoque: {self.livros_estoque} unidades")

    # --- REQUISITO 3.3 ---
    @classmethod
    def listagem_de_estoque(cls, codigo_filial, livros):
        """
        Requisito 3.3: Acessar de forma separada o estoque de cada filial[cite: 20].
        Como é um @classmethod, chamamos através de Filial.listagem_de_estoque().
        Passamos a lista de livros geral como parâmetro para fazer a filtragem.
        """
        print(f"\n--- Listagem de estoque (Filial {codigo_filial}) ---")
        valor_total = 0
        encontrou = False
        
        for livro in livros:
            # Filtramos para mostrar apenas os livros da filial solicitada
            if livro.filial == codigo_filial:
                livro.info_livros()
                # Calcula o valor do estoque multiplicando preço pela quantidade
                valor_total += (livro.valor * livro.quantidade_estoque)
                encontrou = True
        
        # Apresenta o valor total em livros no estoque escolhido [cite: 22]
        if encontrou:
            # Aqui estamos usando um método que foi HERDADO da superclasse OperacoesLivraria
            valor_formatado = cls.formatar_moeda(valor_total)
            print(f"Valor total em livros no estoque: {valor_formatado}")
        else:
            print("Não há livros cadastrados nesta filial.")

    # --- REQUISITO 3.4 ---
    @classmethod
    def busca_individual(cls, codigo_filial, termo_busca, tipo_busca, livros):
        """
        Requisito 3.4: Realizar as buscas já implementadas de forma individual em cada filial[cite: 23].
        O parâmetro 'tipo_busca' define se o usuário quer buscar por 'nome', 'categoria', etc.
        """
        print(f"\n--- Busca por {tipo_busca} na Filial {codigo_filial} ---")
        encontrou = False
        
        for livro in livros:
            # Primeiro, garantimos que estamos olhando apenas para a filial certa
            if livro.filial == codigo_filial:
                
                # Depois, verificamos qual é o tipo de busca e se o termo corresponde
                if tipo_busca == 'nome' and termo_busca.lower() in livro.titulo.lower():
                    livro.info_livros()
                    encontrou = True
                
                elif tipo_busca == 'categoria' and termo_busca.lower() in livro.area.lower():
                    livro.info_livros()
                    encontrou = True
                
                elif tipo_busca == 'preco_maximo' and livro.valor <= float(termo_busca):
                    livro.info_livros()
                    encontrou = True
        
        if not encontrou:
            print(f"Nenhum livro corresponde a esta busca na filial {codigo_filial}.")

    # --- REQUISITO 3.5 ---
    @classmethod
    def busca_por_codigo(cls, codigo_livro, livros, filiais):
        """
        Requisito 3.5: Busca por código que procura em todas as filiais[cite: 24].
        """
        print(f"\n>>>>> Cod#{codigo_livro}")
        
        # Criamos uma lista apenas com os livros que possuem o código buscado
        livros_encontrados = [livro for livro in livros if livro.codigo == codigo_livro]
        
        if not livros_encontrados:
            print("Nenhum livro com este código foi encontrado no sistema.")
            return

        # Como livros idênticos têm o mesmo título, editora e ano[cite: 10], 
        # pegamos essas informações do primeiro livro da lista para não repetir a impressão
        livro_base = livros_encontrados[0]
        print(f"Titulo/Editora: {livro_base.titulo}/{livro_base.editora}") # [cite: 26]
        print(f"Categoria: {livro_base.area}") # [cite: 27]
        print(f"Ano: {livro_base.ano}") # [cite: 28]
        
        valor_total_geral = 0
        
        # Agora iteramos por todos os livros encontrados para mostrar os preços e estoques diferentes
        for livro in livros_encontrados:
            # Descobrindo o nome da filial para a impressão exigida [cite: 29]
            nome_filial = "Desconhecida"
            for f in filiais:
                if f.codigo == livro.filial:
                    nome_filial = f.nome
                    break
            
            valor_formatado = cls.formatar_moeda(livro.valor)
            print(f"Valor: {valor_formatado} >>> Filial {nome_filial}, estoque: {livro.quantidade_estoque} unidades") # [cite: 29]
            
            # Somando ao valor total em estoque (valor unitário * quantidade)
            valor_total_geral += (livro.valor * livro.quantidade_estoque)
            
        print(f"Valor total em estoque: {cls.formatar_moeda(valor_total_geral)}") # [cite: 29]

# nova classe do sistema
class Filial:
    # definindo os atributos da classe
    def __init__(self,codigo,nome,endereco,contato,livros_estoque):
        self.codigo = 'FL' + codigo
        self.nome = nome
        self.endereco = endereco
        self.contato = contato
        self.livros_estoque = livros_estoque
    
    def info_filiais(self):
        print(f"Livros em estoque: {self.livros_estoque} unidades")
    

# declarando lista de filiais
lista_filiais=list()
# lista de livros de cada filial
lista_livros_filial=list()

# função para validar o estoque de livros de cada filial
def conferir_estoque(quantidade):
    with open('livros_cadastrados.txt', 'r') as arquivo:
        for linha in arquivo:
            dados = linha.strip().split(';')
            for filial in lista_filiais:
                if dados[7] == filial.codigo:
                    quantidade += int(dados[6])
                else:
                    continue
    
    return quantidade

# adicionando filiais
lista_filiais.append(Filial(codigo='01',
            nome="Zona Norte",
            endereco="Voluntários da Pátria - 1354",
            contato="5040-3010",
            livros_estoque=conferir_estoque(0)))
lista_filiais.append(Filial(codigo="02",
                                nome="Menino Deus",
                                endereco="Getúlio Vargas - 501",
                                contato="4120-6709",
                                livros_estoque=conferir_estoque(0)))
lista_filiais.append(Filial(codigo="03",
                                nome="Centro",
                                endereco="Duque de Caxias - 890",
                                contato="9001-2530",
                                livros_estoque=conferir_estoque(0)))
