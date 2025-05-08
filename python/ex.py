import os
import random

def limpar_tela():
    os.system("cls" if os.name == "nt" else "clear")
    
    
#      -----//-------//------

#Exc 4


def contar_pares_impares():
    n = int(input("Digite a quantidade de numeros aleatorios: "))
    lista = []
    pares = 0
    impares = 0

    for i in range(n):
        num = random.randint(1, 100)
        lista.append(num)
        if num % 2 == 0:
            pares += 1
        else:
            impares += 1
    
    print("Lista gerada:", lista)
    print("Quantidade de numeros pares:", pares)
    print("Quantidade de numeros ímpares:", impares)
    
#      -----//-------//------

#Exc 5

def indexar_palavras():
    texto = input("Digite um texto: ")
    texto = texto.lower()
    pontuacao = ",.!?-"  # remove pontos

    for p in pontuacao:
        texto = texto.replace(p, "")

    palavras = texto.split()
    indice = {}

    for palavra in palavras:
        inicial = palavra[0]
        if inicial in indice:
            indice[inicial].append(palavra)
        else:
            indice[inicial] = [palavra]
    
    print(indice)

    
#      -----//-------//------


def escolha():
    limpar_tela()
    print("Escolha uma opção:")
    print("1 - Contar pares e impares")
    print("2 - Indexar palavras")
    opcao = int(input("Digite a opção desejada: "))

    if opcao == 1:
        contar_pares_impares()
    elif opcao == 2:
        indexar_palavras()
    else:
        print("Ops, erro!")

escolha()