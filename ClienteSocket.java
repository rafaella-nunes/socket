import java.net.*;
import java.io.*;

public class ClienteSocket {
    public static void main(String[] args) throws IOException {
        String servidorNome = "localhost"; // O nome ou endereço IP do servidor
        int servidorPorta = 2400; // A porta em que o servidor está ouvindo

        Socket socket = null;
        PrintWriter out = null;
        BufferedReader in = null;

        try {
            socket = new Socket(servidorNome, servidorPorta); // Conecta ao servidor
            out = new PrintWriter(socket.getOutputStream(), true);
            in = new BufferedReader(new InputStreamReader(socket.getInputStream()));
        } catch (UnknownHostException e) {
            System.err.println("Endereço do servidor inválido: " + servidorNome);
            System.exit(1);
        } catch (IOException e) {
            System.err.println("Não foi possível conectar ao servidor " + servidorNome);
            System.exit(1);
        }

        // Agora você pode usar o objeto PrintWriter out para enviar mensagens para o servidor.
        // Por exemplo:
        out.println("Olá, servidor!");

        // Receba a resposta do servidor.
        String resposta = in.readLine();
        System.out.println("Servidor: " + resposta);

        // Feche a conexão.
        out.close();
        in.close();
        socket.close();
    }
}
