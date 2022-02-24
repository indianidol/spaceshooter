import pygame
import os
import time
import random
pygame.font.init()

WIDTH, HEIGHT =500,600
WIN = pygame.display.set_mode((WIDTH,HEIGHT))

pygame.display.set_caption("Life's trouble Shooter")



# Load Images
RED_SPACE_SHIP = pygame.image.load(os.path.join("assets", "pixel_ship_red_small.png"))
GREEN_SPACE_SHIP = pygame.image.load(os.path.join("assets", "pixel_ship_green_small.png"))
BLUE_SPACE_SHIP = pygame.image.load(os.path.join("assets", "pixel_ship_blue_small.png"))


# Player Ship
YELLOW_SPACE_SHIP = pygame.image.load(os.path.join("assets", "pixel_ship_yellow.png"))

# Lasers
RED_LASER = pygame.image.load(os.path.join("assets", "pixel_laser_red.png"))
YELLOW_LASER = pygame.image.load(os.path.join("assets", "pixel_laser_yellow.png"))
BLUE_LASER = pygame.image.load(os.path.join("assets", "pixel_laser_blue.png"))
GREEN_LASER = pygame.image.load(os.path.join("assets", "pixel_laser_green.png"))

# Background
BG = pygame.transform.scale(pygame.image.load(os.path.join("assets", "background-black.png")),(WIDTH,HEIGHT))

class Ship:
    def __init__(self, x,y,health=100):
        self.x=x
        self.y=y
        self.health= health
        self.ship_img=None
        self.laser= []
        self.laser_img=None
        self.cool_down_counter = 0
        
    def draw(self, window):
        pygame.draw.rect(window, (255, 0, 0), (self.x,self.y, 50, 50),0)   
        # pygame.draw.rect(window, (255, 0, 0), (350, 350,50, 50),0)   
        # pygame.draw.circle(window,(255,0,0) ,(200,50), 40) 
        
        
def main():
    run = True
    FPS = 60
    level = 1
    lives = 5
    main_font = pygame.font.SysFont("comicsans",50)
    
    player_vel = 5
    
    ship = Ship(225,550)
    
    clock = pygame.time.Clock()
    
    def redraw_window():
        WIN.blit(BG,(0,0))
        
        # draw text
        level_label = main_font.render(f"Level: {level}",1, (255, 255, 255))
        lives_label = main_font.render(f"Lives: {lives}",1, (255, 255, 255))
        
        WIN.blit(lives_label,(10,10))
        WIN.blit(level_label,(WIDTH - level_label.get_width()-10,10))
        
        
        ship.draw(WIN)
        
        
        pygame.display.update()
        
        
    while run:
        clock.tick(FPS)
        redraw_window()
        
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                run=False        
        
        keys = pygame.key.get_pressed()
        if keys[pygame.K_a]  and ship.x - player_vel > 0: #left
            ship.x -= player_vel      
        if keys[pygame.K_d]  and ship.x+50 + player_vel < WIDTH: # right
            ship.x += player_vel
        if keys[pygame.K_w]  and ship.y - player_vel > 0: # UP
            ship.y -= player_vel
        if keys[pygame.K_s]  and ship.y+50 + player_vel < HEIGHT:# down
            ship.y += player_vel
                
main()                 