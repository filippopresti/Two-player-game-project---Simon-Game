# References
'''
Window's icon
"https://www.flaticon.com/free-icons/simon"
Tick icon for scoring board
"https://www.flaticon.com/free-icons/tick"
Cross icon for scoring board
"https://www.flaticon.com/free-icons/cross"
Billy font for text
"https://www.behance.net/gallery/16190081/billy-typeface-(free)"
'''

### Importing the library
from random import randrange
from time import sleep
import pygame

### Initializing Pygame
pygame.init()

# Global variables
screen_width = 800
screen_height = 800
square_size = 200
gap_size = 20
scoring_board = 50
bg_color = (0, 0, 100)
regular_text_color = (255, 255, 255)

good_dog_font = ("fonts/GoodDog.ttf")
billy_font =("fonts/billy.ttf")

# Set window's caption
pygame.display.set_caption("Simon Game")

# Set window's icon
icon = pygame.image.load("images/icon.png")
pygame.display.set_icon(icon)

# Set window's width and height
screen = pygame.display.set_mode((screen_width, screen_height))

# Set background color
screen.fill(bg_color) #inside game loop

# Screen margins calculations to position the four squares
margin_X = int((screen_width - (2 * square_size) - gap_size) / 2)
margin_Y = int((screen_height + scoring_board - (2 * square_size) - gap_size) / 2)

# Squares class
class Square:
    def __init__(self, screen, color, darker_color, pos):
        self.color = color
        self.screen = screen
        self.darker_color = darker_color
        self.rect = pygame.Rect(pos)
        # self.draw(screen, self.color)

    def draw(self, color=False):
        if color == False:
            color = self.color
        pygame.draw.rect(screen, color, self.rect, border_radius = 20)
        #pygame.display.update()

    def dark_then_light(self):
        self.draw(self.darker_color)
        sleep(.5)
        self.draw(self.color)

    # Square clicked function
    def clicked_square(mouse_pos, squares):
        """Return the clicked square or None if no square was clicked."""
        for square in squares:
            if square.rect.collidepoint(mouse_pos):
                return square
        return None  # Return None if no square was clicked.


# Draw text function
def draw_text(text, font, color, x, y):
    text_surface = font.render(text, True, color)
    screen.blit(text_surface, (x, y))

# Erase text function
def erase_text():
    pygame.draw.rect(screen, bg_color, (0, 0, 450, 25))

# Define different size text for the same font
large_font = pygame.font.Font(billy_font, 40)
regular_font = pygame.font.Font(billy_font, 32)
small_font = pygame.font.Font(pygame.font.match_font('arial'), 24)
#small_font = pygame.font.Font(billy_font, 28)

run = False
exit = True
player1_turn = True # Player 1 turn
player2_turn = False # Player 2 turn
score = 0 
# player1_score = 0 # Score counter for player 1
# player2_score = 0 # Score counter for player 2
correct_list = []
index = 0
# Squares colours
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
squares = [
    # Object - Regular shade - Darker shade of same colour - Coordinates which are used to then draw the square
    Square(screen, pygame.Color(yellow), pygame.Color(darker_yellow), (margin_X, margin_Y, square_size, square_size)),
    Square(screen, pygame.Color(blue), pygame.Color(darker_blue), (margin_X + square_size + gap_size, margin_Y, square_size, square_size)),
    Square(screen, pygame.Color(red), pygame.Color(darker_red), (margin_X, margin_Y + square_size + gap_size, square_size, square_size)),
    Square(screen, pygame.Color(green), pygame.Color(darker_green), (margin_X + square_size + gap_size, margin_Y + square_size + gap_size, square_size, square_size)),
    ]

# Set the size for scoring board's images
img_size = (25, 25)
# Load tick image 
go_img = pygame.image.load("images/go.png")
# Scale tick image
go_img = pygame.transform.scale(go_img, img_size)
# Load cross image 
stop_img = pygame.image.load("images/stop.png")
# Scale cross image
stop_img = pygame.transform.scale(stop_img, img_size)


# Scoring board
# Left side: Player 1 
draw_text("PLAYER 1", large_font, regular_text_color, 20, 25)
draw_text("Score:", regular_font, regular_text_color, 20, 60)
# Middle: Turns info
draw_text("Simon's    Turn", small_font, regular_text_color, 300, 25)
screen.blit(go_img, (480, 25))
draw_text("Player 1's Turn", small_font, regular_text_color, 300, 50)
screen.blit(stop_img, (480, 50))
draw_text("Player 2's Turn", small_font, regular_text_color, 300, 75)
screen.blit(stop_img, (480, 75))
# Right side: Player 2
draw_text("PLAYER 2", large_font, regular_text_color, 665, 25)
draw_text("Score:", regular_font, regular_text_color, 665, 60)

# display squares
for square in squares:
    square.draw()



# Simon starts
erase_text()
#draw_text(screen, "SIMON\'S TURN", regular_font, 225, 2)
pygame.display.update()
sleep(.5)

# Append references to the square objects instead of indices.
correct_list.append(squares[randrange(4)])


# Simon repeats all the colours in the list on  screen
for square in correct_list: 
    square.dark_then_light()
    sleep(.15)

# Game loop
run = True

while run:
    # Even handler
    for event in pygame.event.get():
        # Close window when quit button is pressed
        if event.type == pygame.QUIT:
            run = False
            exit = False

        # Keep playing when mouse square is pressed
        elif event.type == pygame.MOUSEBUTTONDOWN:
            correct_square= correct_list[index]
            square = Square.clicked_square(event.pos, squares)
            if square is None:  # No square pressed
                break
            elif square == correct_square:  # Correct square pressed
                square.dark_then_light(screen)
                index += 1
                if index == len(correct_list):  # All squares clicked correctly
                    score += 1
                    index = 0
            else:  # End game when wrong square is pressed
                running = False

while exit:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit = False

pygame.quit()