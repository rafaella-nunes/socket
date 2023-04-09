import socket

HOST = '127.0.0.1' 
PORT = 5000  

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    
    # Associa o socket ao endereço IP e porta utilizando o método bind da classe importada
    s.bind((HOST, PORT))

    # Procura por conexões e mensagens utilizando o método listen da classe importada
    s.listen()
    
    print('Aguardando conexões...')
    
    # Aceita a primeira conexão que chegar
    conexao, endereco = s.accept()
    with conexao:
        print('Conectado por', endereco)
        
        # Loop principal do servidor, enquanto nao receber uma mensagem vazia ele vai continuar a esperar mensagens
        while True:
            
            # Recebe a mensagem enviada pelo cliente
            data = conexao.recv(1024)
            
            # Se não houver mensagem (mensagem nula), encerra o loop
            if not data:
                break
            
            # Exibe os dados recebidos no terminal
            print(f'Dados recebidos: {data.decode()}')
            
            # Envia uma mensagem de confirmação de recebimento para o cliente
            conexao.sendall(b'Recebido')
