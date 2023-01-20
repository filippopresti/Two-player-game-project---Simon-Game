# References
'''
Window's bar icon: "https://www.flaticon.com/free-icons/simon"
Tick icon for scoring board: "https://www.flaticon.com/free-icons/tick"
Cross icon for scoring board: "https://www.flaticon.com/free-icons/cross"
Billy font: "https://www.behance.net/gallery/16190081/billy-typeface-(free)"
Lacquer font: "https://fonts.google.com/specimen/Lacquer"
Arial Rounded Bold MT font: "https://www.download-free-fonts.com/details/92774/arial-rounded-mt-bold"
'''

# Importing the library
import pygame
from random import randint
from time import sleep

# Initializing Pygame
pygame.init()

# Global variables
screen_width = 800
screen_height = 800
bg_color = (0, 0, 120)
square_size = 200
gap_size = 20
scoring_board_size = 50

# Text and fonts variables
text_color = (255, 255, 255)
billy_font = ("fonts/billy.ttf")
lacquer_font = ("fonts/lacquer.ttf")
arial_bold_font = ("fonts/arialbold.ttf")
game_over = pygame.font.Font(lacquer_font, 100)
winner = pygame.font.Font(lacquer_font, 40)
headline = pygame.font.Font(lacquer_font, 50)
large = pygame.font.Font(lacquer_font, 26)
regular = pygame.font.Font(billy_font, 32)
small = pygame.font.Font(arial_bold_font, 19)
instruction = pygame.font.Font(arial_bold_font, 16)

# Squares' colours
#  - Regular shades
yellow = (254, 201, 0)
blue = (0, 147, 237)
red= (254, 0, 0)
green = (0, 210, 93)
# - Darker shades
darker_yellow = (204, 151, 0)
darker_blue = (0, 97, 187)
darker_red= (204, 0, 0)
darker_green = (0, 160, 43)

# Set window's width and height
screen = pygame.display.set_mode((screen_width, screen_height))

# Set window's caption
pygame.display.set_caption("Simon Game")

# Set window's icon
icon = pygame.image.load("images/icon.png")
pygame.display.set_icon(icon)

# Screen margins calculations to position the four squares
margin_X = int((screen_width - (2 * square_size) - gap_size) / 2)
margin_Y = int((screen_height + scoring_board_size - (2 * square_size) - gap_size) / 2)

# Load button play and quit images
play_img = pygame.image.load('images/button_play.png').convert_alpha()
quit_img = pygame.image.load('images/button_quit.png').convert_alpha()

# Game Squares class
class Square():
        def __init__(self, color, darker_color, pos):
            self.color = color
            self.dark_color = darker_color
            self.rect = pygame.Rect(pos)

        # Draw square function
        def draw(self, color=False):
            if color == False:
                color = self.color
            pygame.draw.rect(screen, color, self.rect, border_radius = 20)
            #print('i am in Draw()')
            pygame.display.update()

        # Darker shade applied to squares when clicked then back to normal shade
        def dark_then_light(self):
            sleep(.4)
            #print('i am here')
            self.draw(self.dark_color)
            #print('did u see the dark?')
            sleep(.4)
            self.draw(self.color)

# Menu Buttons class
class Button():
    def __init__(self, x, y, image):
        self.image = image
        self.rect = self.image.get_rect() # Creates rectangle from the image
        self.rect.topleft = (x, y) # Assign x and y values to the top left corner of the rectangle
        self.clicked = False
    
    # Draw button function
    def draw(self):
        action = False
        # Get mouse position
        pos = pygame.mouse.get_pos()
        '''print(pos)''' # Shows mouse x and y coordinates

        # Check mouseover and clicked conditions
        if self.rect.collidepoint(pos):
            '''print('HOVER')''' # Shows if the mouse is on top of a button
            if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False: #[0 for lft click 1 for rgt click]
                #print('button clicked')
                self.clicked = True 
                action = True
        if pygame.mouse.get_pressed()[0] == 0: 
            self.clicked = False
        
        # Draw button on screen
        screen.blit(self.image, self.rect)
        return action 

# Draw text function
def draw_text(text, font, color, x, y):
    img = font.render(text, True, color)
    screen.blit(img, (x, y))

# Erase text function
def erase_text(x, y, width, height):
    pygame.draw.rect(screen, bg_color, (x, y, width, height))

