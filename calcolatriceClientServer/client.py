import socket

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(('127.0.0.1', 17710))

client.send(input("Inserire operazione:\n").encode("utf-8"))

print(client.recv(1024).decode())

client.send("|quit|".encode("utf-8"))
client.close()
