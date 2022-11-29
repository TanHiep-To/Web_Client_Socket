# Chức năng 7 : Concurrent , handle nhiều kết nối cùng một lúc đến các server.
import socket
import threading
from function.request import *
from function.getheader import *
from function.writeFileContent_Length import *
from function.writeFileChunked import *
from function.downsubfolder import *

def getrequest():

    request = ''
    request = input('Get URL here : ')
    
    return request

class RequestParse:

    def __init__(self, request):

        self.url = request

        request_temp = request.split("//", 1)

        if len(request_temp) == 1:
            requestarray = request_temp[0]
        else:
            requestarray = request_temp[1]

        n = len(requestarray.split('/'))

        self.host = ''
        self.path = ''
        self.content = ''

        path = ''
        self.host = requestarray.split('/')[0]

        for i in requestarray.split('/')[1:n]:
            x = i.find('.')
            if x == -1:
                path = path + '/' + i
            else:
                self.content += i
                break

        if path != '':
            self.path = path

        if path != '' and self.content != '':
            self.path += '/'

        if path == '':
            self.path = '/'


def handle_request(request):

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(10)
    
    HOST = request.host
    PORT = 80
    DATABASE = request.content
    PATH = request.path
    URL = request.url

    server_address = (HOST, PORT)
    try:
        s.connect(server_address)

        path = request.path + request.content

        request = "GET " + path + \
            " HTTP/1.1\r\nHost:" + HOST + "\r\n\r\n"

        s.sendall(request.encode())

        getheader = headerrespone(s)

        length = getheader[0]

        if length != -1:
            getContent_Length(s, length, HOST, PATH, DATABASE, URL)

        else:
            getChunked(s, HOST, PATH, DATABASE)

    except Exception as e:
        print(e)


threads = []
requests = []

while True: 
    Links = getrequest()
    if Links =='':
        break
    requests.append(Links)
    
for i in range(0,len(requests)):
    
    request = RequestParse(requests[i])
    thr = threading.Thread(target=handle_request,args=(request,))
    thr.start()
    threads.append(thr)



for t in threads:
    t.join()