
# Perguntas

# 1. Como podemos determinar o tamanho de uma tupla?
t = (1, 2, 3)
print("Tamanho da tupla:", len(t))

# 2. Alterar o primeiro item da tupla (4, 5, 6) para (1, 5, 6)
T = (4, 5, 6)
T = (1,) + T[1:]
print("Tupla alterada:", T)

# Perguntas sobre listas

# 1. Dois modos de criar lista com cinco zeros
lista1 = [0] * 5
lista2 = [0 for i in range(5)]
print("Lista1:", lista1)
print("Lista2:", lista2)

# 2. Quatro operações que alteram list
lista3 = [3, 1, 2]
lista3.append(4)
lista3.sort()
lista3.remove(1)
lista3.insert(0, 10)
print("Lista alterada:", lista3)

# Exercício 1: Vetores intercalados
vetor1 = []
vetor2 = []
vetor3 = []

for i in range(10):
    vetor1.append(int(input(f"Digite o {i+1}º valor do primeiro vetor: ")))
for i in range(10):
    vetor2.append(int(input(f"Digite o {i+1}º valor do segundo vetor: ")))

for i in range(10):
    vetor3.append(vetor1[i])
    vetor3.append(vetor2[i])

print("Vetor Intercalado:", vetor3)

# Exercício 2: Temperaturas do ano
meses = ["Janeiro", "Fevereiro", "Março", "Abril", "Maio", "Junho",
         "Julho", "Agosto", "Setembro", "Outubro", "Novembro", "Dezembro"]
temperaturas = []

for i in range(12):
    temp = float(input(f"Digite a temperatura média de {meses[i]}: "))
    temperaturas.append(temp)

media_anual = sum(temperaturas) / len(temperaturas)
print(f"\nMédia anual: {media_anual:.2f}°C")
print("\nMeses acima da média:")
for i in range(12):
    if temperaturas[i] > media_anual:
        print(f"{meses[i]}: {temperaturas[i]}°C")

# Exercício 3: Enquete de sistemas operacionais
opcoes = ["Windows Server", "Unix", "Linux", "Netware", "Mac OS", "Outro"]
votos = [0] * 6

while True:
    voto = int(input("Vote (1-6) ou 0 para encerrar: "))
    if voto == 0:
        break
    elif 1 <= voto <= 6:
        votos[voto - 1] += 1
    else:
        print("Opção inválida.")

total_votos = sum(votos)

print("\nSistema Operacional    Votos   %")
print("-------------------   ------  ----")
for i in range(6):
    percentual = (votos[i] / total_votos) * 100 if total_votos > 0 else 0
    print(f"{opcoes[i]:<20} {votos[i]:>6}  {percentual:>5.1f}%")

print("-------------------   ------  ----")
print(f"Total                 {total_votos}")

mais_votado = max(votos)
indice_mais_votado = votos.index(mais_votado)
percentual_mais_votado = (mais_votado / total_votos) * 100 if total_votos > 0 else 0

print(f"\nO Sistema Operacional mais votado foi o {opcoes[indice_mais_votado]}, "
      f"com {mais_votado} votos, correspondendo a {percentual_mais_votado:.1f}% dos votos.")
