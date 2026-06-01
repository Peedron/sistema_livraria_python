''' SISTEMA LIVRARIA
Dia 17/05/2026:
Criei mais um arquivo para separar uma possível solução para o programa
que utiliza classmethod e os conceitos de herança, que não vou utilizar por enquanto.
Também separei os menus do programa, deixando o que contém as escolhas do usuário
no arquivo de "funções_principais" e o de apresentação no "__main__".
Neste momento, o mais importante é entender como estruturar os novos requisitos do sistema
para que eles não quebre o programa. 
Ainda não fiz o tratamento de exceções da função
salvar_estoque, o que precisa ser revisado. Além de ajustar as classes
e entender qual é a melhor saída para mostrar as informações da Filial em que
cada livro está em 'dados.py'.

Preciso pensar em como desenvolver a saída de valores que estão em diferentes filiais,
os valores atualmente se repetem, ou seja, o método imprime o mesmo livro duas vezes,
e não só as informações divergentes (valor e quantidade de estoque).
'''
from funcoes_principais import(menu_de_opcoes,sair,separador)
from funcoes_validacao import validar_pergunta

# menu principal do usuário
def menu_de_apresentacao():
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
        
        # chamando a função para validar a escolha do usuário
        menu_de_opcoes()

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
    menu_de_apresentacao()
except EOFError:
    print("\nFim do programa!")
