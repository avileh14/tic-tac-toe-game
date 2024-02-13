# MODULES
import pygame, sys
import numpy as np
from time import sleep

pygame.init()

# CONSTANTS

WIDTH = 600
HEIGHT = 600
LINE_WIDTH = 5
WIN_LINE_WIDTH = 7
BOARD_ROWS = 3
BOARD_COLS = 3
SQUARE_SIZE = 200
CIRCLE_RADIUS = 60
CIRCLE_WIDTH = 7
CROSS_WIDTH = 7
SPACE = 55

# RGB: red green blue

BG_COLOR = (61, 61, 61)
LINE_COLOR = (246, 252, 247)
CIRCLE_COLOR = (207, 23, 71)
CROSS_COLOR = (156, 224, 166)
TEXT_EVEN_COL = (255, 255, 255)
font = pygame.font.SysFont("Snap ITC", 72)

# SCREEN

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('הפרוייקט של ניצן, אבי וסהר')
screen.fill(BG_COLOR)

# CONSOLE BOARD

board = np.zeros((BOARD_ROWS, BOARD_COLS))

# SOUNDS

start_sound = pygame.mixer.Sound("mixkit-bonus-extra-in-a-video-game-2064.wav")
square_sound = pygame.mixer.Sound("mixkit-winning-a-coin-video-game-2069.wav")
circle_sound = pygame.mixer.Sound("mixkit-extra-bonus-in-a-video-game-2045.wav")
win_sound = pygame.mixer.Sound("ywwowoo.wav")

# FUNCTIONS

def draw_text(text, font, text_col, x, y):
    img = font.render(text, True, text_col)
    screen.blit(img, (x, y))

def draw_lines():
    # 1 horizontal
    pygame.draw.line(screen, LINE_COLOR, (0, SQUARE_SIZE), (WIDTH, SQUARE_SIZE), LINE_WIDTH)
    # 2 horizontal
    pygame.draw.line(screen, LINE_COLOR, (0, 2 * SQUARE_SIZE), (WIDTH, 2 * SQUARE_SIZE), LINE_WIDTH)
    # 1 vertical
    pygame.draw.line(screen, LINE_COLOR, (SQUARE_SIZE, 0), (SQUARE_SIZE, HEIGHT), LINE_WIDTH)
    # 2 vertical
    pygame.draw.line(screen, LINE_COLOR, (2 * SQUARE_SIZE, 0), (2 * SQUARE_SIZE, HEIGHT), LINE_WIDTH)

