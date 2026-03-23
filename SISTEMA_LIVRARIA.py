try:
    # função para separação de informações
    def linha():
        print("-="*20)

    # criando classe livraria
    class Livraria:
        # definição dos atributos da classe
        def __init__(self, 
                    titulo,
                    codigo,
                    editora,
                    area,
                    ano,
                    valor,
                    quantidade_estoque):
            self.titulo = titulo
            self.codigo = codigo
            self.editora = editora
            self.area = area
            self.ano = ano
            self.valor = valor
            self.quantidade_estoque = quantidade_estoque # fazer valor de estoque
            self.valor_estoque = self.quantidade_estoque * self.valor

    global lista_livros # definindo lista como variável global
    lista_livros = list() # criando lista que irá receber os livros

    # função para o usuário cadastrar livros
    def cadastro_livros():
        lista_livros.append(Livraria(
            titulo=input("Título do livro: ").title(),
            codigo= input("Código: "),
            editora= input("Editora: ").title(),
            area= input("Área: ").title(),
            ano= input("Ano: "),
            valor= float(input("Valor: ")),
            quantidade_estoque= int(input("Quantidade: "))))

    # função com as informações dos livros cadastrados
    def acervo():
        # mensagem para o usuário
        linha()
        print("Esses são os livros cadastrados:\n")
        # laço de repetição para mostrar as informações de cada livro
        for livro in lista_livros:
            print(f">>>>>Cod#{livro.codigo}")
            print(f"Título/Editora: {livro.titulo}/{livro.editora}")
            print(f"Categoria: {livro.area}")
            print(f"Ano: {livro.ano}")
            print(f"Valor: R$ {livro.valor:.2f}")
            print(f"Estoque: {livro.quantidade_estoque} unidades")
            print(f"Valor total em estoque: R$ {livro.valor_estoque:.2f}")

    # função para encontrar livros por nome
    def buscar_titulo(): 
        # variável recebe o nome do livro e já formata o texto
        nome = input("Digite o título do livro que deseja: ").title()

        contador = 0
        linha()
        for livro in lista_livros:
            if nome not in livro.titulo:
                contador += 1
                print("Livro encontrado! Essas são as informações:\n")
                print(f">>>>>Cod#{livro.codigo}")
                print(f"Título/Editora: {livro.titulo}/{livro.editora}")
                print(f"Categoria: {livro.area}")
                print(f"Ano: {livro.ano}")
                print(f"Valor: R$ {livro.valor:.2f}")
                print(f"Estoque: {livro.quantidade_estoque} unidades")
                print(f"Valor total em estoque: R$ {livro.valor_estoque:.2f}")
        
        if contador == 0:
            print("Este livro não se encontra no acervo!")

    # função para buscar livros por suas categorias/áreas
    def buscar_categoria():
        categoria = input("Qual categoria de livros que deseja ver? ").title()

        contador = 0
        linha()
        for livro in lista_livros:
            if categoria in livro.area:
                contador += 1
                print(f">>>>>Cod#{livro.codigo}")
                print(f"Título/Editora: {livro.titulo}/{livro.editora}")
                print(f"Categoria: {livro.area}")
                print(f"Ano: {livro.ano}")
                print(f"Valor: R$ {livro.valor:.2f}")
                print(f"Estoque: {livro.quantidade_estoque} unidades")
                print(f"Valor total em estoque: R$ {livro.valor_estoque:.2f}")
        
        if contador == 0:
            print("Não há livros com essa categoria!")

    # função de comparação de preços
    def preco_menor():
        preco = float(input("Deseja ver livros abaixo de qual valor? "))

        # contador ajuda a saber se existe pelo menos um livro no até o valor indicado
        contador = 0
        linha()
        print(f"Livros até R$ {preco:.2f}:\n")
        for livro in lista_livros:
            if livro.valor < preco:
                contador += 1
                print(f">>>>>Cod#{livro.codigo}")
                print(f"Título/Editora: {livro.titulo}/{livro.editora}")
                print(f"Categoria: {livro.area}")
                print(f"Ano: {livro.ano}")
                print(f"Valor: R$ {livro.valor:.2f}")
                print(f"Estoque: {livro.quantidade_estoque} unidades")
                print(f"Valor total em estoque: R$ {livro.valor_estoque:.2f}")

        if contador == 0:
            linha()
            print("Não há livros neste valor!")
                
    # função que busca livros com valor de estoque maior
    def valor_estoque():
        valor = int(input("Digite um valor de estoque: "))

        linha()
        for livro in lista_livros:
            if livro.valor_estoque > valor:
                # informações do livro
                a = 1

    # variáveis fixas para que a livraria já tenha livros cadastrados
    livro1 = Livraria(titulo="O Avesso Da Pele",
                    codigo="082",
                    editora="Companhia Das Letras",
                    area="Romance",
                    ano="2021",
                    valor=47.60,
                    quantidade_estoque=12)

    # livros são guardados na lista
    lista_livros.append(livro1)

    # função menu para a navegação pelo sistema
    def menu():
        print("Bem vindo ao sistema livraria!")
        print("Aqui estão as opções do que fazer:\n")

        print("1-Cadastrar novo livro")
        print("2-Listar livros")
        print("3-Buscar livros por nome")
        print("4-Buscar livros por categoria")
        print("5-Buscar livros por preço")
        print("6-Busca por quantidade em estoque")
        print("7-Valor total no estoque")
        print("0-Encerrar atividades\n")

        repetir = True

        while repetir:
            escolha = int(input("Sua escolha: "))

            if escolha == 1:
                cadastro_livros()
            elif escolha == 2:
                acervo()
            elif escolha == 3:
                buscar_titulo()
            elif escolha == 4:
                buscar_categoria()
            elif escolha == 5:
                preco_menor()
            elif escolha == 6:
                valor_estoque()
            elif escolha == 0:
                sair()

            
            resposta = input("Deseja continuar? ").lower()

            if resposta == "nao":
                print("\nFim do programa! Volte sempre")
                repetir = False
            else:
                continue
    
    # função encerra o programa caso o usuário digite '0'
    def sair():
        linha()
        print("Você escolheu encerrar o programa!\n")
        raise(EOFError)
    
    menu()
except EOFError:
    print("Fim do programa!")
