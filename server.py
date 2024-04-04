import socket
import logging

def server(host = "localhost", port=8082):
    data_payload = 2048 #tamanho maximo da mensagem recebida
    
    #cria o socket tcp
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # habilita o re-uso do host e porta
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    # bind do socket na porta
    server_addres = (host, port)
    logging.getLogger("Server").info(f"Iniciando servidor no endereço e porta: {server_addres}")
    sock.bind(server_addres)
    # espera a conexão de até n clientes
    sock.listen(1)
    client = None
    i = 0

    while i < 5:
        if not client:
            logging.getLogger("Server").info("Aguardando conexão")
            client, address = sock.accept()
        #logging.getLogger("Server").info("Aguardando mensagem")
        data = client.recv(data_payload)
        logging.getLogger("Server").info("Aguardando mensagem")
        i += 1
        if data:
            logging.getLogger("Server").info(f"Mensagem recebida: {data}")
            #respondendo
            return_message = f"{data}".encode("utf-8")
            client.send(return_message)
            logging.getLogger("Server").info(f"Enviado para o client {address} a mensagem: {return_message}")
            i = 0
        if data == "close":
            client.close()
            logging.getLogger("Server").info("Conexão encerrada.")
    if i == 5:
        logging.getLogger("Server").info("Conexão encerrada por falta de comunicação")
        

if __name__ == "__main__":
    #FORMAT = '%(asctime)s %(clientip)-15s %(user)-8s %(message)s'
    FORMAT = '%(asctime)s | %(name)s | %(message)s'
    logging.basicConfig(
    level=logging.DEBUG,
    format=FORMAT
    )
    server()