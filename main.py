# MODULES
import pygame
import easy_mode
import medium_mode
import hard_mode

# create game window
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Tic-Tac-Toe")

# game variables
game_continue = False
menu_state = "main"

# define fonts
font = pygame.font.SysFont("Snap ITC", 40)
font1 = pygame.font.SysFont("Snap ITC", 60)

# define colours
TEXT_COL = (61, 61, 61)


# functions
def draw_text(text, font, text_col, x, y):
    img = font.render(text, True, text_col)
    screen.blit(img, (x, y))


def false():
    return 0


# button class
class Button:
    def __init__(self, x, y, image, scale, func=false):
        width = image.get_width()
        height = image.get_height()
        self.image = pygame.transform.scale(image, (int(width * scale), int(height * scale)))
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        self.clicked = False
        self.func = func

    def draw(self, surface):
        action = False
        # get mouse position
        pos = pygame.mouse.get_pos()

        # check mouseover and clicked conditions
        if self.rect.collidepoint(pos):
            if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
                self.clicked = True
                action = True
                surface.fill((255, 255, 255))
                self.func()
        if pygame.mouse.get_pressed()[0] == 0:
            self.clicked = False

        # draw button on screen
        surface.blit(self.image, (self.rect.x, self.rect.y))

        return action


# load button images
resume_img = pygame.image.load("resume.png")
levels_img = pygame.image.load("levels.png")
quit_img = pygame.image.load("quit.png")
easy_img = pygame.image.load('easy.png')
medium_img = pygame.image.load('medium.png')
hard_img = pygame.image.load('hard.png')
back_img = pygame.image.load('back.png')

# create button instances
resume_button = Button(180, 220, resume_img, 1)
levels_button = Button(180, 320, levels_img, 1, false)
quit_button = Button(180, 420, quit_img, 1)
easy_button = Button(180, 30, easy_img, 1, easy_mode.main)
medium_button = Button(180, 130, medium_img, 1, medium_mode.main)
hard_button = Button(180, 230, hard_img, 1, hard_mode.main)
back_button = Button(180, 500, back_img, 1)

# Game loop
run = True
while run:
    screen.fill((255, 255, 255))
    if game_continue:
        # check menu state
        if menu_state == "main":
            # draw 2 options(levels,quite) screen buttons
            draw_text("Tic Tac Toe", font1, TEXT_COL, 110, 50)
            if levels_button.draw(screen):
                menu_state = "levels"
            if quit_button.draw(screen):
                run = False
        # check if the levels menu is opened
        if menu_state == "levels":
            # draw the levels options and back buttons
            if easy_button.draw(screen):
                print("Easy")
            if medium_button.draw(screen):
                print("Medium")
            if hard_button.draw(screen):
                print("Hard")
            if back_button.draw(screen):
                menu_state = "main"
    else:
        draw_text("Welcome!", font, TEXT_COL, 190, 220)
        draw_text("Press SPACE to start", font, TEXT_COL, 45, 320)

    # event handler
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                game_continue = True
            if event.key == pygame.K_ESCAPE:
                if menu_state == "levels":
                    menu_state = "main"
                else:
                    game_continue = False
        if event.type == pygame.QUIT:
            run = False
    pygame.display.update()
pygame.quit()
