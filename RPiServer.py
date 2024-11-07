from Client import messageFromClient, messageFromClient_bytes

if __name__ == "__main__" :
    print("\033cStarting ...\n") # Clear Terminal

import socket
import time
import sys
import os

try :
    import dotenv # pip install python-dotenv
except ModuleNotFoundError:
    sys.exit('No module named dotenv try : pip install python-dotenv')

dotenv.load_dotenv()

bufferSize = 1024
serverPort = int(os.getenv('serverPort_env'))
serverIP = os.getenv('serverIP_env')

RPi_Socket = socket.socket(socket.AF_INET,socket.SOCK_DGRAM) # Using UTP
RPi_Socket.bind((serverIP,serverPort))

print('\033cServer is Up')

try :
    Done = False
    while not Done :
        messageReceived, clientAddress = RPi_Socket.recvfrom(bufferSize)
        messageReceived = messageReceived.decode('utf-8')
        print(f'The message is : {messageReceived}')#\nFrom : \t\t\t{clientAddress[0]}\nOn port number {clientAddress[1]}')

        if messageFromClient == 'Done' :
            Done = True
            messageFromServer = f'{messageFromClient} Received'
            messageFromServer_bytes = messageFromServer.encode('utf-8')
            RPi_Socket.sendto(messageFromServer_bytes, clientAddress)

        elif messageFromClient == 'grab' :
            messageFromServer = f'{messageFromClient} Received'
            messageFromServer_bytes = messageFromServer.encode('utf-8')
            RPi_Socket.sendto(messageFromServer_bytes, clientAddress)

        elif messageFromClient == 'walk' :
            messageFromServer = f'{messageFromClient} Received'
            messageFromServer_bytes = messageFromServer.encode('utf-8')
            RPi_Socket.sendto(messageFromServer_bytes, clientAddress)

        elif messageFromClient == 'down' :
            messageFromServer = f'{messageFromClient} Received'
            messageFromServer_bytes = messageFromServer.encode('utf-8')
            RPi_Socket.sendto(messageFromServer_bytes, clientAddress)

except KeyboardInterrupt :
    pass

print('Programme Stopped')

