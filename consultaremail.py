import sys
from itertools import islice
vazamentos = {
    "abc@gmail.com": "123456"
    , "abcd@gmail.com": "1234567"
    , "abcde@gmail.com": "12345678"
    }
def print_menu():
    print("      ______________________________ ")
    print("     |                              | ")
    print("     | CONSULTA DE E-MAILS VAZADOS. | ")
    print("     |______________________________| ")
    print("")
    print("            Escolha uma opção             ")
    print(" ________________________________________")
    print("|                                        |")
    print("| 1) Sair                                |")
    print("| 2) Consultar email especifico.         |")     
    print("| 3) Verificar todos os e-mails vazados. |")
    print("|________________________________________|")
home = True
def bonito():
    print("===========================================")

def bonitodois():
    print("-------------------------------------------")


def checar():
    pergunta = ""
    buscarEmail = input("Digite um Email: ")
    if buscarEmail in vazamentos:
        senha = vazamentos[buscarEmail]
        email = buscarEmail
        print("Seus dados foram comprometidos")
        print("Seu email e senha são:", email, ":" ,senha)
        bonitodois()
        remover = input("Deseja remover o vazamento?: ").upper()
        if remover == "S":
            remocao = vazamentos.pop(email, senha)
            if remocao != None:
                bonito()
                print("Removido com sucesso")
                bonito()
                pergunta = input("Deseja digitar outro email ?'S' Para confirmar. ").upper()
        else:
            print("A informação não pode ser removida")
            pergunta = input("Deseja digitar outro email ?'S' Para confirmar. ").upper()
        if pergunta == "S":
            checar()
        else:
            negacao()
    else:
        print("Não encontramos dados em nossa base.")
        bonitodois()
        pergunta = input("Deseja digitar outro email ?'S' Para confirmar. ").upper()
        if pergunta == "S":
            checar()
        else:
            negacao()

def iterador():
    print("=======================================")
    print("      Listando",len(vazamentos),"Vazamentos.")
    print("=======================================")
    print("")
    iterator = islice(vazamentos, 10)
    for mail, senha in vazamentos.items():
        print(mail,":", senha)
        bonitodois()
        
def todos():    
    confirma = ""
    if confirma != "N":
        iterador()
        bonito()
        print("               Fim da Lista")
        bonito()

def volta_menu():
    print(" __________________________________________")
    print("| 1)                Sair                   |")
    print("| 2)      Consultar email especifico.      |" )     
    print("| 3) Verificar todos os e-mails vazados.   |")
    print(" ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾")

def respinvalidaum():
    volta_menu()
    print("\n")
    print("Resposta Invalida.")
def respinvalidazero():
    bonito()
    print("Resposta Invalida.")
    bonito()
    

def negacao():
    print("1) Sair ")
    print("2) Voltar ao menu ")
    confirmasaida = input("Digite 1 ou 2: ")
    if confirmasaida == "1":
        saida()
    if confirmasaida == "2":
        volta_menu()
    else:
        print("\n"*10)
        respinvalidazero()
        negacao()

def saida():
    bonito()
    print("      Até mais, Sentirei sua falta :(")
    sys.exit (bonito())

print_menu()
while home:
    bonitodois()
    escolha = input("Escolha entre [1-3]: ")
    bonitodois()

    if escolha == "1":
        print("\n"*2)
        saida()
        
    elif escolha == "2":
        print("\n"*10)
        bonito()
        print("         Consultar email específico")
        bonito()
        checar()

    elif escolha == "3":
        print("\n"*2)
        todos()
        negacao()

    else:
        respinvalidaum()