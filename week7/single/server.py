from socket import *
import sys
import threading

def handle_client(connectionSocket):
  try:
    # menerima pesan dari client dan menampilkanya di server
    message = connectionSocket.recv(1024).decode()
    print(f"Diterima dari client: {message}")
    
    # melakukan operasi yg diminta client, dalam hal ini adalah membaca file dan mengirimkan isinya kembali ke client
    # misalnya client mengirim message = "file.txt", maka server akan membaca file.txt dan mengirimkan isinya kembali ke client
    filename = message.split()[1] # menghapus karakter pertama, dengan asumsi client mengirimkan nama file dengan format "/filename"
    
    # membuka file dan membaca isinya, lalu mengirimkan isi file kembali ke client
    f = open(filename[1: ])
    
    # membaca isi file dan mengirimkannya kembali ke client
    outputdata = f.read()
    
    # kirim respon HTTP 200 OK ke client
    connectionSocket.send(
      "HTTP/1.1 200 OK\r\n\r\n".encode()
    )
    
    #kirim data file ke client
    connectionSocket.sendall(outputdata.encode())
    
    # menutup koneksi dengan client setelah selesai mengirim data
    connectionSocket.close()
  except IOError:
    # jika file tidak ditemukan, kirim respon HTTP 404 Not Found ke client
    connectionSocket.send(
      "HTTP/1.1 404 Not Found\r\n\r\n".encode()
    )
    
    # kirim data error ke client
    connectionSocket.send(
      "<h1>404 Not Found</h1>".encode()
    )
    # menutup koneksi dengan client setelah selesai mengirim data
    connectionSocket.close()



serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.bind(('', 6789))
serverSocket.listen(5) # Maksimal 5 koneksi yang menunggu
print("Server TCP siap menerima koneksi pada port 6789")

while True:
  connectionSocket, addr = serverSocket.accept()
  # membuat thread dan target threadnya, beserta parameter yang akan dikirim ke fungsi handle_client
  thread = threading.Thread(
    target=handle_client,
    args=(connectionSocket, )
 )
  thread.start()