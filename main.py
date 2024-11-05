#Main file for the asteroids game
#Free stuff from the open-source game code library pygame is imported to allow for game coding
#Overall, python isn't ideal for gamedev since it dosen't compile, but some useful stuff can still be made
#Use python3 main.py rather than ./main.py to start the program, close with ctrl-Cs

import pygame
import sys
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField

def main():
        pygame.init()
        screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT)) #Defines the window of the game, aka the graphical user interface (GUI)
        fps = pygame.time.Clock()
        dt = 0
        updatable = pygame.sprite.Group()
        drawable = pygame.sprite.Group()
        asteroids = pygame.sprite.Group()

        Player.containers = (updatable, drawable)     #Ensures that all instances of class Player created goes in this container, making it a member of these two groups
        Asteroid.containers = (updatable, drawable, asteroids)
        AsteroidField.containers = (updatable)

        print("Starting asteroids!",
              f"Screen width: {SCREEN_WIDTH}",
              f"Screen height: {SCREEN_HEIGHT}")

        player_sprite = Player(x=SCREEN_WIDTH/2, y=SCREEN_HEIGHT/2)     #Initalizes the player sprite in the center of the screen
        Asteroidfield1 = AsteroidField()

        while True:    #Infinite while loop - terminate with ctrl - C in terminal
              for event in pygame.event.get():
                  if event.type == pygame.QUIT:
                        return
              for object in updatable:    #Iterate over all the objects in the updatable list and call update on all 
                    object.update(dt)
              for object in asteroids:
                  if object.collide(player_sprite):
                       print("Game over!")
                       sys.exit(0)
              screen.fill('black')
              for object in drawable:     #Iterate over all the objects in drawable list and draw all
                  object.draw(screen)                    
              pygame.display.flip()
              dt = (fps.tick(60)/1000)



if __name__ == "__main__":
    main()