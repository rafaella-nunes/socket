import java.net.*;
import java.io.*;

public class ServidorSocket {
    public static void main(String[] args) throws IOException {
        ServerSocket servidorSocket = null;
        try {
            servidorSocket = new ServerSocket(2400); // Especifica a porta a ser usada
        } catch (IOException e) {
            System.err.println("Não foi possível abrir a porta 1234.");
            System.exit(1);
        }

        Socket clientSocket = null;
        try {
            clientSocket = servidorSocket.accept(); // Aguarda uma conexão
        } catch (IOException e) {
            System.err.println("Falha na conexão.");
            System.exit(1);
        }

        // Agora você pode usar o objeto Socket clientSocket para se comunicar com o cliente.
        // Por exemplo:
        PrintWriter out = new PrintWriter(clientSocket.getOutputStream(), true);
        out.println("Teste");

        // Feche a conexão.
        out.close();
        clientSocket.close();
        servidorSocket.close();
    }
}
