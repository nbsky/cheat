#!/usr/bin/env python

import socket

BUFFER_SIZE = 20

address = ('0.0.0.0', 8080)
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(address)
s.listen(5)

conn, addr = s.accept()
print 'connection address:', addr
while 1:
    data = conn.recv(BUFFER_SIZE)
    if not data: break
    print 'received data:', data
    conn.send(data)
conn.close()
# nc 127.0.0.1 8080
