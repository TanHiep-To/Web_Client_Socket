# Dowload file trong folder.

import socket
import os
from bs4 import BeautifulSoup
from function.request import *
from function.getheader import *
import string


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
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.settimeout(10)

            request = RequestParse(suburl)
            HOST = request.host
            PORT = 80
            DATABASE = request.content
            PATH = request.path

            server_address = (HOST, PORT)

            if "%20" in filelink:
                filelink = filelink.replace("%20"," ")
                
            try:
                s.connect(server_address)
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

                s.close()
            except socket.timeout as e:
                print('Download Sub File unsuccessful\n')
