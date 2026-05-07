#Declarando variáveis
idade=int
ano=2026
resultado=int
#Definindo entrada
nome=input("Digite o seu nome: ")
idade=int(input("Digite a sua idade: "))
#Definindo processamento
resultado=ano-idade
Q1=int(input("Você já fez aniversário esse ano? Digite 1 para sim ou dois para não: "))
if Q1 == 1:
       resultado = ano-idade
else:
    resultado =(ano-idade)-1
print("Olá,", nome, "você nasceu em: ", resultado)
#Saída de dados

