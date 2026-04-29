''' SISTEMA LIVRARIA
Dia 29/04/2026:
Corrigi a função estoque livros e agora estou acresecentando
um tratamento de erros para a função salvar_estoque, para que
não ajam livros repetidos no estoque>
Revise o cada linha do código está fazendo e se alguma
delas pode ou não quebrar o programa ao excutar uma função
depois da outra.
'''
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
    
    def info_livros(self):
        print(f"Título: {self.titulo}")
        print(f"Código: {self.codigo}")
        print(f"Editora: {self.editora}")
        print(f"Categoria: {self.area}")
        print(f"Ano: {self.ano}")
        print(f"Valor: R${self.valor:.2f}")
        print(f"Número de unidades: {self.quantidade_estoque:,.0f}\n")

# declarando lista
lista_livros=list()

# função para separar informações
def linha():
    print('-='*20)

''' ---- FUNÇÕES AUXILIARES PARA VALIDAÇÃO DE DADOS ---- '''
# função para validar perguntas com respostas 'sim ou não'
def validar_pergunta(pergunta):
    repetir = True
    while repetir:
        resposta = input(f"{pergunta}").lower()

        if resposta[0] == 's':
            resposta = 'sim'
            repetir = False
        elif resposta[0] == 'n':
            resposta = 'nao'
            repetir = False
        else:
            print("\nDigite Sim ou Não!")
    
    return resposta

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
                if valor < 1:
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

''' ---- FUNÇÕES PRINCIPAIS DO PROGRAMA ---- '''
# função para carregar os livros cadastrados no arquivo
def estoque_livros():
    linha()
    print("Carregando livros cadastrados...\n")
    
    lista_livros.clear() # esvaziando a lista caso os dados do arquivo já tenham sido baixados
    with open("livros_cadastrados.txt", "r") as arquivo: # abrindo o arquivo para leitura
        for line in arquivo:
            dados = line.strip().split(";") # tirando os espaços e separando as informações por ;

            lista_livros.append(Livro(codigo=dados[0],
                                      titulo=dados[1],
                                      ano=int(dados[2]),
                                      area=dados[3],
                                      editora=dados[4],
                                      valor=float(dados[5]),
                                      quantidade_estoque=int(dados[6])))

    print("O estoque de livros foi baixado!")
    linha()

# função para mostrar os livros baixados do estoque (arquivo)
def listagem_de_livros():
    linha()
    # a variável 'livro' age como um objeto
    # pegando cada elemento da lista_livros e instânciando
    # com os atríbutos da classe Livro
    for livro in lista_livros:
        livro.info_livros()
    
    linha()
                
# função para salvar os livros cadastrados no arquivo
def salvar_estoque():
    with open("livros_cadastrados.txt", "a") as arquivo: # abrindo o arquivo para escrita
        for livro in lista_livros: # livro é o objeto da classe Livro, e cada um dos atributos é separado por ';' para facilitar a leitura do arquivo
            arquivo.write(f"{livro.codigo};{livro.titulo};{livro.ano};{livro.area};{livro.editora};{livro.valor:.2f};{livro.quantidade_estoque}\n")
            # a cada repetição do laço, um livro é escrito no arquivo, e cada atributo é separado por ';' para facilitar a leitura do arquivo

    print("\nAlterações salvas!")
    linha()

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
    
    nome = input("Título do livro: ") # nome do livro
    validar_string(nome)
    
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
    categoria = validar_string(input("Categoria de livros: "))
    
    registro = False # variável é 'false' caso a categoria não exista na lista
    for livro in lista_livros:
        if categoria in livro.area:
            registro = True
            livro.info_livros()
    
    if not registro:
        print("Não há livros com esta categoria!")

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
    
    print(f"O valor total em estoque de livros na livraria é de: R$ {soma:,.2f}".replace(",", "X").replace(".",",").replace("X","."))

    linha()

# função busca livros por quantidade de unidade
def numero_unidades():
    quantidade = validar_int(input("Digite o número de unidades desejada: "))

    for livro in lista_livros:
        if quantidade >= livro.quantidade_estoque:
            livro.info_livros()

# função que encerra o programa
def sair():
    linha()
    print("\nVolte sempre!")
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
            # tratando erro de conversão de valor
            try:
                escolha = int(input("Sua escolha: "))
                # estrutura de decisão
                if escolha == 1:
                    cadastro_livro()
                    validacao = False
                elif escolha == 2:
                    listagem_de_livros()
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
                    if len(lista_livros) > 0:
                        entrada = "\nDeseja salvar o que foi feito antes de carregar o estoque?[Sim/Não]: "
                        resposta = validar_pergunta(entrada)
                        if resposta[0] == 's':
                            salvar_estoque()
                        else:
                            estoque_livros()
                    else:
                        estoque_livros()
                    validacao = False
                elif escolha == 9:
                    salvar_estoque()
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

        # Fazendo a resposta do código ser mais dinâmica
        entrada = '\nContinuar?[Sim/Não]: '
        resposta = validar_pergunta(entrada)

        if resposta[0] == 's':
            continue
        else:
            print("\nDigite 0 para encerrar o programa!")
        linha()

# mensagens introdutórias
print("---- SISTEMA LIVRARIA ---- \n\n")
print("Bem vindo ao programa livraria! :)")
print("Essas são as opções do programa:\n")

try:
    menu()
except EOFError:
    print("\nFim do programa!")
