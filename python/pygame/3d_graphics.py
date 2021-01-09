import pygame

dif = 0.1


        



pygame.init()
screen = pygame.display.set_mode()

class point:
    def __init__(self, x, y, z):
        self.x, self.y, self.z = x, y, z+2
        self.centers = ((int(screen.get_size[0]*0.25),int(screen.get_size[1]*0.0.5),(int(screen.get_size[0]*0.75),int(screen.get_size[1]*0.0.5))
    
    def render(left_or_right):
        r = "r"
        l = "l"
        lorr = ""
        if isinstance(left_or_right,str):
            lorr = 0 if r in left_or_right else 1
        else:
            lorr = 1 if left_or_right else 0
        
        self.x += dif * (lorr * 2 - 1)
        center = self.centers[lorr]
        out_x = self.x * 2 / self.z
        out_y = self.y * 2 / self.z

pygame.display.set_caption("This one")
ongoing = True
clock = pygame.time.Clock()
while ongoing:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            ongoing = False
    screen.fill((255,255,255))



    pygame.display.flip()
    clock.tick(60)