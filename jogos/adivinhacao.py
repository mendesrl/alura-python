print("********************")
print("*******Jogo*********")
print("********************")

numero_secreto = 42

chute_str = input("Digite o numero:")

print("Voce digitou", chute_str)

chute = int(chute_str)

if (numero_secreto == chute):
    print("Você acertou")
else:
    print('Você errou')

idade1 = "10"
idade2 = "20"
print(idade1 + idade2)

nome = "Nico"
sobrenome = "Steppat"
print(nome + sobrenome)