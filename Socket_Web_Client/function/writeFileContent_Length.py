# Download và  Save thành dạng Content_Length."

import socket
import sys
import os
from function.downsubfolder import *


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

    folder_path = './write_file/' + 'Content_Length'
    if os.path.exists(folder_path) == False:
        os.mkdir(folder_path)

    if len(DATABASE) == 0 and len(PATH) == 1:
        with open('./' + folder_path + '/' + HOST + "_index.html", 'wb') as f:
            f.write(response)
            
    elif len(DATABASE) == 0 and len(PATH) != 1:
        downloadSubFolder(response, HOST, path, URL)
        
    elif len(DATABASE) != 0:
        with open('./' + folder_path + '/' + HOST + '_' + DATABASE, 'wb') as f:
            f.write(response)
            
    print('\nDownload data successful\n\n')
