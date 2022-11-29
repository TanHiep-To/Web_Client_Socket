# Chức năng 6 : Gửi nhiều requests trong một connection  khi download file trong folder

import socket
import sys
import threading
import os.path
from os import path
import os
from function.request import *
from function.getheader import *
from function.writeFileChunked import *
from function.downsubfolder import *


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.settimeout(10)


def handle_request(request):

    HOST = request.host
    PORT = 80
    DATABASE = request.content
    PATH = request.path
    URL = request.url

    if len(URL) == 0:
        return False

    server_address = (HOST, PORT)
    try:

        if s == None:
            s.connect(server_address)
            print('Connecting to server ' + str(server_address) + '\n\n')

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

    except Exception as e:
        print(e)

    return True


def getContent_Length(s, length, HOST, PATH, DATABASE, URL):

    response = b""

    try:
        while True:
            data = s.recv(length-len(response))
            if len(response) == length:
                break
            else:
                response += data
    except socket.timeout as e:
        print('Get Data unsuccessful\n\n')

    document = PATH.split("/")
    path = document[len(document) - 2]

    mainfolder_path = './write_file/' + 'Content_Length'
    if os.path.exists(mainfolder_path) == False:
        os.mkdir(mainfolder_path)

    folder_path = './' + mainfolder_path + '/' + HOST
    if os.path.exists(folder_path) == False:
        os.mkdir(folder_path)
        with open('./' + folder_path + '/' + HOST + '_' + DATABASE, 'wb') as f:
            f.write(response)
        print('\nDownload data successful\n')
    else:
        with open('./' + folder_path + '/' + HOST + '_' + DATABASE, 'wb') as f:
            f.write(response)
        print('\nDownload data successful\n')


def connect(request):

    HOST = request.host
    PORT = 80
    DATABASE = request.content
    PATH = request.path
    URL = request.url
    server_address = (HOST, PORT)

    try:

        s.connect(server_address)
        print('Connecting to server ' + str(server_address) + '\n\n')

    except Exception as e:
        print(e)


ok = 0
while True:

    request = getrequest()

    if ok == 0:

        connect(request)
        ok = 1

    check = handle_request(request)
    if check == False:
        break

s.close()
