# Chức năng 6 : Gửi nhiều requests trong một connection  khi download file trong folder

import socket
import sys
import threading
import os.path
from os import path
import os
from bs4 import BeautifulSoup
from function.request import *
from function.getheader import *
from function.writeFileChunked import *


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.settimeout(10)

def handle_request(request):

    HOST = request.host
    PORT = 80
    DATABASE = request.content
    PATH = request.path
    URL = request.url

    server_address = (HOST, PORT)
    
    try:

        if s == None:
            s.connect(server_address)
            print('Connecting to server ' + str(server_address) + '\n\n')

        path = request.path + request.content

        requestx = "GET " + path + \
            " HTTP/1.1\r\nConection:Keep-Alive\r\nHost:" + HOST + "\r\n\r\n"

        s.sendall(requestx.encode())

        getheader = headerrespone(s)

        length = getheader[0]
        
        if length != -1:
            getContent_Length(s, length, HOST, PATH, DATABASE, URL)

        else:
            getChunked(s, HOST, PATH, DATABASE)

    except Exception as e:
        print(e)



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
        
    downloadSubFolder(response, HOST, path, URL)
    
    print('\nDownload Subfolder successful\n')

 
def downloadSubFolder(mainResponse, mainHOST, mainPATH, mainURL):
    
    soup = BeautifulSoup(mainResponse, "html.parser")
    filestype = '.'

    folder_path = './write_file/Content_Length/' + mainHOST + '_' + mainPATH
    
    if os.path.exists(folder_path) == False:
        os.mkdir(folder_path)

    for link in soup.find_all('a', href=True):
        filelink = link.get('href')

        if filestype in filelink:
            
            suburl = mainURL + filelink


            if "%20" in filelink:
                filelink = filelink.replace("%20"," ")
            
            request = RequestParse(suburl)
            HOST = request.host
            PORT = 80
            DATABASE = request.content
            PATH = request.path

            server_address = (HOST, PORT)
            try:
                
                subpath = request.path + request.content

                request = "GET " + subpath + \
                    " HTTP/1.1\r\nConection:Keep-Alive\r\nHost:" + HOST + "\r\n\r\n"

                s.sendall(request.encode())

                getheader = headerrespone(s)
                length = getheader[0]
                
                response = b""
                while True:
                    data = s.recv(length-len(response))
                    if len(response) == length:
                        break
                    else:
                        response += data
                    with open('./' + folder_path + '/' + filelink, 'wb') as f:
                        f.write(response)
                print('Download data successful.\n')
                    
            except socket.timeout as e:
                print('Download Sub File unsuccessful.\n')


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


request = getrequest()

connect(request)

handle_request(request)

s.close()
