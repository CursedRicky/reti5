import socket

port = 17710

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# Indirizzo 0.0.0.0 per auto assegnazione dell'ip del server
server.bind(('0.0.0.0', port))

server.listen()
print("Server in ascolto sulla porta: " + str(port))


def handle(client):
    while True:
        msg = client.recv(1024).decode()
        if len(str(msg)) != 0:
            if msg == "|quit|":
                break
            else:
                # Sostituisci la x con il * per darle valore di moltiplicazione
                tot = eval(msg.replace("x", "*"))
                client.send(("Risultato: " + str(tot)).encode("utf-8"))

    # Connessione terminata, torna ad ascoltare
    print("Client disconnesso")
    ascolta()


def ascolta():
    print("...aspettando client...")
    connectedClient = []
    while True:
        client, indirizzo = server.accept()
        print(f"Connessione da {str(indirizzo)}")

        connectedClient = client
        break
    handle(connectedClient)


ascolta()



