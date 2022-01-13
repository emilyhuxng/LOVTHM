#########################################
# File Name: finalAssignment.py
# Description: Our game LOVTHM is a rhythm game where you tap circles when it reaches a certain point
# Author: Sylvia and Emily
# Date: 19/12/2018
#########################################

from math import pi
import random
import pygame                           
pygame.init()
WIDTH = 800
HEIGHT= 600
gameWindow=pygame.display.set_mode((WIDTH,HEIGHT))

#colours
RED  =(255,  0,  0)
GREEN=(  0,255,  0)
BLUE =(  0,  0,255)
CYAN =(  0,255,255)
WHITE=(255,255,255)
BLACK=(  0,  0,  0)
GREY =(128,128,128)
SKYBLUE = (196, 233, 255)
LIGHTGREEN = (60, 183, 105)
SKIN = (249, 222, 187)
JEANBLUE = (32, 79, 130)
ORANGE = (255, 130, 28)
MAHOGANYLIGHT = (99, 20, 12)
MAHOGANYMEDIUM = (79, 15, 9)
MAHOGANYDARKISH = (53, 10, 6)
MAHOGANYDARK = (25, 4, 2)
DARKGRAY = (25, 23, 23)
LIGHTBLACK = (22, 22, 22)
MEDIUMGRAY = (66, 66, 66)
LIGHTYELLOW = (252, 200, 95)
DARKYELLOW = (193, 150, 62)

#variables
#check if the game should be running
inPlay = True
playing = False
#check if the music should be on
on = True
#the x position of the mouse
mouseX = 0
#the y position of the mouse
mouseY = 0
#the screen to display
currentScreen = 0
#the x position of the border around the songs
borderX = -1000
#the y position of the border around the songs
borderY = -1000
#the y reference of the notes
yRef = 100
#the 4 possible x positions of the notes
tilesPos = [250,350,450,550]
#the x positions of the notes of a song
tilesX = []
#the y positions of the notes of a song
tilesY = []
#the y values for each note
yValues = 240
#the maps of each songs
songMaps = [[ 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 0, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 0, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 0, 0, 0, 0, 1, 0, 1, 0, 1, 0, 1, 0, 0, 0, 1, 0, 1, 0, 1, 0, 0, 0, 1, 0, 1, 0, 1, 0, 1, 0, 0, 0, 0, 0, 1, 0, 1, 0, 1, 0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 1, 0, 1, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 1, 0, 1, 0, 0, 0, 1, 0, 1, 0, 1, 0, 0, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 1, 0, 1, 0, 1, 1, 1, 1, 0, 0, 1, 0, 1, 1, 1, 1, 1, 0, 1, 1, 0, 0, 1, 0, 0, 0, 1, 0, 1, 1, 1, 0, 1, 0, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 1, 0, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 0, 1, 1, 0, 0, 0, 1, 0, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 0, 1, 1, 0, 0, 0, 0, 0, 1, 0],[0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 1, 1, 0, 1, 0, 1, 1, 1, 1, 1, 0, 1, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 0, 0, 1, 1, 0, 1, 1, 1, 1, 0, 1, 0, 1, 0, 0, 0, 0, 0, 1, 1, 0, 0, 1, 0, 1, 1, 1, 0, 1, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 0, 1, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 0, 0, 1, 0, 0, 1, 0, 1, 1, 0, 1, 0, 1, 0, 1, 1, 0, 1, 1, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 0, 1, 0, 0, 0, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 0, 0, 1, 1, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 0, 0, 0, 1, 1, 1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 1, 0, 1, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 1, 0, 0, 1, 1, 1, 1, 0, 1, 1, 1, 1, 0, 1, 0, 0, 1, 0, 0, 1, 1, 1, 1, 0, 1, 1, 1, 1, 0, 1, 0, 0, 0, 0, 0, 1, 1, 1, 1, 0, 1, 1, 0, 1, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 1, 0, 1, 1, 0, 0, 1, 0, 1, 0, 0, 0, 1, 0, 1, 0, 1, 0, 1, 1, 0, 0, 1, 0, 1, 0, 0, 0, 1, 0, 1, 0, 1, 0, 1, 1, 0, 0, 1, 0, 1, 0, 1, 1, 0, 0, 1, 0, 1, 0, 0, 1, 0, 0, 1, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 1, 0, 0, 0, 1, 0, 1, 0, 1, 0, 0, 0, 1, 0, 1, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 1, 1, 0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 1, 0, 1, 0, 1, 1, 0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 1, 0, 1, 0, 1, 1, 0, 1, 1, 0, 1, 0, 1, 1, 0, 1, 1, 0, 1, 0, 1, 1, 0, 1, 1, 0, 1, 0, 0, 0, 1, 0, 1, 0, 1, 0, 0, 0, 1, 0, 1, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 0, 1, 0, 0, 1, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 1, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 1, 0, 1, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 1, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 1, 0, 1, 0, 1, 0, 0, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 0, 1, 0, 1, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1],[0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 1, 0, 1, 0, 0, 0, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 0, 1, 0, 0, 0, 1, 1, 0, 0, 1, 0, 0, 0, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 1, 0, 1, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 0, 1, 0, 0, 0, 0, 1, 1, 1, 1, 1, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 0, 1, 1, 1, 1, 1, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 1, 1, 1, 1, 1, 1, 1]]
#the current chosen song
song = ""
#the index of the song
songNumber = 0
#count set for the loading screen to give player time to get ready
count = 0
#the speed of each song
speeds = [0.63,0.453,0.79,0.3575]
#the speed of the chosen song
speed = 0
#how well you hit the note
scoreColour = (255,255,255)
#the number of times you got good, bad, etc.
notesHit = [0,0,0,0]
#the notes that actually got hit by the user
notesScored = []
#score accumulator
score = 0
#clock to calculate the tick
fpsClock = pygame.time.Clock()

