from curses.ascii import isdigit
import random

topo_numeros = input("escreva um numero: ")

if topo_numeros.isdigit():
    topo_numeros = int(topo_numeros)

    if topo_numeros <= 0:
        print("Por favor insira um numero maior que 0")
        quit()
else:
    print("por favor digite novamente um numero.")
    quit()

numero_aleatorio = random.randint(0, topo_numeros)
# para se testar se funcionou a lógica
# print(numero_aleatorio) 
while True:
    suposicao = input("Adivinhe")
    if suposicao.isdigit():
        suposicao = int(suposicao)
    else:
        print("Por favor digite novamente um numero")
        continue

    if suposicao == numero_aleatorio:
        print("Parabens você acertou")
        break
    elif suposicao > numero_aleatorio:
        print("Você estava acima do numero ")
    else:
        print("Você estava a baixo do numero")

