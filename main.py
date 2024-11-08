#Main file for the asteroids game
#Free stuff from the open-source game code library pygame is imported to allow for game coding
#Overall, python isn't ideal for gamedev since it dosen't compile, but some useful stuff can still be made
#Use python3 main.py rather than ./main.py to start the program, close with ctrl-Cs

import pygame
import sys
from constants import *
from player import Player
from shot import Shot
from asteroid import Asteroid
from asteroidfield import AsteroidField

def main():
        pygame.init()
        screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT)) #Defines the window of the game, aka the graphical user interface (GUI)
        fps = pygame.time.Clock()
        dt = 0
        asteroids_destroyed = 0
        time_alive = 0
        updatable = pygame.sprite.Group()
        drawable = pygame.sprite.Group()
        asteroids = pygame.sprite.Group()
        shots = pygame.sprite.Group()

        Player.containers = (updatable, drawable)     #Ensures that all instances of class Player created goes in this container, making it a member of these two groups
        Asteroid.containers = (updatable, drawable, asteroids)    #Each subsequent container ensures this object class goes into the correct group when created
        AsteroidField.containers = (updatable)        #This is the function that spawns asteroids on the edges of the screen - it does not exist as an ingame object inof itself
        Shot.containers = (updatable, drawable, shots)      #This container contains the shots generated by the player

        print("Starting asteroids!",
              f"Screen width: {SCREEN_WIDTH}",
              f"Screen height: {SCREEN_HEIGHT}")

        player_sprite = Player(x=SCREEN_WIDTH/2, y=SCREEN_HEIGHT/2)     #Initalizes the player sprite in the center of the screen
        Asteroidfield1 = AsteroidField()

        while True:    #Infinite while loop - terminate with ctrl - C in terminal
              for event in pygame.event.get():  #pygame specific function, this loop terminates the code when the game window is closed
                  if event.type == pygame.QUIT:
                        print(f"Game closed! You destroyed {asteroids_destroyed} asteroids and lived for {int(time_alive / 60)} seconds!")
                        return
              for object in updatable:    #Iterate over all the objects in the updatable list and call update on all - housekeeping functions mostly
                    object.update(dt)     #This does track player input
              for object in asteroids:    #Iterates over all the asteroids
                  for shot in shots:      #Iterate over all the shots and see if any are colliding with asteroids
                       if object.collide(shot):
                            asteroids_destroyed += 1  #Simple tracker to see how many asteroids the player destroyed
                            object.split()      #If any shots hit asteroids, split them (unless they are too small) and destroy the original
                            shot.kill()         #Remove the shot
                  if object.collide(player_sprite):   #If the player hits an asteroid, it's game over
                       print(f"Game over! You destroyed {asteroids_destroyed} asteroids, and lived for {int(time_alive / 60)} seconds!")
                       sys.exit(0)        #Terminates code and closes the game window
              screen.fill('black')        #All the other objects are white, so filling with black makes them visible
              for object in drawable:     #Iterate over all the objects in drawable list and draw all
                  object.draw(screen)     #In practice, this updates the display so the player can see and interact with the game
              pygame.display.flip()       #Unsure of the details but it's related to refreshing the screen so the player can see it update
              dt = (fps.tick(60)/1000)    #This makes the clock tic - set at 60 fps, which also means the game updates 60 times per second, meaning there are 60 tics per second
              time_alive += 1             #Tics up once each tic, 60 tics means one second (unless the program runs too slowly to fit 60 tics in a second, which is very unlikely for this)



if __name__ == "__main__":
    main()