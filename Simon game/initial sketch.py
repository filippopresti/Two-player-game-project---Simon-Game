# References
''' Window's icon
    <a href="https://www.flaticon.com/free-icons/simon" title="simon icons">Simon icons created by Freepik - Flaticon</a>
'''
# Importing the library
import pygame
from random import randrange

# Initializing Pygame
pygame.init()

# Global variables
screen_width = 800
screen_height = 800
button_size = 200
gap_size = 20
score = 0
pattern = []

# INTERFACE

# Create the screen and set its width and height
screen = pygame.display.set_mode((screen_width, screen_height))

# Set window's caption and icon

pygame.display.set_caption("Simon Game")
icon = pygame.image.load("images\icon.png")
pygame.display.set_icon(icon)

# Assigning background color
screen.fill((100, 100, 100)) # Assign color to the background

# Buttons colours
# Regular shades
yellow = (254, 201, 0)
blue = (0, 147, 237)
red= (254, 0, 0)
green = (0, 210, 93)
# Darker shades
darker_yellow = (204, 151, 0)
darker_blue = (0, 97, 187)
darker_red= (204, 0, 0)
darker_green = (0, 160, 43)

# Screen margins calculations to position the four buttons
margin_X = int((screen_width - (2 * button_size) - gap_size) / 2)
margin_Y = int((screen_height - (2 * button_size) - gap_size) / 2)

# Buttons coordinates which are used to then draw the rectangles 
yellow_btn = pygame.Rect(margin_X, margin_Y, button_size, button_size)
blue_btn   = pygame.Rect(margin_X + button_size + gap_size, margin_Y, button_size, button_size)
red_btn    = pygame.Rect(margin_X, margin_Y + button_size + gap_size, button_size, button_size)
green_btn  = pygame.Rect(margin_X + button_size + gap_size, margin_Y + button_size + gap_size, button_size, button_size)

#Scoring
score_value = 0
font = pygame.font.SysFont("arial", 30)
textX = 10
textY = 10

def show_score(x, y):
    score = font.render("Score: " + str(score_value), True, (255, 255, 255))
    screen.blit(score, (x, y))

def start_playing():
    pattern.append(randrange(4))
    print(pattern[-1])

start_playing()

# Scoring call
show_score(textX, textY)

# Game Loop
# Show screen until exit button isn't pressed 

running = True
fakeid = pattern[-1]
while running:

    # Draw buttons

    if fakeid == 0:
        pygame.draw.rect(screen, darker_yellow, yellow_btn, border_radius= 20)
    else:
        pygame.draw.rect(screen, yellow, yellow_btn, border_radius= 20)

    if fakeid == 1:
        pygame.draw.rect(screen, darker_blue, blue_btn, border_radius= 20)
    else:
        pygame.draw.rect(screen, blue, blue_btn, border_radius= 20)

    if fakeid == 2:
        pygame.draw.rect(screen, darker_red, red_btn, border_radius= 20)
    else:
        pygame.draw.rect(screen, red, red_btn, border_radius= 20)
    
    if fakeid == 3:
        pygame.draw.rect(screen, darker_green, green_btn, border_radius= 20)
    else:
        pygame.draw.rect(screen, green, green_btn, border_radius= 20)

    #start_playing()
    # Close window when quit button is pressed
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    pygame.display.flip() # Update the full display screen to the window screen