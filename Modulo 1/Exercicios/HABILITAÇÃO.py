nome = input("qual e o seu nome? ")
idade = int(input("qual a sua idade? "))
possui_carteira = int(input("possui carteira de motorista? \n (1-sim / 2-não) "))

if idade >= 18:
    if possui_carteira == 1: 
        print("pode dirigir")

    else:
        print(" não pode dirigir")

else: 
    print("menor de idade")







