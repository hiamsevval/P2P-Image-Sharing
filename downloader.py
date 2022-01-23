
from socket import *
import os
import fnmatch
import time
import datetime
import json

 

user_filename = input('Which content do you want to download? ')

user_filename = user_filename[:-4]
user_filename += '_'

d = {}
with open('MyFile.txt', 'r') as f:
    d = f.readline()

d=eval(d)

serverName = '25.82.21.201' #user must update the serverip

chunk_d = {} 

os.listdir("C://Users//Şevval//Desktop//CMP2204-PROJE//chunks") #user must update the path
listOfFiles = os.listdir('.')
pattern = "*"

 

chunk_control = False  # check if any of the chunk is missing
for i in range(1, 6):
    new_filename = user_filename + str(i)
    chunk_d['requested_content'] = new_filename
    json_chunk_msg = json.dumps(chunk_d)
    f = open('C://Users//Şevval//Desktop//CMP2204-PROJE//chunks//' + new_filename, 'wb') #user must update the path
    
    chunk_found = False
    if new_filename in d:

        for value in d[new_filename]:
            if d[new_filename].length >11 and d[new_filename].length <16:
                value=d[new_filename]
            
            if chunk_found:
                break


            serverPort = 8000
            clientSocket = socket(AF_INET, SOCK_STREAM)
            clientSocket.connect((value, serverPort))
            clientSocket.send(json_chunk_msg.encode())

 

            while (1):
                print('Ready to connect')
                chunk = clientSocket.recv(1024)
                print("Receiving...")
                if not chunk:
                    break
                f.write(chunk)
            f.close()
    
            for entry in listOfFiles:
                if fnmatch.fnmatch(entry, pattern):
                    chunk_found = True
    
                    file1 = open('History.txt', 'a')
                    file1.write(new_filename + ' ')
                    file1.write(' is downloaded from ' + value)  # destination IP address
                    ct = datetime.datetime.now()
                    ts = time.time()
                    file1.write(' at ' + str(ct) + '(' + str(ts) + ')\n')
                    file1.close()

                    break
  
            clientSocket.close()
    if not chunk_found:
        chunk_control = True
        print('CHUNK' + new_filename + ' CANNOT BE DOWNLOADED FROM ONLINE PEERS.')


if not chunk_control:
    user_filename = user_filename[:-1]
    content_name = user_filename  # again, this'll be the name of the content that used wanted to download from the network.
    chunknames = [content_name + '_1', content_name + '_2', content_name + '_3', content_name + '_4',
                  content_name + '_5']

    user_filename += '.png'
    with open(user_filename, 'wb') as outfile:  # in your code change 'ece.png' to content_name+'.png'
        for chunk in chunknames:
            with open('C://Users//Şevval//Desktop//CMP2204-PROJE//chunks//' + chunk, 'rb') as infile:
                outfile.write(infile.read())
            infile.close()