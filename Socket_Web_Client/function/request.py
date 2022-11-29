# Nhận URL và tiến hành phân giải URL

import socket


def getrequest():

    request = ''
    request = input('Get URL here : ')

    return RequestParse(request)


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



def hex_to_int(x):
    return eval('0x'+x)
        
    
    
    
                                    
    
    
    
    