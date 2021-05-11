import numpy as np
import pygame as pg
import sys
import math

BLACK = (0,0,0)
RED = pg.Color("blue")
YELLOW = pg.Color("green")

ROW_COUNT = 7
COLUMN_COUNT = 7
HEIGHT = 20
WIDTH = 20


    
def textbox():   
    def main():
        screen = pg.display.set_mode((700, 500))
        font = pg.font.Font(None, 32)
        clock = pg.time.Clock()
        input_box = pg.Rect(0, 100, 300, 100)
        color_inactive = pg.Color('lightskyblue3')
        color = color_inactive
        active = False
        text = "Tutorial" \
               "the aim of this stratergy game is to line four of your game pieces either horizontally, vertically or diagonally" \
                
        
        done = False
        while not done:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    done = True
                

            screen.fill(('black'))
        
            txt_surface = font.render(text, True, color)
            
            width = max(200, txt_surface.get_width()+10)
            input_box.w = width
            
    
            screen.blit(txt_surface, (input_box.x+10, input_box.y+10))
            
            pg.draw.rect(screen, color, input_box, 2)

            pg.display.flip()
            clock.tick(30)

    if __name__ == '__main__':
        pg.init()
        main()
        pg.quit()
        game()

def game():
    def create_board():
        board = np.zeros((ROW_COUNT,COLUMN_COUNT))
        return board

    def drop_piece(board, row, col, piece):
        board[row][col] = piece

    def is_valid_location(board, col):
        return board[ROW_COUNT-1][col] == 0

    def get_next_open_row(board, col):
        for r in range(ROW_COUNT):
            if board[r][col] == 0:
                return r

    def print_board(board):
        print(np.flip(board, 0))

    def winning_move(board, piece):
        
        for c in range(COLUMN_COUNT-3):
            for r in range(ROW_COUNT):
                if board[r][c] == piece and board[r][c+1] == piece and board[r][c+2] == piece and board[r][c+3] == piece:
                    return True

        
        for c in range(COLUMN_COUNT):
            for r in range(ROW_COUNT-3):
                if board[r][c] == piece and board[r+1][c] == piece and board[r+2][c] == piece and board[r+3][c] == piece:
                    return True

        
        for c in range(COLUMN_COUNT-3):
            for r in range(ROW_COUNT-3):
                if board[r][c] == piece and board[r+1][c+1] == piece and board[r+2][c+2] == piece and board[r+3][c+3] == piece:
                    return True

        
        for c in range(COLUMN_COUNT-3):
            for r in range(3, ROW_COUNT):
                if board[r][c] == piece and board[r-1][c+1] == piece and board[r-2][c+2] == piece and board[r-3][c+3] == piece:
                    return True

    def draw_board(board):
        for c in range(COLUMN_COUNT):
            for r in range(ROW_COUNT):
                pg.draw.rect(screen, pg.Color("red"), (c*SQUARESIZE, r*SQUARESIZE+SQUARESIZE, SQUARESIZE, SQUARESIZE))
                pg.draw.circle(screen, pg.Color("white"), (int(c*SQUARESIZE+SQUARESIZE/2), int(r*SQUARESIZE+SQUARESIZE+SQUARESIZE/2)), RADIUS)

        for c in range(COLUMN_COUNT):
            for r in range(ROW_COUNT):		
                if board[r][c] == 1:
                    pg.draw.circle(screen, pg.Color("blue"), (int(c*SQUARESIZE+SQUARESIZE/2), height-int(r*SQUARESIZE+SQUARESIZE/2)), RADIUS)
                elif board[r][c] == 2: 
                    pg.draw.circle(screen, pg.Color("green"), (int(c*SQUARESIZE+SQUARESIZE/2), height-int(r*SQUARESIZE+SQUARESIZE/2)), RADIUS)
        pg.display.update()


    board = create_board()
    print_board(board)
    game_over = False
    turn = 0

    pg.init()

    SQUARESIZE = 80



    width = COLUMN_COUNT * SQUARESIZE

    height = (ROW_COUNT+1) * SQUARESIZE

    size = (width, height)

    RADIUS = int(SQUARESIZE/2 - 5)

    screen = pg.display.set_mode(size)

    draw_board(board)

    pg.display.update()

    myfont = pg.font.SysFont("monospace", 75)

    while not game_over:
        
        for event in pg.event.get():
            if event.type == pg.QUIT:
                sys.exit()
                
            if event.type == pg.MOUSEMOTION:
                pg.draw.rect(screen, BLACK, (0,0, width, SQUARESIZE))
                posx = event.pos[0]
                if turn == 0:
                    pg.draw.circle(screen, RED, (posx, int(SQUARESIZE/2)), RADIUS)
                else: 
                    pg.draw.circle(screen, YELLOW, (posx, int(SQUARESIZE/2)), RADIUS)
            pg.display.update()

            if event.type == pg.MOUSEBUTTONDOWN:
                pg.draw.rect(screen, BLACK, (0,0, width, SQUARESIZE))
                
                if turn == 0:
                    posx = event.pos[0]
                    col = int(math.floor(posx/SQUARESIZE))

                    if is_valid_location(board, col):
                        row = get_next_open_row(board, col)
                        drop_piece(board, row, col, 1)

                        if winning_move(board, 1):
                            label = myfont.render(Player1.upper() + " WINS!!", 1, RED)
                            screen.blit(label, (40,10))
                            game_over = True


                
                else:				
                    posx = event.pos[0]
                    col = int(math.floor(posx/SQUARESIZE))

                    if is_valid_location(board, col):
                        row = get_next_open_row(board, col)
                        drop_piece(board, row, col, 2)

                        if winning_move(board, 2):
                            label = myfont.render(Player2.upper() + " WINS!!", 1, YELLOW)
                            screen.blit(label, (40,10))
                            game_over = True
                            
                print_board(board)
                draw_board(board)

                turn += 1
                turn = turn % 2
                
                if game_over:
                    
                    pg.time.wait(3000)
                    celebration()

def celebration():
    global HEIGHT
    global WIDTH
    pg.init()
    
    screen = pg.display.set_mode((700,500), 0, 32)

    dogeImg = pg.image.load('dogecoin.png')
    dogex = 150
    dogey = 200
    direction = 'right'
    
    screen.blit(dogeImg, (dogex, dogey))
    running = True 
    while running:
        pg.display.flip()
        for event in pg.event.get():
            if event.type == pg.QUIT:
                running = False



Player1 = input("Player 1 enter your name: ")
Player2 = input("Player 2 enter your name: ")
tutorial = input('''Do you know how to play connect four:
[a] no
[b] yes 
''')
if tutorial == "b":
    game()
if tutorial == "a":
    textbox()