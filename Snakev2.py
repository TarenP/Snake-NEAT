from pygame.locals import *
from random import randint
import pygame
import time
import os
 
class Apple:
    x = 0
    y = 0
    step = 44
 
    def __init__(self,x,y):
        self.x = x * self.step
        self.y = y * self.step
 
    def draw(self, surface, image):
        surface.blit(image,(self.x, self.y)) 
 
 
class Player:
    x = [0]
    y = [0]
    step = 44
    direction = 0
    length = 3
 
    updateCountMax = 2
    updateCount = 0
 
    def __init__(self, length):
       self.length = length
       for i in range(0,2000):
           self.x.append(-100)
           self.y.append(-100)
 
       # initial positions, no collision.
       self.x[1] = 1*44
       self.x[2] = 2*44
 
    def update(self):
 
        self.updateCount = self.updateCount + 1
        if self.updateCount > self.updateCountMax:
 
            # update previous positions
            for i in range(self.length-1,0,-1):
                self.x[i] = self.x[i-1]
                self.y[i] = self.y[i-1]
 
            # update position of head of snake
            if self.direction == 0:
                self.x[0] = self.x[0] + self.step
            if self.direction == 1:
                self.x[0] = self.x[0] - self.step
            if self.direction == 2:
                self.y[0] = self.y[0] - self.step
            if self.direction == 3:
                self.y[0] = self.y[0] + self.step
 
            self.updateCount = 0
 
 
    def moveRight(self):
        self.direction = 0
 
    def moveLeft(self):
        self.direction = 1
 
    def moveUp(self):
        self.direction = 2
 
    def moveDown(self):
        self.direction = 3 
 
    def draw(self, surface, image):
        for i in range(0,self.length):
            surface.blit(image,(self.x[i],self.y[i])) 
 
class Game:
    def isCollision(self,x1,y1,x2,y2,bsize):
        if x1 >= x2 and x1 <= x2 + bsize:
            if y1 >= y2 and y1 <= y2 + bsize:
                return True
        return False
 

windowWidth = 800
windowHeight = 600

game = Game()
player = Player(3) 
apple = Apple(5,5)

snakes = []
ge = []
nets = []

pygame.init()
_display_surf = pygame.display.set_mode((windowWidth,windowHeight), pygame.HWSURFACE)

pygame.display.set_caption('Pygame pythonspot.com example')
_running = True
_image_surf = pygame.image.load(os.path.join("Graphics", "gold2.png"))
_apple_surf = pygame.image.load(os.path.join("Graphics", "apple2.png"))

def on_event(event):
    if event.type == QUIT:
        self._running = False

def on_loop(player, apple):
    player.update()

    # does snake eat apple?
    for i in range(0,player.length):
        if apple.x == player.x[i] and apple.y == player.y[i]:
            apple.x = randint(2,9) * 44
            apple.y = randint(2,9) * 44
            player.length = player.length + 1


    # does snake collide with itself?
    for i in range(2, player.length):
        if game.isCollision(player.x[0],player.y[0],player.x[i], player.y[i],40):
            print("You lose! Collision: ")
            print("x[0] (" + str(player.x[0]) + "," + str(player.y[0]) + ")")
            print("x[" + str(i) + "] (" + str(player.x[i]) + "," + str(player.y[i]) + ")")
            exit(0)

    pass

def on_render(player):
    _display_surf.fill((0,0,0))
    player.draw(_display_surf, _image_surf)
    apple.draw(_display_surf, _apple_surf)
    pygame.display.flip()

def on_cleanup():
    pygame.quit()

def on_execute():
    global _running
    while(_running ):
        pygame.event.pump()
        keys = pygame.key.get_pressed() 

        if (keys[K_RIGHT]):
            player.moveRight()

        if (keys[K_LEFT]):
            player.moveLeft()

        if (keys[K_UP]):
            player.moveUp()

        if (keys[K_DOWN]):
            player.moveDown()

        if (keys[K_ESCAPE]):
            _running = False

        on_loop(player, apple)
        on_render()

        time.sleep (50.0 / 1000.0)
    on_cleanup()

if __name__ == "__main__" :
    on_execute()