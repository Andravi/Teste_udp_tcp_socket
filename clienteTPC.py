import socket
import json


def cliente():
    HOST = "127.0.0.1"
    PORT = 65432

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        print("Converta seu dinheiro!")
        print("=" * 30)
        print("1 -> Dolar")
        print("2 -> Euro")
        print("Escolha uma das opções acima para conversão:")
        option = int(input(""))
        valor_real = input("Digite o valor a ser convertido: R$ ")
        # Depois colocar uma captura de erros aqui
        s.connect((HOST, PORT))  # Conecta ao servidor
        s.sendall(json.dumps((1, valor_real)).encode("utf-8"))

        valor_convertido = s.recv(1024)  # Recebe a resposta do servidor
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
