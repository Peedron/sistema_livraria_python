''' SISTEMA LIVRARIA
Dia 02/04/2026:
Estou fazendo a refatoração do código, fazendo com que a estrutura esteja
mais próxima do que estudei em aula, além de montar corrigir pequenos
detalhes de comunicação com o usuário.
'''
try:
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
        
        # função que mostra os livros cadastrados
        def info_livros(self): # recebe o próprio objeto como parâmetro
            print(f"\nCod#{self.codigo}")
            print(f"Título/Editora: {self.titulo}/{self.editora}")
            print(f"Categoria: {self.area}")
            print(f"Ano: {self.ano}")
            print(f"Valor: R$ {self.valor:.2f}")
            print(f"Estoque: {self.quantidade_estoque} unidades")
            
            # chamando função para calcular o valor do Estoque
            valor_estoque = calcula_valor_estoque(self.valor,self.quantidade_estoque)
            print(f"Valor total em estoque: R$ {valor_estoque:.2f}")
                
            linha()

    # declarando lista e tornando conhecida em todo o código
    global lista_livros
    lista_livros=list()

    ''' ---- FUNÇÕES/REQUISITOS PRINCIPAIS DO SISTEMA LIVRARIA ---- '''
    # função para separar informações
    def linha():
        print('-='*20)

    # função para validar input do tipo float
    def validar_float(entrada):
        repetir = True
        while repetir:
            try:
                entrada = entrada.replace(',', '.')
                valor = float(entrada)
                repetir = False
                return(valor) # retorna o valor caso possa ser convertido
            except ValueError:
                print("Valor inválido! Digite novamente!")
            entrada = input("Preço: ")

    # função para validar input do tipo int
    def valida_int(entrada):
        repetir = True
        while repetir:
            try:
                valor = int(entrada)
                repetir = False
                return(valor) # retorna o valor caso possa ser convertido
            except ValueError:
                print("Valor inválido! Digite novamente!")
            entrada = input("Número de unidades: ")

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
                                valor=validar_float(input("Valor: ")),
                                quantidade_estoque=valida_int(input("Número de unidades: "))))
        linha()

    # função busca o livro pelo nome:
    def buscar_nome():
        linha()
        
        nome = input("Título do livro: ").title() # nome do livro já normalizado
        
        registro = False # variável é falsa caso o livro não exista na lista
        
        for livro in lista_livros:
            if nome in livro.titulo:
                registro = True
                livro.info_livros()
        
        if not registro:
            print("Livro não encontrado!")
        
    # função apresenta livros de uma categoria específica
    def categoria():
        linha()
        # recebendo a categoria
        categoria = input("Categoria de livros: ").title()
        
        registro = False # variável é 'false' caso a categoria não exista na lista
        for livro in lista_livros:
            if categoria in livro.area:
                registro = True
                livro.info_livros()
        
        if not registro:
            print("Não há livros com está categoria!")

    # função demonstra livros que tem preço menor do que um valor
    def limite_valor():
        linha()

        # usuário indica a faixa de preço que deseja
        preco = validar_float(input("Defina um limte de preço: "))

        registro = False # variável é 'false' caso não haja livros até o valor informado
        
        for livro in lista_livros:
            if livro.valor <= preco:
                registro = True
                livro.info_livros()
        
        if not registro:
            print("Não há livros nessa faixa de preço!")

    # função mostrar o valor total em estoque da livraria com os livros
    def compara_valor_estoque():
        linha()
        soma = 0 # declarando soma
        
        for livro in lista_livros:
            # chamando função para calcular o valor do Estoque
            valor_estoque = calcula_valor_estoque(livro.valor,livro.quantidade_estoque)
            soma += valor_estoque # variável soma todos os valores de estoque a cada repetição
        
        print(f"O valor total em estoque de livros na livraria é de: R$ {soma:.2f}")

        linha()

    # função busca livros por quantidade de unidade
    def numero_unidades():
        quantidade = valida_int(input("Digite o número de unidades desejada: "))

        for livro in lista_livros:
            if livro.quantidade_estoque >= quantidade:
                livro.info_livros()
    
    # função que encerra o programa
    def sair():
        print("Você decidiu sair do programa! Volte sempre!")
        raise(EOFError)

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
    '''Esses livros só foram adicionados para que eu pudesse testar
    como a função que imprime os valores dos livros cadastrados funcionaria
    '''

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
                linha()
                print(" ---- Livros cadastrados ---- ") # mensagem para situar o usuário
                for livro in lista_livros:
                    livro.info_livros()
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

            invalido = True # variável para o laço
            # laço de repetição impede que usuário digite algo diferente de 'sim' ou 'não'
            while invalido:
                # usuário decide após ação se deseja fazer mais alguma coisa
                continuar = input("Deseja continuar? [Sim/Não]: ").lower()

                if continuar[0] == 'n': # pegando somente a primeira letra da resposta
                    print("Volte sempre.")
                    print("Saindo...")
                    print("\nFim do programa!")
                    repetir = False # encerra com o laço que continua apresentando as funções do menu
                    invalido = False # encerra o laço de validação
                elif continuar[0] == 's': # pegando somente a primeira letra da resposta
                    invalido = False # encerra o laço de validação
                else:
                    print("Por favor, digite 'Sim' ou 'Não'!")

    menu()
except EOFError:
    print("\nFim do programa!")
