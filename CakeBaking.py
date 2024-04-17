import random
import pygame
import math


class Cake():
    def pixel_batter(self, color):
        pixel = pygame.Surface((self.size*0.8, self.size*0.8))
        pixel.fill(color)

    def flavour(size, self, pixel_batter,flavour): 
        
        Taste = ()
        for row in range(size):
            for col in range(size):
                if Taste == Taste:
                    print(pixel_batter(self,Taste))
                else:
                    print("🟩", end="")
               

        

    def draw_cake(self, surface):
        if self.dead:
            return
        self.surface.set_alpha(self.alpha)
        self.surface
        surface.blit(self.surface, self.pos)    

     
class Explosion():

    def init_(self, pos=(0,0), size=100):
        self.pos = pos
        self.size = size
        self. color = pygame. Color(255, 0, 0)
        self.age = 0 # in milliseconds
        self. alpha = 255
        self. surface = self.update_surface()

    def update(self, dt):
        self. age += dt
        self.alpha = 255 * (math.sin(math.radians (self.age)) + 1) / 2

    def update_surface(self) :
        surf = pygame. Surface((self.size, self.size))
        surf.fill(self.color)
        return surf

    def draw(self, surface):
        surface. blit (self. surface, self.pos)  

        

def main():
    pygame.init()
    pygame.display.set_caption("Make your Cake and Eat it Too!")
    clock = pygame.time.Clock()
    dt = 0
    resolution = (800, 600)
    screen = pygame.display.set_mode(resolution)
    running = True
    while running:
        black = pygame.Color(0, 0, 0)
        screen.fill(black)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN and event.key == pygame.K_f:
                pygame.display.toggle_fullscreen()
        pygame.display.flip()
        dt = clock.tick(12)
    pygame.quit()

if __name__ == "__main__":
    main()