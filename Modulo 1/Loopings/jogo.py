import random

numero_magico = random.randint(1,100)
numero_usuario = 0
print(numero_magico)

while numero_usuario != numero_magico: 
    numero_usuario = int(input("digite um numero entre 1 a 100: "))

    if numero_usuario == numero_magico:
        print("parabens! voce acertou.")

    elif numero_magico > numero_usuario:
        print("o numero magico e maior!")
     
    else:
        print("o numero e menor")

    
   


  