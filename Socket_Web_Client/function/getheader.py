# Phân giải URL nhập vào ra các thành phần tương ứng .

import socket
import sys


def headerrespone(socketrespone):

    header = b''

    try:
        while True:
            header = header + socketrespone.recv(1)
            x = header.find(b"\r\n\r\n")
            if x != -1:
                break
    except socket.timeout:
        print("Crawling header successfull.\n")

    x = header.rfind(b"\r\nContent-Length: ")

    if x == -1:
        return (-1, header)

    headerlength = header[x+len("\r\nContent-Length: "):len(header)]

    y = headerlength.find(b"\r\n")

    length = '-1'
    length = headerlength[0:y]

    return (int(length), header)