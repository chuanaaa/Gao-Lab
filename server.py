#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb  2 21:21:59 2020

@author: arthurtan
"""

import socket
import pickle
import sys
from threading import Thread
from requests import get

try:
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    port = 12345
    server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server.bind(('', port))
    server.listen(5)

    ip = get('https://api.ipify.org').text  
    print(f"My public IP address is: {ip}")
    print("Server is listening")
    position = ["", ""]
    def threadedClient(client):
        global position
        reply = ''
        while True:
            try: 
                data = client.recv(2048)
                if not data:
                    client.send(str.encode("Goodbye"))
                    break
                else:
                    reply = data.decode("utf-8")
                    print("Recieved: " + reply)
                    array = reply.split(":")
                    clientId = int(array[0])
                    position[clientId] = reply
                    client.send(pickle.dumps(position))
            except:
                break            

    while True:
        client, address = server.accept()
        print(address)
        print(f"Socket Up and running with a connection from {address}")
        Thread(target = threadedClient, args = (client,)).start()
        print("Awaiting new connection")

except KeyboardInterrupt:
    print("Closing Connection and freeing the port.")
    client.close()
    sys.exit()


