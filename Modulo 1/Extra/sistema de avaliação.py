nota_1 = int(input("digite a primera nota: "))
nota_2 = int(input("digite a segunda nota: "))
nota_3 = int(input("digite a terceira nota: "))

media = (nota_1 + nota_2 + nota_3) / 3

if media >= 7:
    print("aluno aprovado")
elif media >= 4:
    print("aluno de recuperação")
else:
    print("reprovado")




