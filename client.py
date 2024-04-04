import socket
import logging

def client(host="::1", port=8082):
    sock = socket.socket(socket.AF_INET6, socket.SOCK_STREAM)
    # conexão
    server_address = (host, port, 0,0)
    logging.getLogger("Server").info(f"Tentando conectar ao servidor de endereço e porta {server_address}")
    sock.connect(server_address)
    logging.getLogger("Server").info("Conectado")
    try:
        #enviar dados
        message = "Testando mensagem 1".encode()
        logging.getLogger("Server").info(f"Enviando mensagem: {message}")
        sock.sendall(message)
        
        #Espera por uma resposta
        amount_received = 0
        amount_expected = len(message)
        while(amount_received < amount_expected):
            data = sock.recv(16).decode()
            amount_received += len(data)
            logging.getLogger("Server").info(f"Recebido: {data}")

        message = "close".encode()
        logging.getLogger("Server").info(f"Enviando mensagem: {message}")
        sock.sendall(message)   

        #Espera por uma resposta
        amount_received = 0
        amount_expected = len(message)
        while(amount_received < amount_expected):
            data = sock.recv(16).decode()
            amount_received += len(data)
            logging.getLogger("Server").info(f"Recebido: {data}")

    except socket.error as err:
        logging.getLogger("Server").info(f"Socket error: {str(err)}")
    except Exception as err:
        logging.getLogger("Server").info(f"Something went wrong. Error: {str(err)}")
    finally:
        logging.getLogger("Server").info("Fechando conexão com o servidor")
        sock.close()

if __name__ == "__main__":
    #FORMAT = '%(asctime)s %(clientip)-15s %(user)-8s %(message)s'
    FORMAT = '%(asctime)s | %(name)s | %(message)s'
    logging.basicConfig(
    level=logging.DEBUG,
    format=FORMAT
    )
    client()