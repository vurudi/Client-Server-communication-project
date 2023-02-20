import threading
import socket

"""
   hello peers its VURUDI100 again in this project is just nut simple client
   server socket connection implementation. i have tried as much to makesure
   i try to implement the OOP  programming concepts using the classes and 
   functions for you to understand these code you atlteast shoul have some
   basics on the object oriented programming in python
  """

HOST = '0.0.0.0'
PORT = 5001
nec= (HOST, PORT)
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(nec)
server.listen()
clients_list = []
names_list = []
class Server:
    #OOP BASICS WITH SOCKET PROGRAMMING BE sure to read throgh the readme file
# you can expand this project to fit your needs 

    def broadcast(messege):
        for client in clients_list:
            client.send(messege)

    def handle(client):
        while True:
            try:
                messege = client.recv(1024)
                Server.broadcast(messege)
            except:
                index = clients_list.index(client)
                clients_list.remove(client)
                client.close()
                nickname = names_list[index]
                Server.broadcast(f'{nickname} left the chart'.encode('ascii'))
                names_list.remove(nickname)
                break

    # noinspection PyTypeChecker
    def receive(self):
        print("server is running... ready for connections")
        while True:
            client, address = server.accept()
            print(f'connected with{str(address)}')

            client.send('NICK'.encode('ascii'))
            nickname = client.recv(1024).decode('ascii')
            names_list.append(nickname)
            clients_list.append(client)

            print(f'the current connected device is  {nickname}')
            Server.broadcast(f'{nickname} joined the chart'.encode('ascii'))
            num = len(clients_list)
            print(num)
            client.send(f'{nickname}   you have successfully connected to the server'.encode('ascii'))
            Server.handle(client)
            try:
                thread = threading.Thread(target=Server.handle, args=client)
                thread.start()
            except:
                print(" failed ")

if __name__=='__main__':
    Server.receive('null')