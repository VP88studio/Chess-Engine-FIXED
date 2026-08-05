'''github save if my dumbass cant remember
git add .
git commit -m "Fixing repo and adding latest updates"
git push origin main'''

import pygame, math, time, sys, os
WIDTH = 1000
HEIGHT = 1000
GameBoard = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()
running = True
#load imgs
chessoldimg = pygame.image.load(os.path.join("Assets/gameboard.png"))
chessimg = pygame.transform.scale(chessoldimg, (1000, 1000))

#chess board nested list

chess_board = [
    [None, None, None, None, None, None, None, None],
    [None, None, None, None, None, None, None, None],
    [None, None, None, None, None, None, None, None],
    [None, None, None, None, None, None, None, None],
    [None, None, None, None, None, None, None, None],
    [None, None, None, None, None, None, None, None],
    [None, None, None, None, None, None, None, None],
    [None, None, None, None, None, None, None, None],
]

#chess board pos allocation
                        #Cords Here
chess_board[1][0] = 13, 13
chess_board[1][1] = 150, 950
chess_board[1][2] = 250, 950
chess_board[1][3] = 350, 950
chess_board[1][4] = 450, 950
chess_board[1][5] = 550, 950
chess_board[1][6] = 650, 950
chess_board[1][7] = 750, 950
print('x', chess_board[1][0][0])
print('y', chess_board[1][0][1])

#Peice Classes

class pawn:
    def ___init___(self):
        self
#testing area
test_bloc = {
    'x': chess_board[1][0][0],
    'y': chess_board[1][0][1],
    'width': 100,
    'height': 100,
    'color': (0, 0, 0)
}
rect_test = pygame.Rect((test_bloc['x'], test_bloc['y']), (test_bloc['width'], test_bloc['height']))

while running:
    
    GameBoard.blit(chessimg, (0,0))
    pygame.draw.rect(GameBoard, test_bloc['color'], rect_test)
    pygame.display.flip()