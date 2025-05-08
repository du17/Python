
# Perguntas (Teóricas)

# 1️ Como podemos determinar o tamanho de uma tupla?
T = (1, 2, 3)
print("Tamanho da tupla:", len(T))  # Retorna 3

# 2️ Escreva uma expressão que altere o primeiro item da tupla (4, 5, 6) para (1, 5, 6)
T = (4, 5, 6)
T = (1,) + T[1:]
print("Tupla alterada:", T)

# 1️ Descreva dois modos de construirmos uma lista contendo cinco valores inteiros nulos
lista1 = [0] * 5
lista2 = [0 for i in range(5)]
print("Lista 1:", lista1)
print("Lista 2:", lista2)

# 2️ Cite quatro operações que alterem um objeto da classe list
lista = [3, 1, 2]
lista.append(4)
lista.sort()
lista.remove(1)
lista.insert(0, 10)
print("Lista alterada:", lista)

# Exercícios (Programação)

# 1️ Vetores intercalados
vetor1 = []
vetor2 = []
vetor3 = []

print("\n--- Vetores Intercalados ---")
for i in range(10):
    vetor1.append(int(input(f"Digite o {i+1}º valor do primeiro vetor: ")))
for i in range(10):
    vetor2.append(int(input(f"Digite o {i+1}º valor do segundo vetor: ")))

for i in range(10):
    vetor3.append(vetor1[i])
    vetor3.append(vetor2[i])

print("Vetor Intercalado:", vetor3)

# 2️ Temperaturas médias
meses = ["Janeiro", "Fevereiro", "Março", "Abril", "Maio", "Junho",
         "Julho", "Agosto", "Setembro", "Outubro", "Novembro", "Dezembro"]
temperaturas = []

print("\n--- Temperaturas Médias ---")
for i in range(12):
    temp = float(input(f"Digite a temperatura média de {meses[i]}: "))
    temperaturas.append(temp)

media_anual = sum(temperaturas) / len(temperaturas)
print(f"\nMédia anual de temperatura: {media_anual:.2f}°C")

print("\nMeses com temperatura acima da média:")
for i in range(12):
    if temperaturas[i] > media_anual:
        print(f"{meses[i]}: {temperaturas[i]}°C")

# 3️ Enquete de Sistemas Operacionais
opcoes = ["Windows Server", "Unix", "Linux", "Netware", "Mac OS", "Outro"]
votos = [0] * 6

print("\n--- Enquete Sistemas Operacionais ---")
while True:
    voto = int(input("Vote (1-6) ou 0 para encerrar: "))
    if voto == 0:
        break
    elif 1 <= voto <= 6:
        votos[voto - 1] += 1
    else:
        print("Opção inválida. Tente novamente.")

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