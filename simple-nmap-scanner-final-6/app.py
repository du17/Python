from flask import Flask, render_template, request, jsonify
import socket
import threading
from datetime import datetime

app = Flask(__name__)

# Lista para armazenar portas abertas
portas_abertas = []

def verificar_porta(host, porta):
    """Função simples para verificar se uma porta está aberta"""
    try:
        # Cria um socket
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)  # Timeout de 1 segundo
        
        # Tenta conectar
        resultado = sock.connect_ex((host, porta))
        sock.close()
        
        # Se resultado é 0, a porta está aberta
        if resultado == 0:
            portas_abertas.append(porta)
            return True
        return False
    except:
        return False

def escanear_portas(host, porta_inicial, porta_final):
    """Função para escanear um range de portas"""
    global portas_abertas
    portas_abertas = []  # Limpa a lista
    
    print(f"Iniciando scan em {host} das portas {porta_inicial} até {porta_final}")
    
    # Lista de threads para fazer scan mais rápido
    threads = []
    
    for porta in range(porta_inicial, porta_final + 1):
        # Cria uma thread para cada porta
        thread = threading.Thread(target=verificar_porta, args=(host, porta))
        threads.append(thread)
        thread.start()
        
        # Limita o número de threads simultâneas
        if len(threads) >= 50:
            for t in threads:
                t.join()
            threads = []
    
    # Espera todas as threads terminarem
    for t in threads:
        t.join()
    
    portas_abertas.sort()  # Ordena as portas
    return portas_abertas

@app.route('/')
def index():
    """Página principal"""
    return render_template('index.html')

@app.route('/scan', methods=['POST'])
def scan():
    """Endpoint para fazer o scan"""
    try:
        # Pega os dados do formulário
        host = request.form['host']
        porta_inicial = int(request.form['porta_inicial'])
        porta_final = int(request.form['porta_final'])
        
        # Valida os dados
        if porta_inicial > porta_final:
            return jsonify({'erro': 'Porta inicial deve ser menor que a final'})
        
        if porta_inicial < 1 or porta_final > 65535:
            return jsonify({'erro': 'Portas devem estar entre 1 e 65535'})
        
        # Faz o scan
        inicio = datetime.now()
        portas = escanear_portas(host, porta_inicial, porta_final)
        fim = datetime.now()
        
        tempo_total = (fim - inicio).total_seconds()
        
        return jsonify({
            'sucesso': True,
            'host': host,
            'portas_abertas': portas,
            'total_portas': len(portas),
            'tempo': f"{tempo_total:.2f} segundos"
        })
        
    except Exception as e:
        return jsonify({'erro': str(e)})

if __name__ == '__main__':
    print("=== SCANNER DE PORTAS SIMPLES ===")
    print("Acesse: http://localhost:5000")
    print("Para parar: Ctrl+C")
    app.run(debug=True, host='0.0.0.0', port=5000)
