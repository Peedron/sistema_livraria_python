''' ---- FUNÇÕES AUXILIARES PARA VALIDAÇÃO DE DADOS ---- '''
# função para validar perguntas com respostas 'sim ou não'
def validar_pergunta(pergunta): # o parâmetro recebe a pergunta do usuário
    repetir = True
    while repetir:
        resposta = input(f"{pergunta}").lower() # chamando o parâmetro e normalizando a resposta do input

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

# função para verificar quais é a filial
def validar_filial(entrada):
    validacao = True
    while validacao:
        if (entrada == 'FL01') or (entrada == 'FL02') or (entrada == 'FL03'):
            validacao = False
        else:
            print("\nEstá filial não consta no sistema!")
            print("As filiais conhecidas são: FL01 | FL02 | FL03")

            entrada = input("\nQual é a filial? ")