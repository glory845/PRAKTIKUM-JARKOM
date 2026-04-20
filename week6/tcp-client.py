from socket import *

serverName = "localhost"
serverPort = 12000

clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((serverName, serverPort))

print("[SYSTEM] Masukkan pesan")

running = True

while running:
    message = input("> ")

    # kirim ke server
    clientSocket.send(message.encode())

    # jika exit keluar
    if message.lower() == "exit":
        print("[SYSTEM] keluar dari program")
        running = False
        break

    # terima balasan server
    modifiedMessage = clientSocket.recv(2048)

    print("[SERVER] pesan:", modifiedMessage.decode())

clientSocket.close()
print("[SYSTEM] socket ditutup")