import socket

HOST = '127.0.0.1'  
PORT = 5000  

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    
    # Conecta ao servidor utilizando o método connect da classe importada
    s.connect((HOST, PORT))
    
    # Loop principal do cliente
    while True:
    
        mensagem = input('Mensagem: ')
        
        # Se a mensagem for vazia, encerra o loop
        if not mensagem:
            break
        
        # Envia a mensagem para o servidor
        s.sendall(mensagem.encode())
        
        # Recebe a confirmação de que chegou no servidor
        data = s.recv(1024)
        
        # Exibe a mensagem recebida
        print(f'Resposta do servidor: {data.decode()}')