#---------------------------------------#
# music properties                      #
#---------------------------------------#

music=["loveScenario.mp3","Popstars.mp3","Thanks.mp3","The Eve.mp3"]

#---------------------------------------#
# picture properties                    #
#---------------------------------------#
#background
background = pygame.image.load("ICS Homepage.png")

#instructions button
instructionsButton = pygame.image.load("InstructionsButton.png")

#instructions page
instructionsPage = pygame.image.load("instructions page.png")

#options page
optionsPage = pygame.image.load("options page.png")

#song selection page
songPage = pygame.image.load("SongSelection.png")

#loading page
loadingPage = pygame.image.load("loadingScreen.png")

#end page
endPage = pygame.image.load("endScreen.png")

#pause page
pausePage = pygame.image.load("pausePage.png")

#play button
playButton = pygame.image.load("PlayButton.png")

#settings button
settingsButton = pygame.image.load("SettingsButton.png")

#quit button
quitButton = pygame.image.load("Quit.png")

#title
title = pygame.image.load("Title.png")

#love scenario background
loveScenarioBackground = pygame.image.load("iKON.png")

#popstars background
popstarsBackground = pygame.image.load("KDA.png")

#thanks background
thanksBackground = pygame.image.load("SVT.png")

#the eve background
theEveBackground = pygame.image.load("Exo.png")

#exo gray bar
exoBar = pygame.image.load("EXO BAR.png")

#kda gray bar
kdaBar = pygame.image.load("KDA BAR.png")

#thanks gray bar
thanksBar = pygame.image.load("THANKS BAR.png")

#iKon gray bar
iKonBar = pygame.image.load("IKON BAR.png")

#font
font = pygame.font.SysFont("Century Gothic",20)




#---------------------------------------#
# the main program begins here          #
#---------------------------------------#

#functions
def drawHomepage():
    #background
    gameWindow.blit(background,(0,0))

    #title
    gameWindow.blit(title, (100,100))

    #Quit button
    gameWindow.blit(quitButton, (750,10))

    #Instructions button
    gameWindow.blit(instructionsButton, (100,545))

    #Play button
    gameWindow.blit(playButton, (325,545))   

    #Settings
    gameWindow.blit(settingsButton, (550,545))

def drawInstructions():
    gameWindow.blit(instructionsPage, (0,0))

def drawSongs():
    gameWindow.blit(songPage, (0,0))
    pygame.draw.rect(gameWindow,WHITE,(borderX,borderY,200,200),2)

def drawSettings():
    gameWindow.blit(optionsPage,(0,0))

def drawPause():
    gameWindow.blit(pausePage, (0,0))

def drawEndPage():
    gameWindow.blit(endPage, (0,0))
    
