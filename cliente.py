import socket
import threading


def cliente():
    cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    try:
        cliente.connect(('localhost', 5000))
    except:
        return print('\nNão foi possível conectar ao servidor!\n')

    username = input('Nome de usuário: ')
    print('\nConectado!\n')

    thread1 = threading.Thread(alvo=receber_mensagem, args=[cliente])
    thread2 = threading.Thread(
        alvo=enviar_mensagem, args=[cliente, username])

    thread1.start()
    thread2.start()


def receber_mensagem(cliente):
    while True:
        try:
            mensagem = cliente.recv(4096).decode('utf-8')
            print(mensagem + '\n')
        except:
            print('\nSua conexão foi encerrada inesperadamente!\n')
            cliente.close()
            break


def enviar_mensagem(cliente, username):
    while True:
        try:
            mensagem = input('Digite sua mensagem: ')
            if mensagem == 'sair':
                cliente.close()
            else:
                cliente.send(f'<{username}> {mensagem}'.encode('utf-8'))
        except:
            return


cliente()
