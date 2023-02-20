import socket

import threading

"""
   hello peers its VURUDI100 again in this project is just nut simple client
   server socket connection implementation. i have tried as much to makesure
   i try to implement the OOP  programming concepts using the classes and 
   functions for you to understand these code you atlteast shoul have some
   basics on the object oriented programming in python
  """


client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
HOST = '127.0.0.1'
PORT = 5001
CONN = (HOST, PORT)
client.connect(CONN)
class Client:

    def recieve(self):
        while True:
            try:

                message = client.recv(1024).decode('ascii')
                if message == 'NICK':
                    nickname = input('chose a nickname:   ')
                    client.send(nickname.encode('ascii'))
                else:
                    print(message)
            except:
                print("\n\n what ever you entere wasnt a message")
                break

    def write(self):
        while True:
            message = input(" ")
            client.send(message.encode('ascii'))
            Client.recieve()
    
def run():
    recieve_thread = threading.Thread(target=Client.recieve)
    recieve_thread.start()
    write_thread = threading.Thread(target=Client.write)
    write_thread.start()
    
if __name__=='__main__':
    run()