''' SISTEMA LIVRARIA
Dia 03/05/2026:
Renomeiei o nome do arquivo princpal do código e dividi em outros arquivos
as funções principais e de validação e as classes utilizadas no programa
para melhor organização. Ainda não fiz o tratamento de exceções da função
salvar_estoque, o que precisa ser revisado. Além de ajustar as classes
e entender qual é a melhor saída para mostrar as informações da Filial em que
cada livro está em 'dados.py'.

Preciso pensar em como desenvolver a saída de valores que estão em diferentes filiais,
os valores atualmente se repetem, ou seja, o método imprime o mesmo livro duas vezes,
e não só as informações divergentes (valor e quantidade de estoque).
'''
from funcoes_principais import(cadastro_livro,listagem_de_livros,
                                buscar_nome,categoria,limite_valor,
                                numero_unidades,compara_valor_estoque,
                                estoque_livros,salvar_estoque,sair,separador)

from funcoes_validacao import validar_pergunta

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

        # Fazendo a resposta do código ser mais dinâmica
        resposta = validar_pergunta('\nContinuar?[Sim/Não]: ')
        
        if resposta[0] == 's':
            continue
        else:
            sair()
        separador()

# mensagens introdutórias
print("---- SISTEMA LIVRARIA ---- \n\n")
print("Bem vindo ao programa livraria! :)")
print("Essas são as opções do programa:\n")

try:
    menu()
except EOFError:
    print("\nFim do programa!")