# Display Menu + Instruction function
def display_menu():
    # Title
        draw_text("Simon Game", headline, text_color, 280, 30)
        # Instructions
        # 1
        draw_text("Start the game", large, text_color, 40, 130)
        draw_text(" - Press 'Play' button to begin. Simon will give only first signal;", instruction, yellow, 40, 170)
        # 2
        draw_text("First player", large, text_color, 40, 210)
        draw_text("- Player 1 repeats Simon's signal, and immediately adds one;", instruction, yellow, 40, 250)
        # 3
        draw_text("Second player", large, text_color, 40, 290)
        draw_text("- Player 2 repeats the first two signals (Simon + Player 1's signals) and adds one;", instruction, yellow, 40, 330)
        # 4
        draw_text("Keep playing", large, text_color, 40, 370)
        draw_text("- Game continues with both players repeating the previous sequence and adding a signal;", instruction, yellow, 40, 410)
        # 5
        draw_text("Stay focused", large, text_color, 40, 450)
        draw_text("- The first player who makes an error is out of the game;", instruction, yellow, 40, 490)
        # 6
        draw_text("The winner is...", large, text_color, 40, 530)
        draw_text("- The remaining player is the winner!", instruction, yellow, 40, 570)

# Display Scoring board function
def display_scoring_board():
    # Scoring board
    # Left side: Player 1 
    draw_text("PLAYER 1", large, text_color, 20, 25)
    draw_text("Score: 0", regular, text_color, 20, 60)
    # Middle: Turns info
    draw_text("Simon's    Turn", small, text_color, 300, 25)
    screen.blit(go_img, (480, 25))
    draw_text("Player 1's Turn", small, text_color, 300, 50)
    screen.blit(stop_img, (480, 50))
    draw_text("Player 2's Turn", small, text_color, 300, 75)
    screen.blit(stop_img, (480, 75))
    #Right side: Player 2
    draw_text("PLAYER 2", large, text_color, 660, 25)
    draw_text("Score: 0", regular, text_color, 660, 60)

# Create button instances
play_btn = Button(130, 690, play_img)
quit_btn = Button(498, 690, quit_img)

# Create squares instances
squares = [
    # Object - Regular shade - Darker shade of same colour - Coordinates which are used to then draw the square
    Square(pygame.Color(yellow), pygame.Color(darker_yellow), (margin_X, margin_Y, square_size, square_size)),
    Square(pygame.Color(blue), pygame.Color(darker_blue), (margin_X + square_size + gap_size, margin_Y, square_size, square_size)),
    Square(pygame.Color(red), pygame.Color(darker_red), (margin_X, margin_Y + square_size + gap_size, square_size, square_size)),
    Square(pygame.Color(green), pygame.Color(darker_green), (margin_X + square_size + gap_size, margin_Y + square_size + gap_size, square_size, square_size)),
    ]

# Game loop variables
run = True
first = 0
end_screen = True
main_menu = True
Simon_turn = True # Simon turn set to true since it will be the first to play
player1_turn = False # Player 1 turn
player2_turn = False # Player 2 turn
player1_score = 0 # Score counter for player 1
player2_score = 0 # Score counter for player 2
correct_list = []
temp_list = []
index = 0

# Set the size for scoring board's images
img_size = (25, 25)
# Load tick and cross image 
go_img = pygame.image.load("images/go.png")
stop_img = pygame.image.load("images/stop.png")
# Scale tick and cross image
go_img = pygame.transform.scale(go_img, img_size)
stop_img = pygame.transform.scale(stop_img, img_size)


def basic_draw():
    # Set background color
    screen.fill(bg_color) # Set screen color here in order to cover screen and show wanted screen
     # Display Scoring board
    display_scoring_board()
     # Display squares
    for square in squares:
        square.draw()
        #print('Drawing game screen')

def squares_only_draw(): # Once the game has started, draws only the squares again
    # Display squares
    for square in squares:
        square.draw()
        #print('Drawing only the squares')

# Square clicked function
def clicked_square(mouse_pos, squares):
    #Return the clicked square or None if no square was clicked
    for square in squares:
        if square.rect.collidepoint(mouse_pos):
            return square
    return None  # Return None if no square was clicked.

