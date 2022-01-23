import os
import math
import fnmatch
import time
from socket import *
import json

from collections import defaultdict

cs = socket(AF_INET, SOCK_DGRAM)
cs.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
cs.setsockopt(SOL_SOCKET, SO_BROADCAST, 1)

os.listdir("C://Users//Şevval//Desktop//CMP2204-PROJE")#Users must update the path addresses

 

listOfFiles = os.listdir('.') #to search the contents that user has
pattern = "*.png"
print("Choose a file name without entering '.png' ")
for entry in listOfFiles:
    if fnmatch.fnmatch(entry, pattern):
        print(entry)

 

content_name = input("--> ")#Enter the name of the content to be downloaded.
filename = content_name + '.png'

 


c = os.path.getsize(filename) #dividing the content
CHUNK_SIZE = math.ceil(math.ceil(c) / 5)

 

save_path = r'C://Users//Şevval//Desktop//CMP2204-PROJE//chunks'

 

if not os.path.exists(save_path):
    os.makedirs(save_path)
index = 1
with open(filename, 'rb') as infile:
    chunk = infile.read(int(CHUNK_SIZE))
    while chunk:
        chunkname = content_name + '_' + str(index)
        completeName = os.path.join(save_path, chunkname)
        with open(completeName, 'wb+') as chunk_file:
            chunk_file.write(chunk)
        index += 1
        chunk = infile.read(int(CHUNK_SIZE))
chunk_file.close()

 


print('There are 5 chunks which named: ')
for i in range(1, 6):
    print(content_name + "_" + str(i) + ", ")

 

print('Announcing process has started with these chunks')

while True:
    a_dictionary = defaultdict(list)
    
     
    
    pattern1 = "*" #read the names into the dictionary
    listOfFiles1 = os.listdir(save_path)
    for entry in listOfFiles1:
        if fnmatch.fnmatch(entry, pattern1):
            a_dictionary['chunks'].append(entry)
    
         
    json_obj = json.dumps(a_dictionary)

    cs.sendto(json_obj.encode("utf-8"), ('25.255.255.255', 5001))#broadcast message
    print('Sending...')
    time.sleep(15)