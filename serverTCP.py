import socket
import json
import threading
from random import uniform


HOST = '127.0.0.1' 
PORT = 65432
DOLARFATOR = uniform(2.0, 5.0)
EUROFATOR = uniform(3.0, 6.5)


def handle_client(conn, addr):
    """Lida com a comunicação de um cliente específico"""
    try:
        print(f"Conexão estabelecida com {addr}")
        with conn:
            while True:
                data = json.loads(conn.recv(1024).decode('utf-8'))
                if not data:
                    break  # Se não receber dados, encerra
                 # Depois colocar opção para Euro também
                 
                option, valor_Real = data
                fator = 0.0
                if option == 0:
                    fator = DOLARFATOR
                elif option == 1:
                    fator = EUROFATOR
                else:
                    print("algo de errado não está certo")
                
                print("teste")
                 
                valor_Real = float(valor_Real)
                valor_convertido = str( valor_Real * fator)
                print(f'{valor_Real} -> {valor_convertido}')
                # print(f"Recebido: {data.decode()}")
                conn.sendall(valor_convertido.encode())  # Envia os dados de volta
                break
    except Exception as e:
        print(f"Erro com {addr}: {e}")
    finally:
        print(f"{addr} desconectado")


def servidor():
     with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)  # Permite reusar porta
        s.bind((HOST, PORT))
        s.listen()
        print(f"Servidor escutando em {HOST}:{PORT} (Ctrl+C para parar)")

        try:
            while True:  # Aceita múltiplas conexões
                conn, addr = s.accept()
                client_thread = threading.Thread(target=handle_client, args=(conn, addr))
                client_thread.daemon = True  # Thread morre quando o main thread morrer
                client_thread.start()
                print(f"Conexões ativas: {threading.active_count() - 1}")
        except KeyboardInterrupt:
            print("\nServidor encerrando...")
        except Exception as e:
            print(f"Erro no servidor: {e}")

if __name__ == "__main__":
    servidor()