def playSong(yRef,notesOn,tilesY,songNumber,currentScreen,scoreColour,notesHit,notesScored,score ):
    if yRef == 100:
        pygame.mixer.music.play(-1)
    yRef = int(round(yRef))

    #print out the notes     
    for i in range(0,len(notesOn),1):
        if notesOn[i]==1 and tilesY[i]+yRef>-100 and tilesY[i]+yRef<700:
            pygame.draw.circle(gameWindow,BLACK,(tilesX[i],yRef+tilesY[i]),30,0)
    #blit the bars to cover up the notes at the bottom
        if songNumber == 0:
            gameWindow.blit(iKonBar, (219, 531))
        elif songNumber == 1:
            gameWindow.blit(kdaBar, (219, 531))
        elif songNumber == 2:
            gameWindow.blit(thanksBar, (219, 531))
        elif songNumber == 3:
            gameWindow.blit(exoBar, (219,531))

    #draw the red borders
    for i in range(250,551,100):
        pygame.draw.circle(gameWindow,RED,(i,500),31,3)

    
    #check when a key is pressed down and if it the y position of a circle is within a boundary, print a circle to rep good, bad, etc.
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_d:
                for index in range(len(notesOn)):                
                    if tilesX[index] == 250 and tilesY[index]+yRef >= 490 and tilesY[index]+yRef <= 510 and notesOn[index]==1:
                        scoreColour = (133,255,142)
                        notesScored[index]=1
                        notesHit[0]+=1
                        score+=300
                    elif tilesX[index] == 250 and tilesY[index]+yRef >= 470 and tilesY[index]+yRef <= 530 and notesOn[index]==1:
                        scoreColour = (127,199,253)
                        notesScored[index]=1
                        notesHit[1]+=1
                        score+=200
                    elif tilesX[index] == 250 and tilesY[index]+yRef >= 450 and tilesY[index]+yRef <= 550 and notesOn[index]==1:
                        scoreColour = (169,140,214)
                        notesScored[index]=1
                        notesHit[2]+=1
                        score+=100
            if event.key == pygame.K_f:
                for index in range(len(notesOn)):                
                    if tilesX[index] == 350 and tilesY[index]+yRef >= 490 and tilesY[index]+yRef <= 510 and notesOn[index]==1:
                        scoreColour = (133,255,142)
                        notesScored[index]=1
                        notesHit[0]+=1
                        score+=300
                    elif tilesX[index] == 350 and tilesY[index]+yRef >= 470 and tilesY[index]+yRef <= 530 and notesOn[index]==1:
                        scoreColour = (127,199,253)
                        notesScored[index]=1
                        notesHit[1]+=1
                        score+=200
                    elif tilesX[index] == 350 and tilesY[index]+yRef >= 450 and tilesY[index]+yRef <= 550 and notesOn[index]==1:
                        scoreColour = (169,140,214)
                        notesScored[index]=1
                        notesHit[2]+=1
                        score+=100
            if event.key == pygame.K_j:
                for index in range(len(notesOn)):                
                    if tilesX[index] == 450 and tilesY[index]+yRef >= 490 and tilesY[index]+yRef <= 510 and notesOn[index]==1:
                        scoreColour = (133,255,142)
                        notesScored[index]=1
                        notesHit[0]+=1
                        score+=300
                    elif tilesX[index] == 450 and tilesY[index]+yRef >= 470 and tilesY[index]+yRef <= 530 and notesOn[index]==1:
                        scoreColour = (127,199,253)
                        notesScored[index]=1
                        notesHit[1]+=1
                        score+=200
                    elif tilesX[index] == 250 and tilesY[index]+yRef >= 450 and tilesY[index]+yRef <= 550 and notesOn[index]==1:
                        scoreColour = (169,140,214)
                        notesScored[index]=1
                        notesHit[2]+=1
                        score+=100
            if event.key == pygame.K_k:
                for index in range(len(notesOn)):                
                    if tilesX[index] == 550 and tilesY[index]+yRef >= 490 and tilesY[index]+yRef <= 510 and notesOn[index]==1:
                        scoreColour = (133,255,142)
                        notesScored[index]=1
                        notesHit[0]+=1
                        score+=300
                    elif tilesX[index] == 550 and tilesY[index]+yRef >= 470 and tilesY[index]+yRef <= 530 and notesOn[index]==1:
                        scoreColour = (127,199,253)
                        notesScored[index]=1
                        notesHit[1]+=1
                        score+=200
                    elif tilesX[index] == 250 and tilesY[index]+yRef >= 450 and tilesY[index]+yRef <= 550 and notesOn[index]==1:
                        scoreColour = (169,140,214)
                        notesScored[index]=1
                        notesHit[2]+=1
                        score+=100
            #if p is pressed, pause
            if event.key == pygame.K_p:
                currentScreen = 5
                pygame.mixer.music.pause()
    
    pygame.event.get()
    keys = pygame.key.get_pressed()

    #when a key is held down, make the circle turn white, otherwise keep grey
    if keys[pygame.K_d]:            
        pygame.draw.circle(gameWindow,WHITE,(250,500),28,0)  
    else:
        pygame.draw.circle(gameWindow,GREY,(250,500),28,0)
    if keys[pygame.K_f]:
        pygame.draw.circle(gameWindow,WHITE,(350,500),28,0)
    else:
        pygame.draw.circle(gameWindow,GREY,(350,500),28,0)
    if keys[pygame.K_j]:
        pygame.draw.circle(gameWindow,WHITE,(450,500),28,0)
    else:
        pygame.draw.circle(gameWindow,GREY,(450,500),28,0)
    if keys[pygame.K_k]:
        pygame.draw.circle(gameWindow,WHITE,(550,500),28,0)
    else:
        pygame.draw.circle(gameWindow,GREY,(550,500),28,0)

    #if the last note goes past a certain point, go to end screen and stop music
    if yRef+tilesY[len(notesOn)-1]>=1500:
        currentScreen = 6
        pygame.mixer.music.stop()
        #calculate the number of notes missed
        for i in range(len(notesOn)):
            if notesOn[i]==1 and notesScored[i]==0:
                notesHit[3]+=1
        print (score)
    #print the colour of the grade you got each note
    if scoreColour != (255,255,255):
        pygame.draw.circle(gameWindow,scoreColour,(700,200),40,0)
    return (currentScreen,scoreColour,notesHit,notesScored,score)