def draw_turn_info(input):
    if input == 'Simon':
        erase_text(480, 25, 25, 25)
        screen.blit(stop_img, (480, 25))
    elif input == 'P1 GO':
        erase_text(480, 50, 25, 25)
        screen.blit(go_img, (480, 50))
    elif input == 'P2 GO':
        erase_text(480, 75, 25, 25)
        screen.blit(go_img, (480, 75))
    elif input == 'P1 STOP':
        erase_text(480, 50, 25, 25)
        screen.blit(stop_img, (480, 50))
    elif input == 'P2 STOP':
        erase_text(480, 75, 25, 25)
        screen.blit(stop_img, (480, 75))
    elif input == 'P1 Score':
        erase_text(78, 60, 40, 25)
        draw_text(str(player1_score), regular, text_color, 80, 60)
    elif input == 'P2 Score':
        erase_text(718, 60, 40, 25)
        draw_text(str(player2_score), regular, text_color, 720, 60)

# Game loop
while run:

    # Check Game Status - if True display main menu
    if main_menu == True:
        
        # Set background color
        screen.fill(bg_color)
        # Display main menu + instructions
        display_menu()

        # Display menu buttons
        if play_btn.draw(): # Check if play button is clicked
            main_menu = False # Skip to game screen
        if quit_btn.draw(): # Check if quit button is clicked
            run = False # Exit loop
            end_screen = False
            pygame.quit()
    # - if False display game screen   
    else: 
        
        if first == 0:
            basic_draw()
            first = 1
        
        # GAME LOGIC 
        if Simon_turn == True:
            sleep(0.5)
            Simon_turn = False
            ran = randint(0, 3)
            #print(ran)
            correct_list.append(squares[ran])
            #print(correct_list)
            squares[ran].dark_then_light()
            #print(squares[ran])
            squares_only_draw()
            player1_turn = True
            draw_turn_info('Simon')
        elif player1_turn == True:
            draw_turn_info('P1 GO')
            if event.type == pygame.MOUSEBUTTONDOWN and not player2_turn:
                temp_square = 0
                if index < len(correct_list):
                 temp_square = correct_list[index]
                
                index += 1
                square = clicked_square(event.pos, squares)
                #print('button pressed', square)
                if square is None:  # No button pressed
                    #print('no button pressed')
                    break
                elif square == temp_square:  # Correct button pressed
                    square.dark_then_light()
                    #print('pressed button was correct')
                elif index > len(correct_list):  # All buttons clicked
                       correct_list.append(square)
                       correct_list[-1].dark_then_light()
                       #print('new square added')
                       player2_turn = True
                       player1_turn = False
                       player1_score += 1
                       draw_turn_info('P1 Score')
                       draw_turn_info('P1 STOP')
                       index = 0
                else:  # Wrong button pressed.
                    run = False
                    #print('wrong button pressed')

        elif player2_turn == True:
            draw_turn_info('P2 GO')
            if event.type == pygame.MOUSEBUTTONDOWN and not player1_turn:
                temp_square = 0
                if index < len(correct_list):
                 temp_square = correct_list[index]
                
                index += 1
                square = clicked_square(event.pos, squares)
                #print('button pressed', square)
                if square is None:  # No button pressed
                    #print('no button pressed')
                    break
                elif square == temp_square:  # Correct button pressed
                    square.dark_then_light()
                    #print('pressed button was correct')
                elif index > len(correct_list):  # All buttons clicked
                       correct_list.append(square)
                       correct_list[-1].dark_then_light()
                       #print('new square added')
                       player2_turn = False
                       player1_turn = True
                       player2_score += 1
                       draw_turn_info('P2 Score')
                       draw_turn_info('P2 STOP')                       
                       index = 0
                else:  # Wrong button pressed.
                    run = False
                    #print('wrong button pressed')                                      
                
    # Event handler
    for event in pygame.event.get():
        
        if event.type == pygame.QUIT:
            run = False
            end_screen = False
            pygame.quit()
    
    pygame.display.update() # Updates the game window at each iteration of the code

screen.fill(bg_color)
if player1_turn == False:
    draw_text('GAME OVER!!!', game_over, red, 95, 250)
    string = 'Player 1 is the winner with ' + str(player1_score) + ' pt.'
    draw_text(string, winner, green, 87, 400)
else:
    draw_text('GAME OVER!!!', game_over, red, 95, 250)
    string = 'Player 2 is the winner with ' + str(player2_score) + ' pt.'
    draw_text(string, winner, green, 87, 400)

pygame.display.update() 

while end_screen:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            end_screen = False

pygame.quit()