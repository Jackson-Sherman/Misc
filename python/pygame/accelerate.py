import pygame
import random as rn
pygame.init()
screen = pygame.display.set_mode((400,400))

ongoing = True

class acc:
    def __init__(self):
        self.loc = [screen.get_size()[0] / 2, screen.get_size()[1] / 2]
        self.vel = [0,0]
        self.scale = 20
        self.speedmax = 20 / self.scale

    def get_loc(self):
        return tuple(self.loc)
    
    def right(self):
        if self.vel[0] < self.speedmax:
            self.vel[0] += 1/self.scale

    def left(self):
        if self.vel[0] > -self.speedmax:
            self.vel[0] -= 1/self.scale

    def down(self):
        if self.vel[1] < self.speedmax:
            self.vel[1] += 1/self.scale

    def up(self):
        if self.vel[1] > -self.speedmax:
            self.vel[1] -= 1/self.scale
    
    def move(self):
        for i in (0,1):
            self.loc[i] += self.vel[i]
            self.loc[i] %= screen.get_size()[i]

char = acc()
def rand(scale=256):
    return int(rn.random()*scale)
clock = pygame.time.Clock()
while ongoing:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            ongoing = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                char.up()
            if event.key == pygame.K_s:
                char.down()
            if event.key == pygame.K_a:
                char.left()
            if event.key == pygame.K_d:
                char.right()
            if event.key == pygame.K_ESCAPE:
                ongoing = False
    
    char.move()

    screen.fill((255,255,255))

    pygame.draw.circle(screen,(255,0,0),char.loc,5)

    pygame.display.flip()
    clock.tick()