#main game
while inPlay:
    gameWindow.fill(WHITE)
    #homepage
    if currentScreen == 0:
        drawHomepage()
        #if mouse clicks instructions button, go to instructions page
        if mouseX >= 100 and mouseX <= 250 and mouseY >= 550 and mouseY <=600:
            if event.type == pygame.MOUSEBUTTONDOWN:
                currentScreen = 1
        #if mouse clicks play button, go to song selection screen
        if mouseX >= 325 and mouseX <= 475 and mouseY >= 550 and mouseY <=600:
            if event.type == pygame.MOUSEBUTTONDOWN:
                currentScreen = 2
        #if mouse clicks settings button, go to options page
        if mouseX >= 550 and mouseX <= 700 and mouseY >= 550 and mouseY <=600:
            if event.type == pygame.MOUSEBUTTONDOWN:
                currentScreen = 3
        #if mouse clicks exit button, close progam
        if mouseX >= 750 and mouseX <= 790 and mouseY >= 10 and mouseY <=50:
            if event.type == pygame.MOUSEBUTTONDOWN:
                inPlay = False
        #instructions page
    elif currentScreen == 1:
        drawInstructions()
        borderX = -1000
        borderY = -1000
        #home page
        if mouseX >= 25 and mouseX <= 75 and mouseY >= 35 and mouseY <= 85:
            if event.type == pygame.MOUSEBUTTONDOWN:
                currentScreen = 0
        #song selection page
        if mouseX >= 298 and mouseX <= 501 and mouseY >= 484 and mouseY <= 547:
            if event.type == pygame.MOUSEBUTTONUP:
                currentScreen = 2
                
    elif currentScreen == 2:
        drawSongs()
        #back button
        if mouseX >= 25 and mouseX <= 65 and mouseY >= 30 and mouseY <= 70:
            if event.type == pygame.MOUSEBUTTONDOWN:
                currentScreen = 0
                borderX = -1000
                borderY = -1000
                pygame.mixer.music.stop()
                song = ""
        #play button which continues on to the game
        if mouseX >= 300 and mouseX <= 500 and mouseY >= 525 and mouseY <= 585:
            if event.type == pygame.MOUSEBUTTONDOWN:
                if song != "":
                    currentScreen = 4
                    pygame.mixer.music.stop()
        #love Scenario
        if mouseX >= 148 and mouseX <= 348 and mouseY >= 72 and mouseY <= 272:
            if event.type == pygame.MOUSEBUTTONDOWN:
                borderX = 148
                borderY = 72
                song = music[0]
                songNumber = 0
                screenColour = (255,255,255)
                pygame.mixer.music.load(song)
                pygame.mixer.music.play(-1)
        #Popstars
        if mouseX >= 463 and mouseX <= 663 and mouseY >= 72 and mouseY <= 272:
            if event.type == pygame.MOUSEBUTTONDOWN:
                borderX = 463
                borderY = 72
                song = music[1]
                songNumber = 1
                screenColour = (255,255,255)
                pygame.mixer.music.load(song)
                pygame.mixer.music.play(-1)
        #Thanks
        if mouseX >= 148 and mouseX <= 348 and mouseY >= 313 and mouseY <= 513:
            if event.type == pygame.MOUSEBUTTONDOWN:
                borderX = 148
                borderY = 313
                song = music[2]
                songNumber = 2
                screenColour = (255,255,255)
                pygame.mixer.music.load(song)
                pygame.mixer.music.play(-1)
        #The Eve
        if mouseX >= 463 and mouseX <= 663 and mouseY >= 313 and mouseY <= 513:
            if event.type == pygame.MOUSEBUTTONDOWN:
                borderX = 463
                borderY = 313
                song = music[3]
                songNumber = 3
                screenColour = (255,255,255)
                pygame.mixer.music.load(song)
                pygame.mixer.music.play(-1)
        #options page
    elif currentScreen == 3:
        drawSettings()
        #if mouse clicks back button, go back to homepage
        if mouseX >= 25 and mouseX <= 65 and mouseY >= 30 and mouseY <= 70:
            if event.type == pygame.MOUSEBUTTONDOWN:
                currentScreen = 0
        #music is on
        if mouseX >= 180 and mouseX <=400 and mouseY >=445 and mouseY <=535:
            if event.type == pygame.MOUSEBUTTONDOWN:
                on = True
                pygame.mixer.music.set_volume(5)
        #music is off
        elif mouseX >=400 and mouseX <=620 and mouseY >=445 and mouseY <=535:
            if event.type == pygame.MOUSEBUTTONDOWN:
                on = False
                pygame.mixer.music.set_volume(0)
                
        if on == True:
            pygame.draw.rect(gameWindow, WHITE, (180, 445, 220, 90), 3)
        else:
            pygame.draw.rect(gameWindow, WHITE, (400, 445, 220, 90), 3)

        #song is starting
    elif currentScreen == 4:
        #assign which song and map to play
        if song == music[0]:
            notesOn = songMaps[0]
            speed = speeds[0]
        elif song == music[1]:
            notesOn = songMaps[1]
            speed = speeds[1]
        elif song == music[2]:
            notesOn = songMaps[2]
            speed = speeds[2]
        elif song == music[3]:
            notesOn = songMaps[3]
            speed = speeds[3]
        notesOn = songMaps[songNumber]
        speed = speeds[songNumber]

        #declare the y values of the notes
        for i in range(0,len(notesOn),1):    
            tilesY.append(yValues)
            yValues-=80
        #append the x values and the notes scored
        for i in range(0,len(notesOn),1):
            tilesX.append(tilesPos[random.randint(0,3)])
            notesScored.append(0)
        #after count reaches 500, the map starts
        if count >= 500:
            if songNumber == 0:
                gameWindow.blit(loveScenarioBackground, (0,0))
            elif songNumber == 1:
                gameWindow.blit(popstarsBackground, (0,0))
            elif songNumber == 2:
                gameWindow.blit(thanksBackground, (0,0))
            elif songNumber == 3:
                gameWindow.blit(theEveBackground, (0,0))
            playing = True

        #loading screen for user to get ready    
        else:
            gameWindow.blit(loadingPage, (0,0))
        count+=1

        #actual song starts playing
        if playing == True:
            currentScreen,scoreColour,notesHit,notesScored,score = playSong(yRef,notesOn,tilesY,songNumber,currentScreen,scoreColour,notesHit,notesScored,score)
            #homepage (reset values)
            if currentScreen == 0:
                yRef = 100
                song = ""
                speed = 0
                count = 0
                songNumber = 0
                pygame.mixer.music.stop()
            yRef+=tick*speed
    #pause page        
    elif currentScreen == 5:
        drawPause()
        #homepage (reset values)
        if mouseX >= 355 and mouseX <= 449 and mouseY >= 120 and mouseY <=215:
            if event.type == pygame.MOUSEBUTTONDOWN:
                currentScreen = 0
                yRef = 100
                song = ""
                speed = 0
                count = 0
                songNumber = 0
                pygame.mixer.music.stop()
                notesHit = [0, 0, 0, 0,]
                notesScore = []
                borderX = -1000
                borderY = -1000
                playing = False
                screenColour = (255,255,255)
                score = 0
        #continue
        if mouseX >= 355 and mouseX <= 449 and mouseY >= 235 and mouseY <=330:
            if event.type == pygame.MOUSEBUTTONDOWN:
                currentScreen = 4
                pygame.mixer.music.unpause()
        #song selection (reset values)
        if mouseX >= 355 and mouseX <= 449 and mouseY >= 350 and mouseY <=445:
            if event.type == pygame.MOUSEBUTTONDOWN:
                currentScreen = 2
                yRef = 100
                song = ""
                speed = 0
                count = 0
                songNumber = 0
                pygame.mixer.music.stop()
                notesHit = [0, 0, 0, 0,]
                notesScore = []
                borderX = -1000
                borderY = -1000
                playing = False
                screenColour = (255,255,255)
                score = 0
    #end screen
    elif currentScreen == 6:
        drawEndPage()
        #blit the scores
        perfect = font.render(" " + str(notesHit[0]) ,5,WHITE)
        gameWindow.blit(perfect,(580,220))
        great = font.render(" " + str(notesHit[1]), 5,WHITE)
        gameWindow.blit(great,(580,295))
        ok = font.render(" " + str(notesHit[2]),5,WHITE)
        gameWindow.blit(ok,(580,370))
        missed = font.render(" " + str(notesHit[3]),5,WHITE)
        gameWindow.blit(missed,(580,445))
        
        
        #home page (reset values)
        if mouseX >= 24 and mouseX <=241 and mouseY >=528 and mouseY <=593:
            if event.type == pygame.MOUSEBUTTONUP:
                currentScreen = 0
                yRef = 100
                song = ""
                speed = 0
                count = 0
                songNumber = 0
                pygame.mixer.music.stop()
                notesHit = [0, 0, 0, 0,]
                notesScore = []
                playing = False
                screenColour = (255,255,255)
                borderX = -1000
                borderY = -1000
                score = 0

        #song selection (reset values)
        if mouseX >= 292 and mouseX <=509 and mouseY >=528 and mouseY <=593:
            if event.type == pygame.MOUSEBUTTONDOWN:
                currentScreen = 2
                yRef = 100
                song = ""
                speed = 0
                count = 0
                songNumber = 0
                pygame.mixer.music.stop()
                notesHit = [0, 0, 0, 0,]
                notesScore = []
                borderX = -1000
                borderY = -1000
                playing = False
                screenColour = (255,255,255)
                score = 0

        #play again (reset certain values)
        if mouseX >= 562 and mouseX <=779 and mouseY >=528 and mouseY <=593:
            if event.type == pygame.MOUSEBUTTONDOWN:
                currentScreen = 4
                notesHit = [0, 0, 0, 0,]
                notesScore = []
                yRef = 100
                count = 0
                playing = False
                screenColour = (255,255,255)
                borderX = -1000
                borderY = -1000
                score = 0
    #get position of mouse    
    for event in pygame.event.get():
        (mouseX,mouseY) = pygame.mouse.get_pos()
        
    #check if the escape button is pressed
    pygame.event.get()
    keys = pygame.key.get_pressed()
    if keys[pygame.K_ESCAPE]:
        inPlay = False
        #---------------------------------------#
    pygame.display.flip()                 # display must be updated, in order
    tick = fpsClock.tick_busy_loop(60)             # to show the drawings

#if it is here, that means it is out of the while loop so it should exit
pygame.quit()
