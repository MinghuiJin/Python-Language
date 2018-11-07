#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep  5 10:05:51 2018

@author: minghuijin
"""

from random import choice

def get_computer_choice():
    """ randomly choose and return one of 'rock', 'paper', 'scissors for computer' """
    computer = choice(['rock', 'paper', 'scissors'])
    print('I choose', computer)
    return computer

gamerules = {'p' : {'paper' : 'tie' , 'rock' : 'win' , 'scissors' : 'lose'}, 
             'r' : {'paper' : 'lose', 'rock' : 'tie' , 'scissors' : 'win'}, 
             's' : {'paper' : 'win' , 'rock' : 'lose', 'scissors' : 'tie'}}

count = 1

while True :
    print('Round', count, ':')    
    player = input("Please choose 'R', 'P', 'S' or 'Q' to quit:") 
    
    if player in ['r', 'p', 's', 'q']:
        if player == 'q' :
            print('Thanks for playing!')
            break
        else :            
            computer = get_computer_choice() # Call get_computer_choice() here to avoid redundant func call when player quits the game or input invalid choice
            
            result = gamerules[player][computer]
            if result == 'win' :
                print('Wow! You Win!\n')
            elif result == 'lose' :      
                print('Ouch! You Lose!\n')
            elif result == 'tie' :
                print('Tie! We both chose', computer, '\n')            
    else :
        print('Error! This is an invalid round!\n')
        
    count = count + 1
        
    