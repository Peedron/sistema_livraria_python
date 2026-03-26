# SISTEMA LIVRARIA

try:
    # função para separar informações
    def linha():
        print('-='*20)

    # criando classe 
    class Livro:
        # definindo os atributos da classe
        def __init__(self, titulo,codigo,editora,area,ano,valor,quantidade_estoque):
            self.titulo = titulo
            self.codigo = codigo
            self.editora = editora
            self.area = area
            self.ano = ano
            self.valor = valor
            self.quantidade_estoque = quantidade_estoque

    # declarando lista e tornando conhecida em todo o código
    global lista_livros
    lista_livros=list()

    # função calcula o valor do estoque de livros
    def calcula_valor_estoque(a, b):
        # as variáveis recebem o preço e a quantidade de unidades para multiplicar
        valor = a * b
        return (valor)

    # função de cadastro de livros
    def cadastro_livro():
        linha()
        lista_livros.append(Livro(titulo=input("Título do livro: ").title(),
                                codigo=input("Código: "),
                                editora=input("Editora: ").title(),
                                area=input("Área: ").title(),
                                ano=input("Ano: "),
                                valor=float(input("Valor: ")),
                                quantidade_estoque=int(input("Número de unidades: "))))
        linha()

    # função que mostra os livros cadastrados
    def info_livros():
        linha()
        print(" ---- Livros cadastrados ---- ") # mensagem para situar o usuário
        for livro in lista_livros:
            print(f"\nCod#{livro.codigo}")
            print(f"Título/Editora: {livro.titulo}/{livro.editora}")
            print(f"Categoria: {livro.area}")
            print(f"Ano: {livro.ano}")
            print(f"Valor: R$ {livro.valor:.2f}")
            print(f"Estoque: {livro.quantidade_estoque} unidades")
            
            # chamando função para calcular o valor do Estoque
            valor_estoque = calcula_valor_estoque(livro.valor,livro.quantidade_estoque)
            print(f"Valor total em estoque: R$ {valor_estoque:.2f}")
            
        linha()

    # função busca o livro pelo nome:
    def buscar_nome():
        linha()
        
        nome = input("Título do livro: ").title()
        
        registro = False # variável é 'false' caso o livro não exista na lista
        
        for livro in lista_livros:
            if nome in livro.titulo:
                registro = True
                print("\nLivro encontrado:")
                print(f"\nCod#{livro.codigo}")
                print(f"Título/Editora: {livro.titulo}/{livro.editora}")
                print(f"Categoria: {livro.area}")
                print(f"Ano: {livro.ano}")
                print(f"Valor: R$ {livro.valor:.2f}")
                print(f"Estoque: {livro.quantidade_estoque} unidades")
                
                # chamando função para calcular o valor do Estoque
                valor_estoque = calcula_valor_estoque(livro.valor,livro.quantidade_estoque)
                print(f"Valor total em estoque: R$ {valor_estoque:.2f}")
        
        if not registro:
            print("Livro não encontrado!")
        
        linha()
        
    # função apresenta livros de uma categoria específica
    def categoria():
        linha()
        # recebendo a categoria
        categoria = input("Categoria de livros: ").title()
        
        registro = False # variável é 'false' caso a categoria não exista na lista
        for livro in lista_livros:
            if categoria in livro.area:
                registro = True
                print(f"\nCod#{livro.codigo}")
                print(f"Título/Editora: {livro.titulo}/{livro.editora}")
                print(f"Categoria: {livro.area}")
                print(f"Ano: {livro.ano}")
                print(f"Valor: R$ {livro.valor:.2f}")
                print(f"Estoque: {livro.quantidade_estoque} unidades")
                
                # chamando função para calcular o valor do Estoque
                valor_estoque = calcula_valor_estoque(livro.valor,livro.quantidade_estoque)
                print(f"Valor total em estoque: R$ {valor_estoque:.2f}")
        
        if not registro:
            print("Não há livros com está categoria!")
        linha()

    # função demonstra livros que tem preço menor do que um valor
    def limite_valor():
        linha()
        # usuário indica a faixa de preço que deseja
        preco = float(input("Defina um limte de preço: "))
        registro = False # variável é 'false' caso não haja livros até o valor informado
        
        for livro in lista_livros:
            if livro.valor <= preco:
                registro = True
                print("\nLivro encontrado:")
                print(f"\nCod#{livro.codigo}")
                print(f"Título/Editora: {livro.titulo}/{livro.editora}")
                print(f"Categoria: {livro.area}")
                print(f"Ano: {livro.ano}")
                print(f"Valor: R$ {livro.valor:.2f}")
                print(f"Estoque: {livro.quantidade_estoque} unidades")
                
                # chamando função para calcular o valor do Estoque
                valor_estoque = calcula_valor_estoque(livro.valor,livro.quantidade_estoque)
                print(f"Valor total em estoque: R$ {valor_estoque:.2f}")
        
        if not registro:
            print("Não há livros nessa faixa de preço!")
        linha()

    # função busca livros com valor de estoque maior que o indicado
    def compara_valor_estoque():
        linha()
        valor_indicado = float(input("Digite o valor do estoque: "))
        
        for livro in lista_livros:
            # chamando função para calcular o valor do Estoque
            valor_estoque = calcula_valor_estoque(livro.valor,livro.quantidade_estoque)
            
            if valor_estoque >= valor_indicado:
                print(f"\nCod#{livro.codigo}")
                print(f"Título/Editora: {livro.titulo}/{livro.editora}")
                print(f"Categoria: {livro.area}")
                print(f"Ano: {livro.ano}")
                print(f"Valor: R$ {livro.valor:.2f}")
                print(f"Estoque: {livro.quantidade_estoque} unidades")
                print(f"Valor total em estoque: R$ {valor_estoque:.2f}")
        linha()

    # função busca livros por quantidade de unidade
    def numero_unidades():
        quantidade = int(input("Digite o número de unidades desejada: "))
        
        for livro in lista_livros:
            if livro.quantidade_estoque >= quantidade:
                print(f"\nCod#{livro.codigo}")
                print(f"Título/Editora: {livro.titulo}/{livro.editora}")
                print(f"Categoria: {livro.area}")
                print(f"Ano: {livro.ano}")
                print(f"Valor: R$ {livro.valor:.2f}")
                print(f"Estoque: {livro.quantidade_estoque} unidades")
                
                # chamando função para calcular o valor do Estoque
                valor_estoque = calcula_valor_estoque(livro.valor,livro.quantidade_estoque)
                print(f"Valor total em estoque: R$ {valor_estoque:.2f}")

    # adicionando livros na lista
    livro1 = lista_livros.append(Livro(titulo="O Avesso Da Pele",
                                codigo="0301",
                                editora="Companhia Das Letras",
                                area="Romance",
                                ano="2019",
                                valor=47.60,
                                quantidade_estoque=50))
    livro2 = lista_livros.append(Livro(titulo="Engenharia de Software",
                                codigo="1203",
                                editora="Pressman",
                                area="Computação",
                                ano="2011",
                                valor=78,
                                quantidade_estoque=100))

    # mensagem introdutória
    print("---- SISTEMA LIVRARIA ---- ")

    # menu principal do usuário
    def menu():
        print("Bem vindo ao programa livraria! :)")
        print("Essas são as opções do programa:\n")

        repetir = True
        while repetir:
            # apresentando opções
            print('1 - Cadastrar novo livro')
            print('2 - Listar livros')
            print('3 - Buscar livros por nome')
            print('4 - Buscar livros por categoria')
            print('5 - Buscar livros por preço')
            print('6 - Busca por quantidade em estoque')
            print('7 - Valor total no estoque')
            print('0 - Encerrar atividades')
            
            print("\nO que quer fazer?")
            escolha = int(input("Sua escolha: "))

            # estrutura de decisão
            if escolha == 1:
                cadastro_livro()
            elif escolha == 2:
                info_livros()
            elif escolha == 3:
                buscar_nome()
            elif escolha == 4:
                categoria()
            elif escolha == 5:
                limite_valor()
            elif escolha == 6:
                numero_unidades()
            elif escolha == 7:
                compara_valor_estoque()
            elif escolha == 0:
                sair()

            # usuário decide após ação se deseja fazer mais alguma coisa
            continuar = input("Deseja continuar? ").lower()
            if continuar == 'nao':
                print("Volte sempre.")
                print("Saindo...")
                print("\nFim do programa!")
                repetir = False

    # função que encerra o programa
    def sair():
        print("Você decidiu sair do programa! Volte sempre!")
        raise(EOFError)

    menu()
except EOFError:
    print("\nFim do programa!")






