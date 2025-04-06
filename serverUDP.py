import socket
import json
from random import uniform

HOST = '127.0.0.1' 
PORT = 65432
DOLARFATOR = uniform(2.0, 5.0)
EUROFATOR = uniform(3.0, 6.5)

def handle_client(data, addr):
    """Lida com a requisição de um cliente específico (UDP)"""
    try:
        print(f"Requisição recebida de {addr}")
        data = json.loads(data.decode('utf-8'))
        
        # Mantida a mesma lógica de conversão
        option, valor_Real = data
        fator = 0.0
        if option == 0:
            fator = DOLARFATOR
        elif option == 1:
            fator = EUROFATOR
        else:
            print("Opção inválida recebida")
        
        valor_Real = float(valor_Real)
        valor_convertido = str(valor_Real * fator)
        print(f'{valor_Real} -> {valor_convertido}')
        
        return valor_convertido.encode()
        
    except Exception as e:
        print(f"Erro com {addr}: {e}")
        return f"Erro: {e}".encode()
    finally:
        print(f"Requisição de {addr} processada")

def servidor():
    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:  # Alterado para SOCK_DGRAM
        s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        s.bind((HOST, PORT))
        print(f"Servidor UDP escutando em {HOST}:{PORT} (Ctrl+C para parar)")

        try:
            while True:
                # UDP: recebe dados e endereço com recvfrom()
                data, addr = s.recvfrom(1024)
                
                # Processa a requisição e envia resposta
                resposta = handle_client(data, addr)
                s.sendto(resposta, addr)  # UDP: envia com sendto()
                
        except KeyboardInterrupt:
            print("\nServidor encerrando...")
        except Exception as e:
            print(f"Erro no servidor: {e}")

if __name__ == "__main__":
    servidor()