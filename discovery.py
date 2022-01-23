
def append_value(dict_obj, key, value):
    # Check if key exist in dict or not
    if key in dict_obj:
        # Key exist in dict.
        # Check if type of value of key is list or not
        if not isinstance(dict_obj[key], list):
            # If type is not list then make it list
            dict_obj[key] = [dict_obj[key]]
        # Append the value in list
        dict_obj[key].append(value)
    else:
        # As key is not in dict,
        # so, add key-value pair
        dict_obj[key] = value




from socket import *
import json

serverPort = 5001

# Create a UDP socket
serverSocket = socket(AF_INET, SOCK_DGRAM)

# Bind the socket to the port
serverSocket.bind(('', serverPort))
print("The server is ready to receive")

content_dic = {}

while 1:
    message, clientAddress = serverSocket.recvfrom(2048)
    ip = clientAddress[0]
    print('received {} bytes from {}'.format(len(message.decode()), ip))
    y = json.loads(message.decode())  # y.keys()="chunks"

    print(' {} : {}'.format(ip, y.values()))

    x = list(y.values())

    for j in x:
        for i in j:
            if i not in content_dic:
                content_dic[i] = ip
            else:
                if ip not in content_dic[i]:
                    append_value(content_dic,i,ip)

    file1 = open("MyFile.txt", "w")
    file1.write(str(content_dic))
    file1.close()