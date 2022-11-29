# Thực hiện các chức năng tải file cơ bản và lưu tại folder tương ứng : Content_Length và Chunk.

import socket
from function.request import *
from function.getheader import *
from function.writeFileContent_Length import *
from function.writeFileChunked import *

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.settimeout(10)

request = getrequest()

HOST = request.host
PORT = 80
DATABASE = request.content
PATH = request.path
URL = request.url

server_address = (HOST, PORT)

try:

    s.connect(server_address)
    print('Connecting to server ' + str(server_address))

    path = request.path + request.content

    request = "GET " + path + \
        " HTTP/1.1\r\nConection:Keep-Alive\r\nHost:" + HOST + "\r\n\r\n"

    s.sendall(request.encode())
    getheader = headerrespone(s)
    length = getheader[0]

    if length != -1:
        getContent_Length(s, length, HOST, PATH, DATABASE, URL)
    else:
        getChunked(s, HOST, PATH, DATABASE)

    s.close()

except socket.timeout as e:
    print("Time Out!")
