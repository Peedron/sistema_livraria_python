''' SISTEMA LIVRARIA
Dia 14/04/2026:
Corrigi os tratamentos de erros e validações, 
e adicionei a função para salvar os livros cadastrados no arquivo,
a criei mais uma função para mostrar os livros cadastrados no arquivo.
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

    # função para separar informações
    def linha():
        print('-='*20)

    ''' ---- FUNÇÕES AUXILIARES PARA VALIDAÇÃO DE DADOS ---- '''
    # função para validar input do tipo float
    def validar_float(entrada):
        repetir = True
        while repetir:
            try:
                entrada = entrada.replace(',', '.')
                valor = float(entrada) # conversão do dado
                
                # laço verifica se o número não é negativos
                validacao = True
                while validacao:
                    if valor < 0:
                        print("Valor negativo! Digite novamente!")
                        entrada = input("Qual é o preço? ") 
                        validacao = False
                    else:
                        validacao = False
                        repetir = False
            except ValueError:
                print("Erro, digite somente números!")
                entrada = input("Preço: ")
        
        return(valor) # retorna o valor caso possa ser convertido

    # função para validar input do tipo int
    def validar_int(entrada):
        repetir = True
        while repetir:
            try:
                valor = int(entrada) # conversão de dados

                # laço verifica se o número não é negativo
                validacao = True
                while validacao:
                    if valor < 0:
                        print("Valor negativo! Digite novamente!")
                        entrada = input("Número de unidades: ")
                        validacao = False
                    else:
                        validacao = False
                        repetir = False
            except ValueError:
                print("Erro, digite somente números!")
                entrada = input("Número de unidades: ")
        
        return(valor) # retorna o valor caso possa ser convertido

    # função para validar ano do livro
    def validar_ano(entrada):
        repetir = True
        while repetir:
            if len(entrada) == 4:
                year = int(entrada) # conversão para inteiro para fazer a comparação
                
                # condição de comparação para o ano ser aceito
                if year >= 1455 and year <= 2026:
                    repetir = False
                else:
                    print("Não há livros publicados nesse ano!")
                    print("Digite novamente!")
                    entrada = input("Ano: ")
            else:
                print("Erro, digite um ano válido!")
                entrada = input("Ano: ")
        
        return(year)

    # função para validar as strings do título, editora e área do livro
    def validar_string(entrada):

        repetir = True
        while repetir:

            entrada = entrada.replace(';', '') # o título não pode conter ';' para evitar problemas na leitura do arquivo
            variavel = " ".join(entrada.split()) # normalizando o título para remover espaços extras entre as palavras
            variavel = variavel.strip() # removendo espaços extras no inicio e no fim do título

            if len(variavel) > 0 and len(variavel) <= 100: # o título deve ter entre 1 e 100 caracteres
                variavel = variavel.title() # normalizando o nome para título
                repetir = False
            else:
                print("Entrada inválida! Digite novamente!")
                entrada = input("Entrada: ")
        
        return(variavel) # retorna o título normalizado caso seja válido

    # função para validar o código do livro
    def validar_codigo(entrada):
        repetir = True
        while repetir:
            if len(entrada.strip()) > 0 and len(entrada.strip()) <= 6: # o código deve ter entre 1 e 6 caracteres
                
                valido = entrada.isalnum() # o código deve ser alfanumérico
                if not valido:
                    print("Código inválido! O código deve conter somente letras e números!")
                    print("Digite novamente!")
                    entrada = input("Código: ")
                else:
                    cod = entrada.upper() # normalizando o código para maiúsculo
                    repetir = False
            else:
                print("Código inválido! O código deve conter entre 1 e 6 caracteres!\n")
                print("Digite novamente!")
                entrada = input("Código: ")
        
        return(cod) # retorna o código normalizado caso seja válido

        repetir = True
        while repetir:
            if len(entrada.strip()) > 0 and len(entrada.strip()) <= 50: # a área deve ter entre 1 e 50 caracteres
                area = entrada.title().strip() # normalizando a área para título
                repetir = False
            else:
                print("Área inválida! Digite novamente!")
                entrada = input("Área: ")
        
        return(area) # retorna a área normalizada caso seja válida

    ''' ---- FUNÇÕES PRINCIPAIS DO PROGRAMA ---- '''
    # função para exibir os livros cadastrados
    def estoque_livros():
        linha()
        with open("livros_cadastrados.txt", "r") as arquivo: # abrindo o arquivo para leitura
            if not arquivo: # caso o arquivo esteja vazio, a mensagem é exibida
                print("Não há livros cadastrados no estoque!")
            else:
                for line in arquivo: # cada linha do arquivo é lida
                    dados = line.strip().split(';') # os dados são separados por ';' e armazenados em uma lista
                    print(f"\nCod#{dados[0]}") # cada dado é acessado por seu índice na lista
                    print(f"Título/Editora: {dados[1]}/{dados[4]}")
                    print(f"Categoria: {dados[3]}")
                    print(f"Ano: {dados[2]}")
                    print(f"Valor: R$ {float(dados[5]):.2f}")
                    print(f"Estoque: {dados[6]} unidades")
                    
                    # chamando função para calcular o valor do Estoque
                    valor_estoque = calcula_valor_estoque(float(dados[5]),int(dados[6]))
                    print(f"Valor total em estoque: R$ {valor_estoque:.2f}")
        linha()

    # função para salvar os livros cadastrados no arquivo
    def salvar_estoque():
        with open("livros_cadastrados.txt", "a") as arquivo: # abrindo o arquivo para escrita
            for livro in lista_livros: # livro é o objeto da classe Livro, e cada um dos atributos é separado por ';' para facilitar a leitura do arquivo
                arquivo.write(f"{livro.codigo};{livro.titulo};{livro.ano};{livro.area};{livro.editora};{livro.valor:.2f};{livro.quantidade_estoque}\n")
                # a cada repetição do laço, um livro é escrito no arquivo, e cada atributo é separado por ';' para facilitar a leitura do arquivo

    # função calcula o valor do estoque de livros
    def calcula_valor_estoque(preco, quantidade):
        # as variáveis recebem o preço e a quantidade de unidades para multiplicar
        valor = preco * quantidade
        return (valor)

    # função de cadastro de livros
    def cadastro_livro():
        linha()
        lista_livros.append(Livro(titulo=validar_string(input("Título do livro: ")),
                                codigo=validar_codigo(input("Código: ")),
                                editora=validar_string(input("Editora: ")),
                                area=validar_string(input("Área: ")),
                                ano=validar_ano(input("Ano: ")),
                                valor=validar_float(input("Valor: ")),
                                quantidade_estoque=validar_int(input("Número de unidades: "))))
        print("\nLivro cadastrado com sucesso!")
        linha()
        
    # função busca o livro pelo nome:
    def buscar_nome():
        linha()
        
        nome = input("Título do livro: ").title().strip() # nome do livro já normalizado
        
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
        categoria = input("Categoria de livros: ").title().strip() # categoria já normalizada
        
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
        quantidade = validar_int(input("Digite o número de unidades desejada: "))

        for livro in lista_livros:
            if quantidade >= livro.quantidade_estoque:
                livro.info_livros()
    
    # função que encerra o programa
    def sair():
        print("Encerrando atividades...")
        raise(EOFError)

    # menu principal do usuário
    def menu():
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
            print('8 - Carregar estoque de livros')
            print('9 - Atualizar arquivo de livros cadastrados')
            print('0 - Encerrar atividades')
            
            print("\nO que quer fazer?")
            
            # laço impede do programa para próxima pergunta
            validacao = True
            while validacao:
                # tratando conversão errada
                try:
                    escolha = int(input("Sua escolha: "))
                    # estrutura de decisão
                    if escolha == 1:
                        cadastro_livro()
                        validacao = False
                    elif escolha == 2:
                        linha()
                        print(" ---- Livros cadastrados ---- ") # mensagem para situar o usuário
                        for livro in lista_livros:
                            livro.info_livros()
                        validacao = False
                    elif escolha == 3:
                        buscar_nome()
                        validacao = False
                    elif escolha == 4:
                        categoria()
                        validacao = False
                    elif escolha == 5:
                        limite_valor()
                        validacao = False
                    elif escolha == 6:
                        numero_unidades()
                        validacao = False
                    elif escolha == 7:
                        compara_valor_estoque()
                        validacao = False
                    elif escolha == 8:
                        print("Função em desenvolvimento!")
                        validacao = False
                    elif escolha == 9:
                        print(" ---- Livros cadastrados no estoque ---- ") # mensagem para situar o usuário
                        estoque_livros()
                        validacao = False
                    elif escolha == 0:
                        pergunta = input("\nDeseja salvar as alterações antes de sair? [Sim/Não]: ").lower()

                        invalido = True # variável para o laço
                        while invalido:
                            if pergunta[0] == 's': # pegando somente a primeira letra da resposta
                                salvar_estoque()
                                print("Alterações salvas com sucesso!")
                                invalido = False # encerra o laço de validação
                            elif pergunta[0] == 'n': # pegando somente a primeira letra da resposta
                                print("Alterações não salvas!")
                                invalido = False # encerra o laço de validação
                            else:
                                print("Por favor, digite 'Sim' ou 'Não'!")

                        sair()
                        validacao = False
                    else:
                        print("Digite um dos números acima para avançar, por favor!")
                        # laço não encerra até uma das opções ser selecionada
                except ValueError:
                    print("Erro, digite somente números!")

            invalido = True # variável para o laço
            # laço de repetição impede que usuário digite algo diferente de 'sim' ou 'não'
            while invalido:
                # usuário decide, após ação, se deseja fazer mais alguma coisa
                continuar = input("Deseja continuar? [Sim/Não]: ").lower()

                if continuar[0] == 'n': # pegando somente a primeira letra da resposta
                    pergunta = input("\nDeseja salvar as alterações antes de sair? [Sim/Não]: ").lower()

                    salvar = True # variável para o laço
                    while salvar:
                        if pergunta[0] == 's': # pegando somente a primeira letra da resposta
                            salvar_estoque()
                            print("Alterações salvas com sucesso!")
                            salvar = False # encerra o laço de validação
                        elif pergunta[0] == 'n': # pegando somente a primeira letra da resposta
                            print("Alterações não salvas!")
                            salvar = False # encerra o laço de validação
                        else:
                            print("Por favor, digite 'Sim' ou 'Não'!")
                    
                    print("Volte sempre.")
                    print("Saindo...")
                    print("\nFim do programa!")
                    repetir = False # encerra com o laço que continua apresentando as funções do menu
                    invalido = False # encerra o laço de validação
                elif continuar[0] == 's': # pegando somente a primeira letra da resposta
                    invalido = False # encerra o laço de validação
                else:
                    print("Por favor, digite 'Sim' ou 'Não'!")

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

    # mensagens introdutórias
    print("---- SISTEMA LIVRARIA ---- \n\n")
    print("Bem vindo ao programa livraria! :)")
    print("Essas são as opções do programa:\n")
    
    menu()
except EOFError:
    print("\nFim do programa!")
