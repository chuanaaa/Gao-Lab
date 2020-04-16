#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 19 16:51:16 2020

@author: arthurtan
"""

import pygame



class Player():
    
    def __init__(self, startx, starty, velocity, color, radius):
        self.x = startx
        self.y = starty
        self.velocity = velocity
        self.color = color
        self.radius = radius




class Game():
    
    def __init__(self, width, height, players, numOfPlayers, client):
        self.client = client
        self.width = width
        self.height = height
        self.numOfPlayers = numOfPlayers
        self.players = players
            
    def __call__(self):
        pygame.init()
        window = pygame.display.set_mode((self.width,self.height))
        pygame.display.set_caption("Game")
        run = True
        while run:
            pygame.time.wait(10)
            window.fill((0,0,0))
            self.draw(window)
            self.detectKey()
            self.detectBoundaries()
            self.sendCoordinates()
            reply = self.receiveCoordinates()
            newCoordinates = self.processCoordinates(reply)
            player = 0
            for player in range(self.numOfPlayers):
                self.players[player].x, self.players[player].y = newCoordinates[player]
        pygame.quit()
        
    def detectKey(self):
        events = list(pygame.event.get())
        for event in events:
            if event.type == pygame.QUIT:
                pygame.quit()
        for key in events:
                if key.type == pygame.MOUSEMOTION:
                    mousePosition = pygame.mouse.get_pos()
                    self.players[self.client.clientNumber].x = mousePosition[0]
                    self.players[self.client.clientNumber].y = mousePosition[1]
    
    def detectBoundaries(self):
        if self.players[self.client.clientNumber].x >= (self.width-self.players[self.client.clientNumber].radius):
            self.players[self.client.clientNumber].x = self.width-self.players[self.client.clientNumber].radius
        if self.players[self.client.clientNumber].x <= self.players[self.client.clientNumber].radius:
            self.players[self.client.clientNumber].x = self.players[self.client.clientNumber].radius
        if self.players[self.client.clientNumber].y >= (self.height-self.players[self.client.clientNumber].radius):
            self.players[self.client.clientNumber].y = self.height-self.players[self.client.clientNumber].radius
        if self.players[self.client.clientNumber].y <= self.players[self.client.clientNumber].radius:
            self.players[self.client.clientNumber].y = self.players[self.client.clientNumber].radius
                
                        
                        
    def draw(self, window):
        player = 0
        for player in range(self.numOfPlayers):
            pygame.draw.circle(window, self.players[player].color, (self.players[player].x, self.players[player].y), self.players[player].radius)         
            pygame.display.flip()
    
    
    def sendCoordinates(self):
        coordinates = str(self.players[self.client.clientNumber].x) + "," + str(self.players[self.client.clientNumber].y)
        self.client.send(coordinates)
        
    def receiveCoordinates(self):
        reply = self.client.receive()
        print(reply)
        return reply
    
    def processCoordinates(self, reply):
        newCoordinates = []
        player = 0
        for player in range(self.numOfPlayers):
            playerCoordinates = []
            if reply[player] == '':
                playerCoordinates.append(self.players[player].x)
                playerCoordinates.append(self.players[player].y)
                newCoordinates.append(playerCoordinates)
                print(newCoordinates)
                continue;
            playerCoordinates = reply[player].split(":")[1].split(",")
            playerCoordinates[0] = int(playerCoordinates[0])
            playerCoordinates[1] = int(playerCoordinates[1])
            newCoordinates.append(playerCoordinates)
        return newCoordinates
    

    
    
    
    
    
    






     

