import socket
import logging

def server(host = "::1", port=8082):
    data_payload = 2048 #tamanho maximo da mensagem recebida
    
    #cria o socket tcp
    sock = socket.socket(socket.AF_INET6, socket.SOCK_STREAM)
    # habilita o re-uso do host e porta
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    # bind do socket na porta
    server_addres = (host, port)
    logging.getLogger("Server").info(f"Iniciando servidor no endereço e porta: {server_addres}")
    sock.bind(server_addres)
    # espera a conexão de até n clientes
    sock.listen(1)
    client = None
    WAIT_FOR_CONNECTION = 0
    MAX_WAIT_FOR_CONNECTION = 5

    while WAIT_FOR_CONNECTION < MAX_WAIT_FOR_CONNECTION:
        if not client:
            logging.getLogger("Server").info("Aguardando conexão")
            client, address = sock.accept()
        data = client.recv(data_payload).decode()
        logging.getLogger("Server").info("Aguardando mensagem")
        WAIT_FOR_CONNECTION += 1
        if data:
            logging.getLogger("Server").info(f"Mensagem recebida: {data}")
            #respondendo
            return_message = f"{data}".encode()
            client.send(return_message)
            logging.getLogger("Server").info(f"Enviado para o client {address} a mensagem: {return_message}")
            i = 0
        if data == "close":
            client = client.close()
            logging.getLogger("Server").info("Conexão encerrada.")
    if WAIT_FOR_CONNECTION == MAX_WAIT_FOR_CONNECTION:
        logging.getLogger("Server").info("Conexão encerrada por falta de comunicação")
        

if __name__ == "__main__":
    #FORMAT = '%(asctime)s %(clientip)-15s %(user)-8s %(message)s'
    FORMAT = '%(asctime)s | %(name)s | %(message)s'
    logging.basicConfig(
    level=logging.DEBUG,
    format=FORMAT
    )
    server()