def draw_figures():
    for row in range(BOARD_ROWS):
        for col in range(BOARD_COLS):
            if board[row][col] == 1:
                pygame.draw.circle(screen, CIRCLE_COLOR, (
                int(col * SQUARE_SIZE + SQUARE_SIZE // 2), int(row * SQUARE_SIZE + SQUARE_SIZE // 2)), CIRCLE_RADIUS,
                                   CIRCLE_WIDTH)
            elif board[row][col] == 2:
                pygame.draw.line(screen, CROSS_COLOR,
                                 (col * SQUARE_SIZE + SPACE, row * SQUARE_SIZE + SQUARE_SIZE - SPACE),
                                 (col * SQUARE_SIZE + SQUARE_SIZE - SPACE, row * SQUARE_SIZE + SPACE), CROSS_WIDTH)
                pygame.draw.line(screen, CROSS_COLOR, (col * SQUARE_SIZE + SPACE, row * SQUARE_SIZE + SPACE),
                                 (col * SQUARE_SIZE + SQUARE_SIZE - SPACE, row * SQUARE_SIZE + SQUARE_SIZE - SPACE),
                                 CROSS_WIDTH)

def mark_square(row, col, player):
    board[row][col] = player
    if player == 1:
        circle_sound.play()
    if player == 2:
        square_sound.play()

def available_square(row, col):
    return board[row][col] == 0

def is_board_full():
    for row in range(BOARD_ROWS):
        for col in range(BOARD_COLS):
            if board[row][col] == 0:
                return False
    pygame.display.update()
    sleep(1)
    screen.fill(BG_COLOR)
    draw_text('TIE!',font,TEXT_EVEN_COL,200,250)
    return True

def check_win(player):
    # vertical win check
    for col in range(BOARD_COLS):
        if board[0][col] == player and board[1][col] == player and board[2][col] == player:
            draw_vertical_winning_line(col, player)
            pygame.display.update()
            sleep(1)
            if player == 1:
                screen.fill(BG_COLOR)
                draw_text('O WIN!',font,CIRCLE_COLOR,130,250)
            else:
                screen.fill(BG_COLOR)
                draw_text('X WIN!',font,CROSS_COLOR,130,250)
            win_sound.play()
            return True
    # horizontal win check
    for row in range(BOARD_ROWS):
        if board[row][0] == player and board[row][1] == player and board[row][2] == player:
            draw_horizontal_winning_line(row, player)
            pygame.display.update()
            sleep(1)
            if player == 1:
                screen.fill(BG_COLOR)
                draw_text('O WIN!',font,CIRCLE_COLOR,130,250)
            else:
                screen.fill(BG_COLOR)
                draw_text('X WIN!',font,CROSS_COLOR,130,250)
            win_sound.play()
            return True
    # asc diagonal win check
    if board[2][0] == player and board[1][1] == player and board[0][2] == player:
        draw_asc_diagonal(player)
        pygame.display.update()
        sleep(1)
        if player == 1:
            screen.fill(BG_COLOR)
            draw_text('O WIN!', font, CIRCLE_COLOR, 130, 250)
        else:
            screen.fill(BG_COLOR)
            draw_text('X WIN!', font, CROSS_COLOR, 130, 250)
        win_sound.play()
        return True
    # desc diagonal win check
    if board[0][0] == player and board[1][1] == player and board[2][2] == player:
        draw_desc_diagonal(player)
        pygame.display.update()
        sleep(1)
        if player == 1:
            screen.fill(BG_COLOR)
            draw_text('O WIN!', font, CIRCLE_COLOR, 130, 250)
        else:
            screen.fill(BG_COLOR)
            draw_text('X WIN!', font, CROSS_COLOR, 130, 250)
        win_sound.play()
        return True
    return False

def draw_vertical_winning_line(col, player):
    posX = col * SQUARE_SIZE + SQUARE_SIZE // 2
    if player == 1:
        color = CIRCLE_COLOR
    elif player == 2:
        color = CROSS_COLOR
    pygame.draw.line(screen, color, (posX, 15), (posX, HEIGHT - 15), LINE_WIDTH)

def draw_horizontal_winning_line(row, player):
    posY = row * SQUARE_SIZE + SQUARE_SIZE // 2
    if player == 1:
        color = CIRCLE_COLOR
    elif player == 2:
        color = CROSS_COLOR
    pygame.draw.line(screen, color, (15, posY), (WIDTH - 15, posY), WIN_LINE_WIDTH)

def draw_asc_diagonal(player):
    if player == 1:
        color = CIRCLE_COLOR
    elif player == 2:
        color = CROSS_COLOR
    pygame.draw.line(screen, color, (15, HEIGHT - 15), (WIDTH - 15, 15), WIN_LINE_WIDTH)

def draw_desc_diagonal(player):
    if player == 1:
        color = CIRCLE_COLOR
    elif player == 2:
        color = CROSS_COLOR
    pygame.draw.line(screen, color, (15, 15), (WIDTH - 15, HEIGHT - 15), WIN_LINE_WIDTH)

def restart():
    screen.fill(BG_COLOR)
    draw_lines()
    for row in range(BOARD_ROWS):
        for col in range(BOARD_COLS):
            board[row][col] = 0

def draw_text(text, font, text_col, x, y):
    img = font.render(text, True, text_col)
    screen.blit(img, (x, y))

def main():
    BG_COLOR = (61, 61, 61)
    screen.fill(BG_COLOR)
    draw_lines()
    start_sound.play()
    player = 1
    game_over = False
    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN and not game_over:
                mouseX = event.pos[0]  # x
                mouseY = event.pos[1]  # y
                clicked_row = int(mouseY // SQUARE_SIZE)
                clicked_col = int(mouseX // SQUARE_SIZE)
                if available_square(clicked_row, clicked_col):
                    mark_square(clicked_row, clicked_col, player)
                    draw_figures()
                    if check_win(player):
                        game_over = True
                        pygame.display.update()
                        sleep(3.5)
                        restart()
                        run = False
                    if is_board_full():
                        pygame.display.update()
                        sleep(3.5)
                        restart()
                        run = False
                    player = player % 2 + 1
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    restart()
                    player = 1
                    game_over = False
                if event.key == pygame.K_ESCAPE:
                    restart()
                    run = False
        pygame.display.update()

