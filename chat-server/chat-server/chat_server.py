import socket
import select

port = 60003

sum == 1
def message(sum):
    if sum == sum:
        return str(sum) + "Client connected"

def klient(sum):
    if sum == sum:
        return str(sum) + "Client Disconnected"
   


sockL = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sockL.bind(("127.0.0.1", port))
sockL.listen(2)


listOfSockets = [sockL]


print("Listening to port {}".format(port))


while True:
   
   tup = select.select(listOfSockets, [], [])
   sock = tup[0][0]


   if sock==sockL:
     # TODO New client joins.
   
     # Call (sockClient, addr) = sockL.accept() and take care of the new client.
     (sockClient, addr) = sockL.accept()
      # print("New client joining")
     print(message(len(listOfSockets)), addr)
    
     for sock in listOfSockets:
                if sock != sockL:
                    sock.sendall (message(len(listOfSockets)).encode())
     # Put the client's socket into listOfSockets.
     listOfSockets.append(sockClient)
     
     
   else:
      # Existing client sending data or disconnecting...
      data = sock.recv(2048)
      if not data:
          # TODO handle Disconnected from sock.
          if sock in listOfSockets:
          # Close the socket connection and remove the socket from the list.
           listOfSockets.remove(sock)
           sock.close()
           print (klient(len(listOfSockets)), addr)
          for sock in listOfSockets:
           if sock != sockL:
               sock.sendall(klient(len(listOfSockets)).encode())
      else:
           # data is a message from the client.
           for sock in listOfSockets:
                    if sock != sockL:
                        sock.sendall(data)
                        sock.sendall(message(len(listOfSockets)).encode())
           # send this to all clients.

