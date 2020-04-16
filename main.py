#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb 20 21:22:45 2020

@author: arthurtan
"""

import game
from game import Player
from client import Client

if __name__ == "__main__":
    width = 1000
    height = 1000
    velocity = 105
    startx1 = 50
    starty1 = 50
    color1 = (0,0,128)
    startx2 = 950
    starty2 = 950
    color2 = (200,0,0)
    radius = 20
    ipAddress = '192.168.1.219'
    port = 12345
    clientNumber = int(input("Input your client number: "))
    client = Client(ipAddress, port, clientNumber)
    player1 = Player(startx1, starty1, velocity, color1, radius)
    player2 = Player(startx2, starty2, velocity, color2, radius)
    players = []
    players.append(player1)
    players.append(player2)
    numOfPlayer = 2
    g = game.Game(width, height, players, numOfPlayer, client)
    g()