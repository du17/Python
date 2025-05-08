import socket
import sys
from datetime import datetime

# Limpa a tela
print("-" * 50)
print("Scanner de Portas Simples")
print("-" * 50)

# Solicita entrada
alvo = input("Digite o endereço IP alvo: ")

# Adiciona um banner bonito
print("-" * 50)
print(f"Escaneando alvo: {alvo}")
print(f"Hora de início: {datetime.now()}")
print("-" * 50)

try:
    # Escaneia portas entre 1 e 1024
    for porta in range(1, 1025):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket.setdefaulttimeout(1)
        
        # Retorna um indicador de erro
        resultado = s.connect_ex((alvo, porta))
        if resultado == 0:
            print(f"Porta {porta}: Aberta")
        s.close()

except KeyboardInterrupt:
    print("\nSaindo do programa.")
    sys.exit()
except socket.gaierror:
    print("\nNão foi possível resolver o nome do host.")
    sys.exit()
except socket.error:
    print("\nNão foi possível conectar ao servidor.")
    sys.exit()

print("\nEscaneamento completo.")