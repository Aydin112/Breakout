import pygame
import sys
from time import sleep 
import math 
import random

points = 0

class box:
    def __init__(self, starting_health: int, x: int, y: int):
        self.health = starting_health
        self.x = x
        self.y = y
        self.colours = [
            "black",
            "red",
            "orange",
            "yellow",
            "cyan",
            "blue",
            "green",
            ""
        ]
        self.alive = True
        

    def render(self):
        if self.alive:
            pygame.draw.rect(screen, self.colours[self.health], (self.x - 20, self.y - 10, 40, 20))

    def collision(self) -> bool:
        if self.alive:
            if(self.x-20<ball_position.x<self.x+20):
                if(self.y-10<ball_position.y<self.y+10):
                    self.health -= 1
                    if self.health <= 0:
                        self.alive = False
                        pipe.play()
                    return True
        return False









# pygame setup
pygame.init()
pygame.mixer.init()
oof = pygame.mixer.Sound("/home/aydin/Documents/roblox-death-sound-effect.wav")
pipe=pygame.mixer.Sound("/home/aydin/Documents/metal-pipe-clang.wav")
vine=pygame.mixer.Sound("/home/aydin/Documents/vine-boom.wav")


screen = pygame.display.set_mode((720, 1000))
pygame.display.set_caption('Breakout Indev')
clock = pygame.time.Clock()
running = True
font = pygame.font.SysFont('Arial', 48)

ball_position = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 1.2)
x_speed = 9
y_speed = -9


controller_x = screen.get_width() / 2
controller_y = 900
controller_width = 300
controller_height = 20
controller_move_speed = 16

level=1

#create blocks


level1 = [
    box(6, 200, 50), 
    box(6, 200, 75), 
    box(6, 200, 100), 
    box(6, 200, 125), 
    box(6, 150, 150), box(6, 200, 150), box(6, 250, 150),
    box(6, 150, 175), box(6, 200, 175), box(6, 250, 175),
    box(6, 150, 200), box(6, 200, 200), box(6, 250, 200),
     box(6, 150, 225), box(6, 200, 225), box(6, 250, 225),
     box(6, 150, 250), box(6, 200, 250), box(6, 250, 250),
     box(6, 150, 275), box(6, 200, 275), box(6, 250, 275),
    
    
]


level2 = [
box(4, 600,400)

]





current_level = level1

while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # fill the screen with a color to wipe away anything from last frame
    screen.fill("black")

    # Get the state of all keyboard buttons
    keys = pygame.key.get_pressed()


    #Bouncing
    if(ball_position.x>=720):
        x_speed= -x_speed

    if(ball_position.x<=0):
        x_speed= -x_speed
        
    if(ball_position.y<=0):
        y_speed= -y_speed

    if(ball_position.y>=1000):
        running = False
        print("GAME OVER, Restart to play again:)")
        oof.play()
    
     

    if(ball_position.y>=controller_y):
        if(controller_x < ball_position.x < controller_x + controller_width):
            y_speed= -abs(y_speed)

    # MOVEMENT
    ball_position.y += y_speed
    ball_position.x += x_speed


    # Move the rectangle based on arrow key presses
    if keys[pygame.K_LEFT]:
        if controller_x > 0:
            controller_x -= controller_move_speed
            

    if keys[pygame.K_RIGHT]:
        if controller_x + controller_width < 720:
            controller_x += controller_move_speed


    # Box Collisoins

    for box_item in current_level:
        if(box_item.collision() == True):
            y_speed = -y_speed*(random.random()*0.1+1)
            x_speed = -x_speed*(random.random()*0.2+1)
            points +=1
            vine.play()


    #levels

    if points==14:
        current_level = level2
     

    # RENDER YOUR GAME HERE
    pygame.draw.circle(screen, "white", ball_position, 10)

    pygame.draw.rect(screen, "white", (controller_x, controller_y, controller_width, controller_height))

    for box_item in current_level:
        box_item.render()


    text_surface = font.render("Score= "+str(points), True, (255, 255, 255))  # White color

    screen.blit(text_surface, (500, 20))





    # flip() the display to put your work on screen
    pygame.display.flip()

    clock.tick(60)  # limits FPS to 60


    if running == False:
            text_surface = font.render("Game Over", True, (255, 255, 255))  # White color

            screen.blit(text_surface, (350, 500))
            pygame.display.flip()
            sleep(5)
























pygame.quit()
sys.exit()