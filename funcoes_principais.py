from dados import Livro, lista_livros, Filial, lista_filiais, lista_livros_filial
from funcoes_validacao import (validar_pergunta,validar_int,validar_ano,validar_codigo,
                               validar_float,validar_string,validar_filial)

''' ---- FUNÇÕES PRINCIPAIS DO PROGRAMA ---- '''
# menu que recebe a escolha do usuário
def menu_de_opcoes():
    print("\nO que quer fazer?")
    escolha = input("Sua escolha: ")

    # laço para validar as escolhas feitas no menu
    validacao = True
    while validacao:
        try:
            escolha = int(escolha) # só parte para as estrturas caso possa ser convertido
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
                estoque_livros()
                validacao = False
            elif escolha == 9:
                salvar_estoque()
                validacao = False
            elif escolha == 0:
                sair()
                validacao = False
            else:
                print("Número inteiro fora das opções!")
                escolha = input("\nSua escolha: ")
                # laço não encerra até uma das opções ser selecionada
        except ValueError:
            print("Erro, o campo só aceita números inteiros!")
            escolha = input("\nSua escolha: ")

# função para separar informações
def separador():
    print('-='*20)

# função para carregar os livros cadastrados no arquivo
def estoque_livros():
    separador()

    if len(lista_livros) > 0:
        entrada = "\nDeseja salvar o que foi feito antes de carregar o estoque?[Sim/Não]: "
        resposta = validar_pergunta(entrada)
        if resposta[0] == 's':
            salvar_estoque()

    print("Carregando livros cadastrados...\n")
    
    '''lista_livros.clear() # esvaziando a lista caso os dados do arquivo já tenham sido baixados
    with open("livros_cadastrados.txt", "r") as arquivo: # abrindo o arquivo para leitura
        for linha in arquivo:
            dados = linha.strip().split(";") # tirando os espaços e separando as informações por ';'

            lista_livros.append(Livro(codigo_livro=dados[0],
                                      titulo=dados[1],
                                      ano=int(dados[2]),
                                      area=dados[3],
                                      editora=dados[4],
                                      valor=float(dados[5]),
                                      quantidade_estoque=int(dados[6]),
                                      filial=dados[7]))
    print("O estoque de livros foi baixado!")
    separador()'''

# função para mostrar os livros baixados do estoque (arquivo)
def listagem_de_livros():
    separador()
    if len(lista_livros) == 0:
        print("Não há livros no sistema!")
        print("Carregue o estoque para ver os livros cadastrados!")
    else:
        # a variável 'livro' age como um objeto
        # pegando cada elemento da lista_livros e instânciando
        # com os atríbutos da classe Livro
        for livro in lista_livros:
            livro.info_livros()
        
    separador()

# função para salvar os livros cadastrados no arquivo
def salvar_estoque():
    with open("livros_cadastrados.txt", "a") as arquivo: # abrindo o arquivo para escrita
        for livro in lista_livros: # livro é o objeto da classe Livro, e cada um dos atributos é separado por ';' para facilitar a leitura do arquivo
            if livro.filial == 'FL01':
                arquivo.write(f"")
            arquivo.write(f"{livro.codigo};{livro.titulo};{livro.ano};{livro.area};{livro.editora};{livro.valor:.2f};{livro.quantidade_estoque}\n")
            # a cada repetição do laço, um livro é escrito no arquivo, e cada atributo é separado por ';' para facilitar a leitura do arquivo

    print("\nAlterações salvas!")
    separador()

# função calcula o valor do estoque de livros
def calcula_valor_estoque(preco, quantidade):
    # as variáveis recebem o preço e a quantidade de unidades para multiplicar
    valor = preco * quantidade
    return (valor)

# função de cadastro de livros
def cadastro_livro():
    separador()
    lista_livros.append(Livro(titulo=validar_string(input("Título do livro: ")),
                            codigo_livro=validar_codigo(input("Código[de 1 a 6 caracteres]: ")),
                            editora=validar_string(input("Editora: ")),
                            area=validar_string(input("Área: ")),
                            ano=validar_ano(input("Ano: ")),
                            valor=validar_float(input("Valor: ")),
                            quantidade_estoque=validar_int(input("Número de unidades: ")),
                            filial=validar_filial(input("Qual é a filial? "))))
    print("\nLivro cadastrado com sucesso!")
    separador()
    
# função busca o livro pelo nome:
def buscar_nome():
    separador()
    
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
    separador()
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
    separador()

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
    separador()
    soma = 0 # declarando soma
    
    for livro in lista_livros:
        # chamando função para calcular o valor do Estoque
        valor_estoque = calcula_valor_estoque(livro.valor,livro.quantidade_estoque)
        soma += valor_estoque # variável soma todos os valores de estoque a cada repetição
    
    print(f"O valor total em estoque de livros na livraria é de: R$ {soma:,.2f}".replace(",", "X").replace(".",",").replace("X","."))

    separador()

# função busca livros por quantidade de unidade
def numero_unidades():
    quantidade = validar_int(input("Digite o número de unidades desejada: "))

    for livro in lista_livros:
        if quantidade >= livro.quantidade_estoque:
            livro.info_livros()

# função que encerra o programa
def sair():
    separador()
    if len(lista_livros) == 0:
        raise(EOFError)
    else:
        resposta = validar_pergunta("\nDeseja salvar as alterações antes de sair? [Sim/Não]: ")

        if resposta[0] == 's': # pegando somente a primeira letra da resposta
            salvar_estoque()
            print("Alterações salvas com sucesso!")
        else:
            print("Alterações não salvas!")
        
        print("\nVolte sempre!")
        print("Encerrando atividades...")
        raise(EOFError)
