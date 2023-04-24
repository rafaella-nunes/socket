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

    thread1 = threading.Thread(target=receber_mensagem, args=[cliente])
    thread2 = threading.Thread(target=enviar_mensagem, args=[cliente, username])

    thread1.start()
    thread2.start()

def enviar_mensagem(mensagem):
    mensagem_bytes = mensagem.encode('utf-8')
    cliente.send(mensagem_bytes)

    while True:
        mensagem = input("Digite uma mensagem que termine em 's': ")
        mensagem_valida = mensagem.strip().endswith('s')
        if mensagem_valida:
            enviar_mensagem(mensagem)
            # faça algo com a resposta do servidor aqui
        else:
            print("Mensagem inválida: a mensagem deve terminar em 's'")
