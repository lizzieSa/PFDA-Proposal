import pygame


class Cake():
    '''def pixel_batter(self, color, size, cake_flavour):
        color = cake_flavour
        surf = pygame.Surface((self.size*0.8, self.size*0.8))
        surf.fill((color))'''
      
    def cake_fill(cake_flavour,self):
        surf = pygame.Surface((self.size*0.8, self.size*0.8))
        #surf.fill((0,0,0))
        surf = pygame.Surface((300, 300))
        for pixel in surf:
            flavour = cake_flavour.lower()
            if flavour == "red":
                color = (255,0,0)
            elif flavour == "green":
                color = (0,255,0)
            elif flavour == "blue":
                color = (0,0,255)
            surf.fill(color )

    def draw(self, surf):
        surf.blit(self.surface, self.pos) 
    
class Particle():

    def __init__(self, pos=(0, 0),size = 15):
        cake_flavour = input("Cake flavour? ")
        flavour = cake_flavour.lower()
        if flavour == "red":
            color = pygame.Color(255,0,0)
        elif flavour == "green":
            color = pygame.Color(0,255,0)
        elif flavour == "blue":
            color = pygame.Color(0,0,255) 
        self.pos = pos
        self.size = size
        self.color = pygame.Color(0, 255, 0)

        self.surface = self.update_surface()

    def update_surface(self):
        surf = pygame.Surface((self.size*0.8, self.size*0.8))
        surf.fill(self.color)
        return surf
    
    def draw(self, surface):
        surface.blit(self.surface, self.pos)

class Cube():
    def __init__(self,pos=(0,0), size = 50):
        self.pos= pos
        self.size = size
        self.particles = []
        counter = 10
        for row in range(counter):
            for col in range(size):
                surface.blit(self.surface, self.pos)
        

    def grid_pattern(self, surface, size = 50):
        for row in range(size):
            for col in range(size):
                surface.blit(self.surface, self.pos)
               
        print()


def main():
    '''icing_flavour = input("Icing flavour? ")
    topping_type = input("What toppings do you want? ")'''
    #print (f"flavour: {cake_flavour}")
    #print (f"icing: {icing_flavour}")
    #print (f"topping: {topping_type}")
    pygame.init()
    pygame.display.set_caption("Digital Rain")
    clock = pygame.time.Clock()
    dt = 0
    resolution = (800, 600)
    particle = Particle()
    screen = pygame.display.set_mode(resolution)
    running = True
    while running:
        #cake = CakeStuff()
        #cake_fill(cake_flavour).draw(screen)
        #screen.fill(cake_fill(cake_flavour))
        #screen.blit(cake_fill(cake_flavour))
        pygame.display.flip()
        dt = clock.tick(12)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN and event.key == pygame.K_f:
                pygame.display.toggle_fullscreen()
        
        black = pygame.Color(0, 0, 0)
        screen.fill(black)
        particle.pos = (resolution[0]//2, resolution[1]//2)
        particle.draw(screen)
        pygame.display.flip()
    pygame.quit()


if __name__ == "__main__":
    main()