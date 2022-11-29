# Download và  Save thành dạng "Transfer - Encoding : chunked"

import socket
import os
import string
import sys
from function.request import *


def is_hex(s):
    try:
        int(s, 16)
        return True
    except ValueError:
        return False


def getChunked(s, HOST, PATH, DATABASE):

    response = b""

    try:
        while True:
            chunkdata = s.recv(10000000)
            chunkposition = 0

            if len(chunkdata) == 0:
                break
            else:
                while True:

                    rnposition = chunkdata.find(b"\r\n", chunkposition)

                    if rnposition == -1:
                        str2 = chunkdata[chunkposition:]
                        response += str2
                        break

                    Str = chunkdata[chunkposition:rnposition]

                    if is_hex(Str) == False:
                        response += Str

                    chunkposition = rnposition+2

    except socket.timeout as e:
        print('Get Data successfull')

    document = PATH.split("/")
    path = document[len(document) - 2]

    folder_path = './write_file/' + 'Chunk'
    if os.path.exists(folder_path) == False:
        os.mkdir(folder_path)

    if len(DATABASE) == 0 and len(PATH) == 1:
        with open('./' + folder_path + '/' + HOST + "_index.html", 'wb') as f:
            f.write(response)
    elif len(DATABASE) == 0 and len(PATH) != 1:
        with open('./' + folder_path + '/' + HOST + path, 'wb') as f:
            f.write(response)
    elif len(DATABASE) != 0:
        with open('./' + folder_path + '/' + HOST + '_' + DATABASE, 'wb') as f:
            f.write(response)

    print('\nDownload Data successful\n')
