import socket
import threading

max_connections = 10

HOST = 'localhost'
PORT = 5000

def handle_client(conexao):
    while True:
        data = conexao.recv(1024).decode() # receber a mensagem
        if not data:
            conexao.close()
        if data.endswith('s'):
            conexao.send('Mensagem recebida com sucesso!'.encode()) # enviar a confirmação
        else:
            conexao.send('Mensagem não terminada em "s". Tente novamente.'.encode()) # enviar mensagem de erro
    conexao.close() # fechar a conexão


def servidor():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # criar o socket do servidor
    server_socket.bind((HOST, PORT)) 
    server_socket.listen(max_connections) 
    print(f'Servidor iniciado em {HOST}:{PORT}')

    while True:
        conexao, endereco = server_socket.accept() # aceitar uma nova conexão
        print(f'Nova conexão recebida de {endereco}')
        thread = threading.Thread(target=handle_client, args=(conexao,)) # criar uma nova thread para lidar com a conexão
        thread.start() # iniciar a thread


def tratar_mensagem(mensagem):
    mensagem = mensagem.strip() # remove espaços em branco no início e fim da mensagem
    if mensagem.endswith('s'): # verifica se a mensagem termina em "s"
        return mensagem
    else:
        return None

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as servidor:
    servidor.bind((HOST, PORT))
    servidor.listen()
    print(f"Servidor ouvindo em {HOST}:{PORT}")

    conexao, endereco_cliente = servidor.accept()
    print(f"Conexão estabelecida com {endereco_cliente}")

    with conexao:
        while True:
            dados = conexao.recv(1024) # recebe até 1024 bytes de dados
            mensagem = dados.decode('utf-8')
            mensagem_valida = tratar_mensagem(mensagem)
            if mensagem == 'tchau':
                break
            elif mensagem_valida:
                print(f"Nova mensagem recebida: {mensagem_valida}")
            else:
                print(f"Mensagem inválida: {mensagem}")
