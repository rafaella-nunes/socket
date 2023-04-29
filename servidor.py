import socket
import threading

clientes = []

HOST = 'localhost'
PORT = 5000


def servidor():

    servidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    try:
        servidor.bind((HOST, PORT))
        servidor.listen()
    except:
        return print('\nNão foi possível iniciar o servidor!\n')

    while True:
        cliente, endereco = servidor.accept()
        clientes.append(cliente)

        thread = threading.Thread(target=tratar_mensagem, args=[cliente])
        thread.start()


def tratar_mensagem(cliente):
    while True:
        try:
            mensagem = cliente.recv(4096)
            if mensagem != 'sair':
                broadcast(mensagem, cliente)
            else:
                apagar_cliente(cliente)
        except:
            apagar_cliente(cliente)
            break


def broadcast(mensagem, cliente):
    for clienteItem in clientes:
        if clienteItem != cliente:
            try:
                clienteItem.send(mensagem)
            except:
                apagar_cliente(clienteItem)

# remove cliente da lista


def apagar_cliente(cliente):
    clientes.remove(cliente)


servidor()
