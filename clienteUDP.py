import socket
import json

HOST = '127.0.0.1'
PORT = 65432

def cliente():
    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:  # Alterado para SOCK_DGRAM
        print("Converta seu dinheiro!")
        print("=" * 30)
        print("1 -> Dolar")
        print("2 -> Euro")
        print("Escolha uma das opções acima para conversão:")
        option = int(input(""))
        valor_real = input("Digite o valor em R$: ")
        
        
        data = json.dumps([int(option), valor_real]).encode('utf-8')
        
        s.sendto(data, (HOST, PORT))
        
        valor_convertido, _ = s.recvfrom(1024)
        valor_convertido = float(valor_convertido.decode())
        if option == 1:
            print(
                f"R$ {valor_real.replace('.',',')} são ${str(round(valor_convertido,2)).replace('.',',')} Dolares"
            )
        elif option == 2:
            print(
                f"R$ {valor_real.replace('.',',')} são ${str(round(valor_convertido,2)).replace('.',',')} Euros"
            )
        else:
            print("algo errado...")
            
            

if __name__ == "__main__":
    cliente()