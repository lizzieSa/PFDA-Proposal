import pygame

pygame.font.init()


class Cake():
    def __init__(self, pos=(0, 0), size=210):
        self.pos = pos
        self.size = size
        self.color = pygame.Color(0, 255, 0)
        cake_flavour = input("Would you like vanilla, strawberry or chocolate flavour cake? ")
        flavour = cake_flavour.lower()
        if flavour == "vanilla":
            self.color = pygame.Color(255,250,205)
        elif flavour == "strawberry":
            self.color = pygame.Color(240,128,128)
        elif flavour == "chocolate":
            self.color = pygame.Color(160,82,45)
        else:
            print("Well we dont have that so you're getting vanilla, I hope you're happy.")
            self.color = pygame.Color(255,250,205)
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
        cake_flavour = input("Icing flavour? Same choices, vanilla, chocolate or strawberry? ")
        flavour = cake_flavour.lower()
        if flavour == "vanilla":
            self.color = pygame.Color(255,250,240)
        elif flavour == "chocolate":
            self.color = pygame.Color(139,69,19)
        elif flavour == "strawberry":
            self.color = pygame.Color(220,20,60)
        else:
            print ("Did I say that was an option? ")
            self.color = pygame.Color(255,0,0)
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
        cake_flavour = input("Candle colour? We have yellow, cyan and magenta. ")
        flavour = cake_flavour.lower()
        if flavour == "cyan":
            self.color = pygame.Color(0,255,255)
        elif flavour == "yellow":
            self.color = pygame.Color(255,255,102)
        elif flavour == "magenta":
            self.color = pygame.Color(255,20,147)
        else:
            print("Are you sure that's even a color?")
            self.color = pygame.Color(255,20,147)
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

class Bomb():
    def __init__(self, pos=(295, 195), size=210):
        self.pos = pos
        self.size = size
        self.color = pygame.Color(130, 130, 130)
        self.surface = self.update_surface()

    def update_surface(self):
        surf = pygame.Surface((self.size, self.size))
        pygame.draw.circle(surf, self.color, (220//2, 195//2), 195//2)
        return surf
    
    def draw(self, surface):
        surface.blit(self.surface, self.pos)
    
class Fuse():
    def __init__(self, pos=(392, 105), size=500):
        self.pos = pos
        self.size = size
        self.color = pygame.Color(240,230,140)
        self.surface = self.update_surface()

    def update_surface(self):
        surf = pygame.Surface((25, 110))
        surf.fill(self.color)
        return surf
    
    def draw(self, surface):
        surface.blit(self.surface, self.pos)

class Tip():
    def __init__(self, pos=(392, 105), size=500):
        self.pos = pos
        self.size = size
        self.color = pygame.Color(255,0,0)
        self.surface = self.update_surface()

    def update_surface(self):
        surf = pygame.Surface((25, 25))
        surf.fill(self.color)
        return surf
    
    def draw(self, surface):
        surface.blit(self.surface, self.pos)

class BiteMark():
    def __init__(self, pos=(290, 190), size=100):
        self.pos = pos
        self.size = size
        self.color = pygame.Color(130, 130, 130)
        self.surface = self.update_surface()

    def update_surface(self):
        surf = pygame.Surface((self.size, self.size))
        pygame.draw.circle(surf, self.color, (220//2, 195//2), 195//2)
        return surf
    
    def draw(self, surface):
        surface.blit(self.surface, self.pos)

class toEat():
    def __init__(self, pos=(200, 450), size=210):
        self.pos = pos
        self.size = size
        #FONTS = pygame.font.get_fonts()
        self.font = pygame.font.SysFont('badaboombbreg', 50)
        self.surface = self.update_surface()

    def update_surface(self):
        surf = pygame.Surface((self.size, self.size))
        surf.fill((0,0,0))
        return surf
    
    def draw(self, surface):
        surface.blit(pygame.font.Font.render(self.font, f"Press space to eat!", True, (255,255,255)), self.pos)

class Suspicion():
    def __init__(self, pos=(200, 450), size=210):
        self.pos = pos
        self.size = size
        #FONTS = pygame.font.get_fonts()
        self.font = pygame.font.SysFont('badaboombbreg', 50)
        self.surface = self.update_surface()

    def update_surface(self):
        surf = pygame.Surface((self.size, self.size))
        surf.fill((0,0,0))
        return surf
    
    def draw(self, surface):
        surface.blit(pygame.font.Font.render(self.font, f"Wait a minute...", True, (255,255,255)), self.pos)

class Surprise():
    def __init__(self, pos=(200, 450), size=210):
        self.pos = pos
        self.size = size
        #FONTS = pygame.font.get_fonts()
        self.font = pygame.font.SysFont('badaboombbreg', 50)
        self.surface = self.update_surface()

    def update_surface(self):
        surf = pygame.Surface((self.size, self.size))
        surf.fill((0,0,0))
        return surf
    
    def draw(self, surface):
        surface.blit(pygame.font.Font.render(self.font, f"The cake is a LIE!!!", True, (255,255,255)), self.pos)

def main():
    pygame.init()
    pygame.display.set_caption("Bake Your Cake and Eat it Too!")
    clock = pygame.time.Clock()
    resolution = (800, 600)
    particle = Cake()
    frosting = Icing()
    fires = Candles()
    lie = Bomb()
    stick = Fuse()
    lighter = Tip()
    bite = BiteMark()
    text1 = toEat()
    text2 = Suspicion()
    text3 = Surprise()
    screen = pygame.display.set_mode(resolution)
    running = True
    cakedraw = True
    bombdraw = False
    spacecount = 0
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
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE and spacecount == 0:
                spacecount += 1
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE and spacecount == 1:
                spacecount += 1
                cakedraw = False
                bombdraw = True
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE and spacecount == 2:
                spacecount += 1
                cakedraw = False
                bombdraw = False

        black = pygame.Color(0, 0, 0)
        screen.fill(black)
        if bombdraw:
            stick.draw(screen)
            lie.draw(screen)
            lighter.draw(screen)
            text3.draw(screen)
        if cakedraw:
            particle.pos = ((resolution[0]//2)-105, (resolution[1]//2)-105)
            particle.draw(screen)
            frosting.draw(screen)
            fires.draw(screen)
            if spacecount == 0:
                text1.draw(screen)
            if spacecount == 1:
                text2.draw(screen)
                bite.draw(screen)


        pygame.display.flip()
    pygame.quit()


if __name__ == "__main__":
    main()