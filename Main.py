##Nathan Hinton
import pygame

"""
crab:
move side to side
slow

gorilla:
move faster & jump

bunny:
hpos
if touching anther play player turns into bunny until loosing life or round is over

armidillo:
curl up into a bal and be invinsible, takes time to change

octopus:
clings to walls and grabs animal master which makes him unable to move for 5 seconds during which anyone tags while having etarnal lfe is upgraded.

snake:
slithers, has extra life bites animal master forcing him to lie down on the ground for 5 secinds.

eagle:
extra life, flys, grabs animal master for 5 seconds simillar to the octopus.

dragon:
flys, breathes fire, has armour, grabs animal master.

phenox:
flys, breathes fire, sets the animal master on fire when he touches him, if ever dies bets reborn after 5 seconds with 3 lives.
"""

levelOptions = ['crab', 'gorilla', 'bunny', 'armidillo', 'octopus', 'snake', 'eagle', 'dragon', 'phenox']

class Animal:
    def __init__(self):
        self.name = input("Player name:")
        self.level = 0
        self.lives = 2
        self.speed = 2

#Add player to the game:
add = True
animalsPlaying =[]
while add == True:
    if input("Add player (y/N): ") == 'y':
        animalsPlaying.append(Animal())
    else:
        add = False
if animalsPlaying == []:
    animalsPlaying.append(Animal())
    animalsPlaying.append(Animal())

class Game:
    def __init__(self, animalsPlaying):
        pass
