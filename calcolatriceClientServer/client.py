import socket

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(('127.0.0.1', 8844))

print ('''
Formato operazione: NUMERO1 OPERAZIONE NUMERO2
Operatori disponibili:
    + -> Addizione
    - -> Sottrazione
    * -> Moltiplicazione
    / -> Divisione
        ''')

ctrl = True
while (ctrl) :
    client.send(input("Inserire operazione:\n").encode("utf-8"))

    print(client.recv(1024).decode())

    rispostaUtente = input("Continuare ad eseguire operazioni?\n").lower()
    if (rispostaUtente == "si") :
        ctrl = True
    else :
        ctrl = False

client.send("QUIT".encode("utf-8"))
client.close()
