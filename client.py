#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb  2 21:35:10 2020

@author: arthurtan
"""

import socket
import pickle



class Client:
    def __init__(self, ipAddress, port, clientNumber):
        self.server = socket.socket()
        self.ipAddress = ipAddress
        self.port = port
        self.clientNumber = clientNumber
        try:
            self.server.connect((self.ipAddress, self.port))
            print("Connected to server")
        except Exception as e: 
            print("something's wrong with %s:%d. Exception is %s" % (self.ipAddress, self.port, e))

        
    def send(self, coordinates):
        myPosition = str(self.clientNumber) + ":" + coordinates
        self.server.send(myPosition.encode("utf-8"))
    
    def receive(self):
        data = self.server.recv(2048)
        allPositions = pickle.loads(data)
        return allPositions

