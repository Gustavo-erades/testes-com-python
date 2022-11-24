def money():
    print("**********")
    print("** MONEY **")
    print("**********\n")
    din_din=float(input("Quanto você ganha por hora? "))
    horas=float(input("Quantas horas completas você trablhou? "))
    dias=30
    total=(din_din*horas)*dias
    print("Seu salário por mês é: R${:.2f}".format(total))

def conversor():
    print("***********")
    print("** m-->cm **")
    print("***********\n")
    metro=input("digite a medida em metros: ")
    cent_metro= int(metro)*100
    print(str(metro), " Metros em Centimetros equivale à", str(cent_metro))

def somatorio():
    num1=input("Digite um número: ")
    num2=input("Digite outro número: ")
    num3=input("Digite mais um número: ")
    soma=int(num1)+int(num2)+int(num3)
    print("A soma de ", num1,"+", num2, "+",num3, " é igual a ", soma)

def menu(): 
    print("******************************")
    print("* 1 --> calcular dinheiro    *")
    print("* 2 --> conversor de unidade *")
    print("* 3 --> soma de núemeros      *")
    print("******************************\n")
    num=int(input("Opção desejada: "))
    if num==1:
        money()
    elif num==2:
        conversor()
    elif num==3:
        somatorio()
    elif num!=1 and 2 and 3:
        print("Escolha uma opção válida\n")
        menu()
menu()





