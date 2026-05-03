from socket import *
import threading
import os

def handle_client(connectionSocket):
    try:
        # menerima request dari client
        message = connectionSocket.recv(1024).decode()
        print("Request:\n", message)

        # ambil nama file
        filename = message.split()[1]
        filepath = filename[1:]  # hapus "/"

        # default ke index.html jika root
        if filepath == "":
            filepath = "index.html"

        # cek apakah file ada
        if os.path.exists(filepath):
            with open(filepath, 'r') as f:
                outputdata = f.read()

            # kirim HTTP 200 OK
            connectionSocket.send("HTTP/1.1 200 OK\r\n\r\n".encode())
            connectionSocket.sendall(outputdata.encode())
        else:
            raise IOError

        connectionSocket.close()

    except:
        # jika file tidak ditemukan
        connectionSocket.send("HTTP/1.1 404 Not Found\r\n\r\n".encode())
        connectionSocket.send("<h1>404 Not Found</h1>".encode())
        connectionSocket.close()

serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.bind(('', 6789))
serverSocket.listen(5)

print("Server multithread berjalan di port 6789...")

while True:
    connectionSocket, addr = serverSocket.accept()
    print("Terhubung dari:", addr)

    # buat thread baru untuk setiap client
    thread = threading.Thread(
        target=handle_client,
        args=(connectionSocket,)
    )
    thread.start()