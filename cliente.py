import socket

HOST = 'localhost'
PORT = 5000

def enviar_mensagem(mensagem):
    mensagem_bytes = mensagem.encode('utf-8')
    cliente.send(mensagem_bytes)

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as cliente:
    cliente.connect((HOST, PORT))
    print(f"Conexão estabelecida com {HOST}:{PORT}")

    while True:
        mensagem = input("Digite uma mensagem que termine em 's': ")
        mensagem_valida = mensagem.strip().endswith('s')
        if mensagem_valida:
            enviar_mensagem(mensagem)
            # faça algo com a resposta do servidor aqui
        else:
            print("Mensagem inválida: a mensagem deve terminar em 's'")
