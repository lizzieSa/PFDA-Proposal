import pygame


class Cake():
    def __init__(self, pos=(0, 0), size=210):
        self.pos = pos
        self.size = size
        self.color = pygame.Color(0, 255, 0)
        cake_flavour = input("Cake flavour? ")
        flavour = cake_flavour.lower()
        if flavour == "red":
            self.color = pygame.Color(255,0,0)
        elif flavour == "green":
            self.color = pygame.Color(0,255,0)
        elif flavour == "blue":
            self.color = pygame.Color(0,0,255)
        self.surface = self.update_surface()

    def update_surface(self):
        surf = pygame.Surface((self.size, self.size))
        surf.fill(self.color)
        return surf
    
    def draw(self, surface):
        surface.blit(self.surface, self.pos)

class Icing():
    def __init__(self, pos=(295, 195), size=210):
        self.pos = pos
        self.pos_2 = (295, 300)
        self.size = size
        self.color = pygame.Color(0, 255, 0)
        cake_flavour = input("Icing flavour? ")
        flavour = cake_flavour.lower()
        if flavour == "red":
            self.color = pygame.Color(255,0,0)
        elif flavour == "green":
            self.color = pygame.Color(0,255,0)
        elif flavour == "blue":
            self.color = pygame.Color(0,0,255)
        self.surface_top = self.update_surface(1)
        self.surface_bot = self.update_surface(2)

    def update_surface(self, topBottom):
        if topBottom == 1:
            surf = pygame.Surface((self.size, (self.size)-150))
        else:
            surf = pygame.Surface((self.size, 30))
        surf.fill(self.color)
        return surf
        
    
    def draw(self, surface):
        surface.blit(self.surface_top, self.pos)  
        surface.blit(self.surface_bot, self.pos_2) 

class Candles():
    def __init__(self, pos=(325, 135), size=210):
        self.pos = pos
        self.pos_2 = (385, 135)
        self.pos_3 = (445, 135)
        self.size = size
        self.color = pygame.Color(0, 255, 0)
        cake_flavour = input("Candle colour? ")
        flavour = cake_flavour.lower()
        if flavour == "red":
            self.color = pygame.Color(255,0,0)
        elif flavour == "green":
            self.color = pygame.Color(0,255,0)
        elif flavour == "blue":
            self.color = pygame.Color(0,0,255)
        self.surface_left = self.update_surface(1)
        self.surface_middle = self.update_surface(2)
        self.surface_right = self.update_surface(3)

    def update_surface(self, LeftRightMiddle):
        surf = pygame.Surface((30, 60))
        surf.fill(self.color)
        return surf
        
    
    def draw(self, surface):
        surface.blit(self.surface_left, self.pos)  
        surface.blit(self.surface_middle, self.pos_2) 
        surface.blit(self.surface_right, self.pos_3)


class Particle():

    def __init__(self, pos=(0, 0), size=15):
        self.pos = pos
        self.size = size
        self.color = pygame.Color(0, 255, 0)
        cake_flavour = input("Cake flavour? ")
        flavour = cake_flavour.lower()
        if flavour == "red":
            self.color = pygame.Color(255,0,0)
        elif flavour == "green":
            self.color = pygame.Color(0,255,0)
        elif flavour == "blue":
            self.color = pygame.Color(0,0,255)
        self.surface = self.update_surface()

    def update_surface(self):
        surf = pygame.Surface((self.size*0.8, self.size*0.8))
        surf.fill(self.color)
        return surf
    
    def draw(self, surface):
        for row in range(15):
            for col in range(15):
                surface.blit(self.surface, self.pos)

class Stuff():
    def __init__(self, pos=(0, 0), size=15):
        self.pos = pos
        self.size = size
        self.surface = self.update()
        self.particles = []

    def update(self):
        particle = Particle(self.pos, size=self.size)
        self.particles.insert(0, particle)
    
    def draw(self, surface, pos=(0,0), size = 50):
        self.pos = pos
        self.size = size
        surf = pygame.Surface((self.size, self.size))
        for row in range(15):
            for col in range(15):
                surface.blit(pygame.Surface((self.size, self.size)), self.pos)

class Cube():
    #i need to make multiple particles with different pos
    #when initializing i need to make a surface for the particles to fill
    def update(self, dt):
        particle = Particle(self.pos)
        self.particles.insert(0, particle)
        self._update_pos(dt)


    def _update_pos(self, dt):
            x, y = self.pos
            y += self.size
            self.pos = (x, y)

    def draw_cube():
        surface = pygame.Surface((105, 105))
        particle = Particle()
        for row in range(7):
            for col in range(7):
                surface.blit()




def main():
    '''icing_flavour = input("Icing flavour? ")
    topping_type = input("What toppings do you want? ")'''
    #print (f"flavour: {cake_flavour}")
    #print (f"icing: {icing_flavour}")
    #print (f"topping: {topping_type}")
    pygame.init()
    pygame.display.set_caption("Digital Rain")
    clock = pygame.time.Clock()
    resolution = (800, 600)
    particle = Cake()
    frosting = Icing()
    fires = Candles()
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
        particle.pos = ((resolution[0]//2)-105, (resolution[1]//2)-105)
        particle.draw(screen)
        frosting.draw(screen)
        fires.draw(screen)
        pygame.display.flip()
    pygame.quit()


if __name__ == "__main__":
    main()